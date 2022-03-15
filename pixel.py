from PIL import Image
from os import system

def pixel(image) :
    # Ce programme découpe en carré de 16 et en adapte juste le nombre selon l'image 


    """ Fonction qui permet de trouver l'entier qui multiplié par la largeur donne 0 """
    def get_width(width):
        n = 0
        x = width
        while (16*n) != x :
            n += 1
    
        return n

    """ Fonction qui permer de trouver l'entier qui multiplié par la longueur donne 0 """
    def get_height(height) :
        n = 0
        x = height
        while (16*n) != x :
            n += 1
    
        return n

    """ Fonction qui prend en paramètre une des variables r,g ou b + le nombre de carré de 16 a mettre en longueur et largeur
        et qui retourne la moyenne sous la forme Sequence[int] qui est le format requis pr le param. data de .putdata 
    """
    def pixel(l,p,q):
        for a in range(q):
            for c in range(p):
                mo=0
                for d in range(16):
                    for b in range(16):
                        mo=mo+l[a*256*p+b*16*p+c*16+d]
                mo=int(mo/256)
                for d in range(16):
                    for b in range(16):
                        l[a*256*p+b*16*p+c*16+d]=mo
        return l


    p= get_width(image.width)   # largeur de l'image
    q= get_height(image.height)    # longueur de l'image
    # ouverture + splitage de l'image
    im = image
    r,g,b=im.split()

    # transformation de chaque image en liste et récupération des valeurs des pixels + passage de ces données en liste 
    r=list(r.getdata())
    # utilisation de la fonction pixel pour créer le carré de 16
    r=pixel(r,p,q)

    # même procéssus pour le vert et le bleu (g--> green/vert; b--> blue/bleu)

    g=list(g.getdata())
    g=pixel(g,p,q)

    b=list(b.getdata())
    b=pixel(b,p,q)
    # création de 3 nouvelles images (une pour chaque variable) et copie les donnnées de type 'séquence' (dans notre cas un tableau) 
    # issues de la fonction pixel sur une image
    nr = Image.new("L",(16*p,16*q))
    nr.putdata(r)
    ng = Image.new("L",(16*p,16*q))
    ng.putdata(g)
    nb = Image.new("L",(16*p,16*q))
    nb.putdata(b)

    # fusion des trois nouvelles images en une seule --> new_image
    new_image = Image.merge('RGB',(nr,ng,nb)) 
    print('Ouverture de l\'image')
    new_image.show()

    # new_image.save('') # pour sauvegarder l'image mais flemme