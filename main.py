#!/usr/bin/env python

# imports de Librairie
from image_manip import *
from os import system
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from quantification import quantification
from convolution import i_do_a_convolution
from solarisation import solarisation
from pixel import pixel
from taquin_game import taquin, rules, colors

SUPPPORTED_EXTENSIONS = ['.png','.jpg','.bnp','.svg']

# Titre de la fenêtre
system('title NSI project 2 by DEROZE Clement - SUTTER Gauthier - GODEL Oxane - FROEHLY Jean-Baptiste')
system('cls')

""" Fonction utilisant directement les class du fichiers filters pour appliquer les différents filtres
    à l'image selectionnée. Prend en paramètre l'image choisie par l'utilisateur

"""
def apply_filters(picture) :
    system('cls')
    print("""
    >> Ici, vous pouvez appliquer différente filtres à l'image choisie précédemment...
       Veuillez faire votre choix :
       [1] > Convolution de l'image (détection de contours/filtre Laplacien)
       [2] > Pixelliser l'image
       [3] > Quantifier l'image
       [4] > Solariser l'image
       [0] ~ Retourner au menu
    """)
    filter_choice = int(input('>> '))

    if filter_choice == 1 :
        i_do_a_convolution(picture)
        system('pause >> null')
        apply_filters(picture)
    elif filter_choice == 2 :
        pixel(picture)
        system('pause >> null')
        apply_filters(picture)
    elif filter_choice == 3 :
        quantification(picture)
        system('pause >> null')
        apply_filters(picture)
    elif filter_choice == 4 :
        solarisation(picture)
        system('pause >> null')
        apply_filters(picture)
    elif filter_choice == 0 :
        print('OK tu vas returner au menu dans deux secondes...')
        system('timeout -t 2 -nobreak >> null')
        menu()
    else :
        print('ce choix n\'est pas disponible veuillez réessayer :) ')
        system('pause')
        apply_filters(path)


""" Fonction faisant appel a tkinter et qui permet de choisir simplement à l'utilisateur
    de choisir un fichier dans son ordinateur, fichier dont la variable path va prendre la 
    valeur.
"""
def image_choice():
    choice = str(input('Voulez vous importer une image ? (le cas échéant, une image par def. sera utilisée | le format idéal est .png)\n[y/N]: '))
    if choice == 'y' or choice == 'Y' :
        Tk().withdraw()
        path = askopenfilename()
        check_user_choice = str(input(f'Votre image est bien {path} ? [Y/n]'))
        if check_user_choice == 'n' or check_user_choice == 'N' :
            system('cls')
            path = None
            image_choice()
        
        # gestion de l'erreur
        elif path == '':
            print('Veuillez entrer un chemin valide...')
            path = open_image(image_choice())
        else :
            # prend la valeur de l'extension de l'image
            path_extension = path[-4:]
            
            # regarde si cette extension est supportée
            if path_extension in SUPPPORTED_EXTENSIONS :
                print('Image compatible :)')
                return path
            else :
                system('cls')
                print('Fichier non supporté... Veuillez réessayer')
                system('pause')
                system('cls')
                path = open_image(image_choice())

    else :
        print('Vous choisissez l\'image par défaut...')
        path = 'pic.jpg'

        return path


""" Fonction permettant d'afficher le menu qui fait office de remplacement d'une interface graphique

"""

def menu():
    system('cls')
    print(r"""
  _   _  _____ _____    _____  _____   ____       _ ______ _____ _______   ___    ___  
 | \ | |/ ____|_   _|  |  __ \|  __ \ / __ \     | |  ____/ ____|__   __| |__ \  / _ \ 
 |  \| | (___   | |    | |__) | |__) | |  | |    | | |__ | |       | |       ) || | | |
 | . ` |\___ \  | |    |  ___/|  _  /| |  | |_   | |  __|| |       | |      / / | | | |
 | |\  |____) |_| |_   | |    | | \ \| |__| | |__| | |___| |____   | |     / /_ | |_| |
 |_| \_|_____/|_____|  |_|    |_|  \_\\____/ \____/|______\_____|  |_|    |____(_)___/ 
                                                                                      
---------------------------------------------------------------------------------------
-------------------------------------- MENU -------------------------------------------
---------------------------------------------------------------------------------------
    [1] Appliquer des filtres
    [2] Jouer au jeu du taquin 
    [c] Changer la couleur (très utile è_è)
    [r] Règles du jeu
    [x] A propos
    [e] Quitter
---------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------
    """)

    choice = input('Que voulez-vous faire ? > ')

    
    if choice == '1' :
        apply_filters(path)
    elif choice == '2' :
        taquin(path)
        system('pause')
        menu()
    elif choice == 'c' :
        colors()
        menu()
    elif choice == 'r' :
        rules()
        system('pause')
        menu()
    elif choice == 'x' :
        system('title A propos')
        system('cls')
        print('''
        ~ Projet réalisé dans le cadre d'un cours de NSI par :

        * Deroze Clément
        * Sutter Gauthier
        * Godel Oxane 
        * Froehly Jean-Baptiste 
        
        ~ 
        ''')
        system('pause')
        menu()
    elif choice == 'e' :
        print('Merci d\'avoir joué et à bientot !')
        exit()
    else :
        print('Ca marche paaaaas veuillez réessayer (-_-)')
        system('pause')
        menu()

path = open_image(image_choice())
menu()