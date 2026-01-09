def elso():
    print("I/A. feladat, bekérés")
    nev=input("Név: ")
    kor=int(input("kor: "))
    print("I/B feladat, kiírás")
    if kor<14:
        print(f"{nev} kora {kor} év, még gyerek")
    if kor<18:
        print(f"{nev} kora {kor} év, még kiskorú")
    if kor>21:
        print(f"{nev} kora {kor} év, már nagykorú")
        
