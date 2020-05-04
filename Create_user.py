from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
import os
import os.path
import pathlib
os.chdir('Keys')
from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend as crypto_default_backend


def main():
    key = rsa.generate_private_key(
        backend=crypto_default_backend(),
        public_exponent=65537,
        key_size=2048
    )
    private_key = key.private_bytes(
        crypto_serialization.Encoding.PEM,
        crypto_serialization.PrivateFormat.PKCS8,
        crypto_serialization.NoEncryption())
    public_key = key.public_key().public_bytes(
        crypto_serialization.Encoding.OpenSSH,
        crypto_serialization.PublicFormat.OpenSSH
    )
    qelesiPriv = str(private_key)
    qelesiPub = str(public_key)
    def Provo():
        zgjedhja = input("Deshiron te provoshe perser(PO/JO):")
        if zgjedhja.upper() == "PO":
            CreateUser()
        else:
            print("----Procesi perfundoi-----")

    def CreateUser():
        listaUser = []
        while True:
            komanda = input("\nVendos Komanden: ")
            user = komanda[12:]
            print(user)
            if user.strip() != "":
                break

        a = "" + user + ".xml"
        b = "" + user + "pub.xml"

        if komanda[0:11].upper() == "CREATE-USER":
            if os.path.isfile(a):
                print("Gabim: Celesi \'"+ a +"\' ekziston paraprakisht.")
                Provo()
            elif user not in listaUser:
                listaUser.append(user)
                a = ""+ user +".xml"
                b = ""+user+".pub.xml"
                with open(a, "w+") as user:
                    user.write(qelesiPriv)
                    qelesi = "Eshte krijuar celesi privat 'keys/"+komanda[12:]+".xml'"
                    print(qelesi)
                    user.close()

                with open(b, "w+") as user:
                    user.write(qelesiPub)
                    qelesi1 = "Eshte krijuar celesi publik 'keys/" + komanda[12:] + ".pub.xml'"
                    print(qelesi1)
                    print(listaUser)
                    user.close()
                    Provo()
        
        elif komanda[0:11].upper() == "DELETE-USER":
            deleteUser(user)
            
    
    def deleteUser(user):
        a = ""+ user +".xml"
        b = ""+user+".pub.xml"
        if os.path.isfile(b) and os.path.isfile(a):
            os.remove(b)
            os.remove(a)
            
            print("Celesi privat\'" + a +"\' u fshi me sukses.")
            print("Celesi publik \'"+b+"\' u fshi me sukses.")
            Provo()
            
        elif os.path.exists(a) and not os.path.exists(b):
            os.remove(a)
            print("Celesi privat \'"+ a +"\' u fshi me sukses.")

        elif not (os.path.exists(a)) and os.path.exists(b):
            os.remove(b)
            print("Celesi publik \'"+ b +"\' u fshi me sukses.")

        else:
            print("Celesi \'" + a + "\' nuk ekziston.")
            Provo()

                
    CreateUser()


if __name__=="__main__":
    main()