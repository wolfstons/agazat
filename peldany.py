from Ember import Ember
def peldany():
    lali=Ember("lali",88)
    feri=Ember("feri",99)
    juli=Ember("juli",77)

    print(f"név: {lali.nev} \nkor: {lali.kor}")
    print(f"név: {juli.nev} \nkor: {juli.kor}")
    emberek=[lali,feri,juli]
    print(emberek)