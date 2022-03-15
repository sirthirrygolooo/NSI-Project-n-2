from image_manip import *


"""
comme le dit le nom de la fonction, prend en paramètre l'image de l'utilisateur et applique un effet de convolution dessus
pixel par pixel

"""

def i_do_a_convolution(your_image):

    image = your_image
    width, height = image_size(image)
    
    # création d'une nouvelle image sur laquelle appliquer le filtre 
    new = new_image((width,height))
    
    """
    la fonction convolution prend en paramètre x et y 
    la variable matrice contient les valeurs nécéssaires à l'application d'un filtre de 
    détection de contours (filtre laplacien) 
    new_r, new_v et new_b contiendront les nouvelles valeurs colorimétriques et sont réglées sur zero au début
    du programme

    """
    
    def convolution(x, y):
        matrice = [[0, 1, 0], [1, -4, 1], [0, 1, 0]]
        new_r = 0
        new_v = 0
        new_b = 0

        # carré de 3*3
        for k in range(3):
            for i in range(3):
                new_r += get_pixel(image, (x, y))[0] * matrice[k][i]
                new_v += get_pixel(image, (x, y))[1] * matrice[k][i]
                new_b += get_pixel(image, (x, y))[2] * matrice[k][i]
            x -= 3

        if 25 < new_r < 255 or 25 < new_v < 255 or 25 < new_b < 255:
            new_r = 0
            new_v = 0
            new_b = 0
        else:
            new_r = 255
            new_v = 255
            new_b = 255

        pixel_centre = (x+1 , y-1)
        
        put_pixel(new, pixel_centre, (new_r, new_v, new_b))
    x = 0
    y = 0  
    
    print('Calcul en cours...')
    # applique la fonction convolution(x,y) sur toute l'image ou a est l'axe y et b l'axe x
    
    for a in range((height)):
        for b in range((width)):
            convolution(x, y)
            x += 1
        x = 0
        y += 1
    print('Affichage de l\'image... Appuyez sur entrée une fois celle-ci fermée pour continuer...')
    show_image(new)