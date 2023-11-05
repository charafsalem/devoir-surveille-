import exercice
import attaque

quiter="f"
while quiter=="f":
    while True:


        print("taper 1 pour le chiffrement")
        print("taper 2 pour le déchiffrement")
        print("taper 3 pour calculer le hachage d'un pwd")
        print("taper 4 pour pour attaque de dictionnaire")
        choix = input("donner votre choix ")
        if choix=="1":
            print(exercice.cesar())
            break
        elif choix=="2":
            print(exercice.cesar_dechiff())
            break
        elif choix=="3":
            print(exercice.hachage())
            break
        elif choix=="4":
            print(attaque)
            break
        else:
            print("merci d'introduire 1 ou 2")

    quiter=input("si vous voulez quiter taper autre que f ")
print("aurevoir")
