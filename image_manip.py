#
# PROJET 2 - MANIPULATION D'IMAGE
#
# Ce fichier contient des fonctions utiles pour la manipulation d'images
# Il peut être importé avec la ligne
#	from image_manip import *
#
# Création, chargement et enregistrement des images :
#	image = new_image(taille, couleur)
#	image = open_image(file)
#	save_image(image, file)
#
# Affichage
#	show_image(image)
#	show_histogram(histo)
#
# Manipulation de pixels
#	largeur, hauteur = image_size(image)
#	couleur = get_pixel(image, (i, j))
#	put_pixel(image, (i, j), couleur)
#
# Copier-coller des sous-images
#	simg = copy_subimage(image, (x1, y1, x2, y2))
#	paste_subimage(simg, image, (x1, y1, x2, y2))
#
# Conversion entre systèmes de couleurs :
# 	hsl_pixel = rgb_to_hsl(rgb_pixel) : convertit une valeur (r, v, b) en (h, s, l)
# 	rgb_pixel = hsl_to_rgb(hsl_pixel) : convertit une valeur (h, s, l) en (r, v, b)

from PIL import Image

def new_image(taille, couleur = None):
	""" Crée une nouvelle image de la taille donnée (sous forme de tuple (largeur, hauteur)).
		La couleur est optionnelle (defaut est noir). Si elle est spécifiée, ce doit être un triplet (r, v, b)
	"""
	if couleur is None:
		return Image.new('RGB', taille)
	return Image.new('RGB', taille, color = couleur)

def open_image(file):
	""" Ouvre le fichier image `file` et retourne l'image correspondante """
	return Image.open(file)

def save_image(image, file):
	""" Enregistre l'image dans le fichier (format JPEG) """
	image.save(file, 'JPEG')

def show_image(image):
	""" Affiche l'image dans une fenêtre séparée (Python) ou dans le notebook (Jupyter) """
	import sys
	if 'ipykernel' in sys.modules:
		# Dans Jupyter convertir l'image en tableau pour utiliser matplotlib
		import matplotlib.pyplot as plt
		import numpy as np

		im_array = np.asarray(image)
		plt.axis('off')
		plt.imshow(im_array)
		plt.show()
	else:
		# Dans Python afficher dans une nouvelle fenêtre
		image.show()

def show_histogram(histo):
	""" Affiche le contenu du tableau `histo` sous forme d'histogramme """
	import matplotlib.pyplot as plt
	plt.plot(histo)
	plt.show()

def image_size(image):
	""" Retourne la taille de l'image sous forme de tuple (largeur, hauteur) """
	return (image.width, image.height)

def get_pixel(image, coords):
	""" Retourne la valeur (r, v, b) du pixel 
		aux coordonnées coords (ligne, colonne) de l'image """
	return image.getpixel(coords)

def put_pixel(image, coords, couleur):
	""" Affecte la couleur au pixel de coordonnées coords (ligne, colonne) de l'image.
		La couleur doit être spécifiée sous forme de triplet (r, v, b)
	"""
	image.putpixel(coords, couleur)

def copy_subimage(image, rect):
	""" Retourne une nouvelle image dont le contenu est la partie de `image`
		définie par rect = (x1, y1, x2, y2)
	"""
	return image.crop(rect)

def paste_subimage(image, destimage, rect):
	""" Remplace par le contenu `image` la partie de `destimage`
		définie par rect = (x1, y1, x2, y2)
	"""
	image.paste(destimage, rect)

import math

def rgb_to_hsl(rgb_pixel):
	""" Convertit un pixel RVB représenté sous forme de tuple (r, g, b) 
		en sa valeur correspondante (h, s, l) dans le système HSL
	"""
	r, g, b = rgb_pixel
	R, G, B = r / 255., g / 255., b / 255.
	cmin = min(R, G, B)
	cmax = max(R, G, B)
	delta = cmax - cmin

	# initialiser la teinte, la saturation et la luminosité
	h = None
	s = 0.0
	l = (cmin + cmax) / 2.

	# niveau de gris -> pas de teinte
	if math.isclose(cmin, cmax):
		return (h, s, l)

	# calculer la saturation
	if l <= 0.5:
		s = (cmax - cmin) / (cmax + cmin)
	else:
		s = (cmax - cmin) / (2.0 - cmax - cmin)

	# calculer la teinte
	if cmax == R:
		h = (G - B) / delta
	elif cmax == G:
		h = 2.0 + (B - R) / delta
	else:
		h = 4.0 + (R - G) / delta

	# normaliser la teinte et retourner le résultat
	h *= 60.
	if h < 0:
		h += 360.
	return (h, s, l)


def hsl_to_rgb(hsl_pixel):
	""" Convertit un pixel HSL représenté sous forme de tuple (h, s, l) 
		en sa valeur correspondante (r, g, b) dans le système RVB
	"""
	h, s, l = hsl_pixel
	if h is None:
		h = 0.0

	# calculer les valeurs p et q utilisées par convert
	if l < 0.5:
		q = l + l*s
	else:
		q = l + s - l*s
	p = 2*l - q
	h = h / 360.0

	# initialiser les valeurs r, g, b
	r = h + 1./3.
	g = h
	b = h - 1./3.

	# calcule la valeur de la composante de couleur c
	# en fonction des valeurs de p et q calculées ci-dessus
	def convert(c):
		if c < 0.0:
			c += 1.0
		elif c > 1.0:
			c -= 1.0

		if c < 1./6.:
			return p + 6*c*(q-p)
		if c < 0.5:
			return q
		if c < 2./3.:
			return p + 6*(2./3.-c)*(q-p)
		return p

	# calculer les valeurs (r, g, b) et retourner le résultat
	r = round(convert(r) * 255)
	g = round(convert(g) * 255)
	b = round(convert(b) * 255)
	return (r, g, b)

