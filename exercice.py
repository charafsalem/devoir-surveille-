def cesar():
    msg = input("donner un message a chiffré: ")
    while True:
        try:
            cle = int(input("donner une clé de décalage: "))
            break

        except ValueError:
            print("merci d'introduire un entier")
    chiffre = ""
    for i in msg :
        chiffre+=chr((ord(i)+cle)%1000)
    return chiffre


def cesar_dechiff():
    msg = input("donner un message a dechiffré: ")
    while True:
        try:
            cle = int(input("donner une clé de décalage: "))
            break

        except ValueError:
            print("merci d'introduire un entier")
    chiffre = ""
    for i in msg :
        chiffre+=chr((ord(i)-cle)%1000)
    return chiffre
def hachage():
    import hashlib
    import maskpass


    msg = maskpass.askpass()
    return hashlib.sha256(msg.encode()).hexdigest()

f1 = open('doc.txt' ,'r')
def dict():

import hashlib
import pyautogui

pwd = pyautogui.password("tapez le mot de passe : ")
pwd1=hashlib.md5(pwd.encode()).hexdigest()
def reading_data(f):
    while True:

         data = f.readline().strip()
         if (data == '') or (data == None):
            break
         if hashlib.md5(data.encode()).hexdigest() == pwd1:
             print(f"The hash of your password : {hashlib.md5(data.encode()).hexdigest()} was Cracked, \n your password:{pwd}")
             break

    if not data:
        print("password not found :( ")

reading_data(f1)


    def bcrypt()
mot_a_hasher = maskpass.askpass(&quot;Entrez le mot à hacher : &quot;)
salt = bcrypt.gensalt()
hashed_password = bcrypt.hashpw(mot_a_hasher.encode(), salt)
print(f&quot;Hachage bcrypt : {hashed_password}&quot;)