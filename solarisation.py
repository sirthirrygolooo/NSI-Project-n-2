from image_manip import *

"""
Cette fonction remplace chaque pixel par un pixel mais de saturation maximale. Le paramètre est l'image de l'utilisateur
choisie dans le fichier main.py

"""
def solarisation(image):

    # get the size of the picture stored in the image var.
    width, height = image_size(image)
    # creation of the new image to apply the filter on it
    new_pic = new_image((width,height))
    print('Application du filtre en cours...')
    for i in range(height):
        for k in range(width):
            
            # une déclaration try - except pour éviter les erreurs de type opératoires non supportés
            try:
                rgb = get_pixel(image, (k, i))
                # prend la valeure hsl a partir du rgb
                # change le type en list pour pouvoir modifier les valeures
                hsl = list(rgb_to_hsl(rgb))
                # attribue la saturation opposée 
                hsl[0] = 360 - (180 - hsl[0])
                # crée un nouveau pixel avec les valeures et repasse les valeurs en rgb tout en remettant sous forme de tuple
                new = hsl_to_rgb(tuple(hsl))
                put_pixel(new_pic, (k, i), new)
            
            # fin de la déclaration try - except avec gestion de l'erreur
            except TypeError:
                continue
                
    print("Ouverture de l'image... Appuyez sur entrée une fois l'image fermée pour continuer")
    show_image(new_pic)