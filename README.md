<!-- -->

# README projet de NSI n°2 Mars 2022  

Informations techniques relatives au projet et à son
fonctionnement.

***

## __Sommaire__ :

- [README projet de NSI n°2 Mars 2022](#readme-projet-de-nsi-n2-mars-2022)
  - [__Sommaire__ :](#sommaire-)
    - [__Projet 2__](#projet-2)
    - [__Installation__](#installation)
    - [__Bibliothèques requises__](#bibliothèques-requises)
    - [__A propos__](#a-propos)
    - [__Informations Complémentaires__](#informations-complémentaires)



### __Projet 2__


> Ce projet a pour objectif de créer dans un premier temps
un programme de traitement d'images de par l'application de différents filtres sur une image selectionnée puis, dans un second temps donner à l'utilisateur la possibilité de jouer au jeu du taquin avec son image (partie non achevée dans notre cas)

***

### __Installation__ 
> Depuis github
<!--  -->
Cloner le dépot :

        git clone https://github.com/sirthirrygolooo/NSI-Project-n-2

Aller dans le répertoire requis avec 

        cd NSI-Project-n-2

Une fois dans le dossier :

>Lancer le fichier de configuration windows (launch.bat) et dans le cas ou vous n'avez pas les bibliothèques requises, utilisez l'option I afin de les installer (cela requiert d'avoir le module pip fourni avec python)  
<!--  -->
>Une fois les bibliothèques installées, utilisez l'option S pour lancer le programme et suivez les instructions/propositions à l'écran.
<!--  -->
> Possibilité de vérifier la version de python avec l'option V ou avec la commande windows : 
<!--  -->
    python --version


***

### __Bibliothèques requises__ 
__Pour des raisons de compatibilité avec pillow, python 3.8.2 est fortement suggéré__

    Bibliothèquees :
    - Pillow (PIL) > Python 3.8.2 fortement recommandé 
    - TKinter (TK) > Python 3.8 ou supérieur
    - Image_manip est inclue dans les fichiers
    - OS est inclue par défaut dans python

***

### __A propos__

Projet réalisé par __Deroze Clément__, __Godel Oxane__, __Sutter Gautier__ et __Froehly Jean-Baptiste__ dans le cadre du projet de NSI.  
Ce projet n'est pas complètement achevé : seule la partie traitement d'image est fonctionnelle mais pas la partie taquin qui ne permet pas d'utiliser une image.

***

### __Informations Complémentaires__ 

Ce projet a été développé sous python 3.8.2 et prend en compte les formats d'image suivants :

- [x] PNG --> Format recommandé
- [x] JPG
- [ ] GIF
- [x] BNP
- [x] SVG

__Attentention ! Certains filtres peuvent mettre du temps à s'appliquer du fait du traitement pixel par pixel qui peut prendre du temps (2073600 pixels a traiter pour une image en 1920x1080)__
***
![Github](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Flogosmarcas.net%2Fwp-content%2Fuploads%2F2020%2F12%2FGitHub-Simbolo.png&f=1&nofb=1 "github logo")

Projet disponible sur github via ce lien :

[Lien Github vers NSI-Project-n-2](https://github.com/sirthirrygolooo/NSI-Project-n-2 "Lien github du projet")




