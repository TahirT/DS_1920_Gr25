from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import  hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
import sys


def main():
        inputi = input()
        komanda = inputi.split('"')
        try:
            mesazhi = komanda[1]
            try:
                shtegu = komanda[2]
                shtegu = shtegu[1:]
                print(shtegu)
            except:
                print("")
        except:
            print("Ju lutem vendosni mesazhin ne thonjeza!\nShemb: Write-Message emri \"mesazhi\" shtegu")
            Provo()
        komanda = inputi.split()



        type = komanda[0]
        emri = komanda[1]



        if type.upper() == "WRITE-MESSAGE":
            emri = ""+emri+".pub.xml"
            try:
                file = open("Keys/" + emri, "r")
                if file.mode == "r":
                    private_key = rsa.generate_private_key(
                        public_exponent=65537,
                        key_size=2048,
                        backend=default_backend()
                    )

                    public_key = private_key.public_key()
                    #konverton mesazhin ne bytes
                    arr = bytes(mesazhi, 'utf-8')
                    #enkriptimi i mesazhit duke perdoreur qelesin publik te gjeneruar nga vet sistemi rsa
                    ciphertext = public_key.encrypt(
                        arr,
                        padding.OAEP(
                            mgf=padding.MGF1(algorithm=hashes.SHA1()),
                            algorithm=hashes.SHA1(),
                            label=None
                        )

                    )
                    try:
                        file = open("Keys/"+shtegu, "a+")
                        file.write(str(ciphertext))
                        print("Mesazhi i enkriptuar u ruajt ne fajllin "+shtegu+".")
                        Provo()
                    except:
                        print(ciphertext)
                        Provo()

            except:
                print("Gabim: Celesi publik "+emri+" nuk ekziston")
                Provo()
        else:
            print("Vendos komanda valide!")
            Provo()

def Provo():
    zgjedhja = input("Deshiron te provoshe perser(PO/JO):")
    if zgjedhja.upper() == "PO":
        main()
    else:
        print("----Procesi perfundoi-----")

if __name__ == '__main__':
    main()
