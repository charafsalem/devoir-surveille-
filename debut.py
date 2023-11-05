import maskpass
import exercice


def afficher_menu():
    print("Connexion :")
    print("1. Enregistrement ")
    print("2. Authentification")

    print("3. Quitter")

def option1():
    print("Vous avez choisi l'option 1.")


def option2():
    print("Vous avez choisi l'option 2.")


def option3():
    print("Vous avez choisi l'option 3.")


while True:
    afficher_menu()
    choix = input("Entrez le numéro de l'option que vous souhaitez sélectionner : ")

    if choix == "1":

        # Modèle d'expression régulière pour une adresse email simple
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        import re

        while True:
            email = input("Entrez une adresse email : ")
            if re.match(pattern, email):
                # print("Adresse email valide : ", email)
                break
            else:
                print("Adresse email invalide. Veuillez réessayer.")


        def Introduire_pwd():
            import hashlib
            import maskpass
            import string

            while True:
                p = maskpass.askpass()
                if (len(p) == 8):
                    if any(c in string.digits for c in p):
                        if any(c in string.ascii_uppercase for c in p):
                            if any(c in string.ascii_lowercase for c in p):
                                if any(c in string.punctuation for c in p):
                                    p = hashlib.sha256(p.encode()).hexdigest()
                                    return p
                                else:
                                    print("SVP au min un caractere special")
                            else:
                                print("SVP au min un caractere minuscule")
                        else:
                            print("SVP au min un caractere majuscule")
                    else:
                        print("SVP au min un chiffre")
                else:
                    print("SVP le mot de passe est de 8 caractères")

        y = Introduire_pwd()

        with open("mon_fichier.txt", "w") as fichier:

            resultat = "Ceci est le résultat que vous souhaitez enregistrer dans le fichier."
            fichier.write(resultat)



        print("Résultat enregistré avec succès dans 'mon_fichier.txt'")

    elif choix == "2":


        adresse_mail = input("Entrez votre adresse e-mail : ")
        p = maskpass.askpass()

        with open('cyber.txt', "w") as fichier:
            fichier.write(p + "\n")

        with open('cyber.txt', "r") as fichier:
            cyber = fichier.read().splitlines()
            if p in cyber:

                print("taper 1 pour le chiffrement")
                print("taper 2 pour le déchiffrement")
                print("taper 3 pour calculer le hachage d'un pwd")
                print("taper 4 pour pour attaque de dictionnaire")
                print("taper 5 pour pour genere un salt (bcrypt)")
                choix = input("donner votre choix ")


                if choix == "1":
                    print(exercice.cesar())
                    break
                elif choix == "2":
                    print(exercice.cesar_dechiff())
                    break
                elif choix == "3":
                    print(exercice.hachage())
                    break
                elif choix == "4":
                    print(exercice.dict())
                    break
                elif choix == "5":
                    print(exercice.bcrypt())
                    break

            else:
                print("Utilisateur introuvable veuillez vous connecter.")

    elif choix == "3":
        print("Au revoir !")

        break
    else:
        print("Option invalide. Veuillez entrer un numéro valide.")