from random import randint
from PIL import Image

def denominateurOptCommune(l1:list,l2:list)->list:
    res=[]
    for i in l1:
        for j in l2:
            if i==j:res.append(i)
    return res

def generate(world,d:dict,taille):
    t=world
    d_k=list(d.keys())
    for i in range(taille):
        if len(t)<=i:
            t.append([])
        for j in range(taille):
            #print(i)
            #print(len(t[i]))
            if len(t[i])>j:
                pass
            else:
                #print(i,j)
                if i==0 and j==0:
                    t[i].append(d_k[randint(0,len(d_k)-1)])
                elif i==0:
                    #print(t[i][j-1])
                    #print(d[t[i][j-1]])
                    t[i].append(d[t[i][j-1]][randint(0,len(d[t[i][j-1]])-1)])
                elif j==0:
                    #print(d[t[i-1][j]])
                    t[i].append(d[t[i-1][j]][randint(0,len(d[t[i-1][j]])-1)])
                else:
                    #print(d[t[i-1][j]])
                    #print(t[i][j-1])
                    #print(d[t[i][j-1]])
                    possibility=denominateurOptCommune(d[t[i-1][j]],d[t[i][j-1]])
                    t[i].append(possibility[randint(0,len(possibility)-1)])
    return t

def genDict(n):
    d={0:[0,1]}
    for i in range(1,n+1):
        if not i==n:
            d[i]=[i-1,i,i+1]
        else:
            d[i]=[i-1,i]
    return d

def printWorldGrid(world):
    for i in world:
        print(i)

def afficher_monde(monde, echelle=5):
    couleurs = {
        0: (200, 200, 200),
        1: (0, 50, 200),
        2: (200, 200, 0),
        3: (50, 200, 50),
        4: (25, 100, 25),
        5: (50, 50, 25),
        6: (0, 0, 0)
    }

    hauteur, largeur = len(monde), len(monde[0])
    image = Image.new("RGB", (largeur, hauteur))
    for y in range(hauteur):
        for x in range(largeur):
            image.putpixel((x, y), couleurs[monde[y][x]])

    image = image.resize((largeur * echelle, hauteur * echelle), Image.NEAREST)
    image.show()

world=[[0,0,0]]
taille=100
#d={"r":"t","t":"t"}
#print(list(d.keys()))
option=genDict(5)
#print(option)
#d=list(option.keys())
#print(d)
world=generate(world,option,taille)
#printWorldGrid(world)
afficher_monde(world)