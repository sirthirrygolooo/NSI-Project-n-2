from os import system

def taquin(image) :
    system('cls')
    print(r'Pas reussi \(ToT)/')

def rules():
    system('cls')
    print("""
    Les règles sont assez simple : l'image est décomposée en différent carrés de taille
    identiques. L'objectif est de reconsitutuer l'image en bougeant ces carrés de manière
    latérale. 
    Pour y jouer tapez 2 une fois dans le menu... (c'est faux ca marche pas haha)
    
    """)

def colors():
    system('cls')
    system('title option du futur incroyablement innovante sans exageration et ce n\'est absolument pas pour meubler le fait que le jeu ne marche pas')
    print("""
    ~ Rouge
    ~ Vert 
    ~ Bleu 
    ~ Blanc 
    ~ Cyan 
    """)

    choice = str(input('Faites votre choix >> '))

    if choice == 'rouge' or choice == 'Rouge' :
        system('color 04')
    elif choice == 'vert' or choice == 'Vert' :
        system('color 0A')
    elif choice == 'Bleu' or choice == 'bleu' :
        system('color 01')
    elif choice == 'blanc' or choice == 'Blanc' :
        system('color 0F')
    elif choice == 'cyan' or choice == 'Cyan' :
        system('color 0B')
    else :
        print('Il n\'y a pas cette couleur désolé recommence !')
        system('pause')
        colors()