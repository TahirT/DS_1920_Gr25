from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
import os
os.chdir('Keys')
def main():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()

    )

    public_key = private_key.public_key()

    message = b"Qelesi eshte i sigurte"

    ciphertext = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA1()),
            algorithm=hashes.SHA1(),
            label=None

        )
    )
    print(ciphertext)

    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA1()),
            algorithm=hashes.SHA1(),
            label=None
        )
    )
    print(plaintext)
    def Provo():
        zgjedhja = input("Deshiron te provoshe perser(PO/JO):")
        if zgjedhja.upper() == "PO":
            CreateUser()
        else:
            print("----Procesi perfundoi-----")
    def CreateUser():
        listaUser = []
        komanda = input("\nVendos Komanden: ")
        user = komanda[12:]
        print(user)
        print(komanda[0:11])

        if komanda[0:11].upper() == "CREATE-USER":
            if user in listaUser:
                a = "Gabim: " + user +" ekziston paraprakisht."
                Provo()
            elif user not in listaUser:
                listaUser.append(user)
                with open("public_key.xml", "w+") as user:
                    user.write("Ky eshte qelsi publik\n")

                with open("private_key.xml", "w+") as user:
                    user.write("Ky eshte qelsi private\n")
                    print(user.closed)
                    print(listaUser)
                    Provo()
    CreateUser()

if __name__=="__main__":
    main()
