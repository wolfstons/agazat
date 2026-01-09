import random
def lista_keszit():
    print("II/A,kiírás")
    szamlista=[]
    i=0
    while i<7:
        szam=random.randint(10,99)
        szamlista.append(szam)
        i+=1
    return szamlista


def lista_kiír(szamlista):
    i=0
    while i<len(szamlista)-1:
        print(szamlista[i], end=";")
        i+=1
    print(szamlista[i] ,end="\n")



def paratlan(szamlista):
    cv=0
    db=0
    while cv<len(szamlista):
        if szamlista[cv]%2==1:
            db+=1
        cv+=1
    return db


def min(szamlista):
    i=0
    min=100
    while i<len(szamlista):
        if szamlista[i]<min:
            min=szamlista[i]
        i+=1
    return min


def max(szamlista):
    i=0
    max=0
    while i<len(szamlista):
        if szamlista[i]>max:
            max=szamlista[i]
        i+=1
    return max

    


def kiíras(min,max,db):
    print("III/B feladat, számolás")

    print(f"páratlanok száma: {db}")

    print(f"legkissebb érték {min},legnagyob érték {max}")

def fajlba_kiir(db):
    with open("paratlanok.txt","w",encoding="utf-8")as f:
        f.write(f"páratlanok száma: {db}")
    print(f"paratlanok.txt elkészült!")
    f.close()
