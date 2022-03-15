from image_manip import *

"""
Fonction qui applique un effet de quantification a l'image prise en paramètre 

"""

def quantification(image):
    
    # prend les dimensions de l'image et les attribue dans les variables correspondantes variables hauteur et largeur 
    width, height = image_size(image)

    # création d'une nouvelle image vierge de bonnes dimensions sur laquelle appliquer les filtres
    new = new_image((width,height))
    
    print('Application du filtre en cours...')

    # boucle qui vient appliquer les filtres pixel par pixel 
    for k in range(height):
        for i in range(width):
            rgb = get_pixel(image, (i, k))
            hsl = list(rgb_to_hsl(rgb))
            hsl[1] = 100
            nouveau_pixel = hsl_to_rgb(tuple(hsl))
            put_pixel(new, (i, k), nouveau_pixel)

    print("Ouverture de l'image... Appuyez sur entrée une fois l'image fermée pour continuer")
    show_image(new)