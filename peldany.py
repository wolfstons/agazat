from Ember import Ember
def peldany():
    lali=Ember("lali",88)
    feri=Ember("feri",99)
    juli=Ember("juli",77)

    print(f"név: {lali.nev} \nkor: {lali.kor}")
    print(f"név: {juli.nev} \nkor: {juli.kor}")
    emberlista=[]
    emberlista.append(lali)
    emberlista.append(feri)
    emberlista.append(juli)
