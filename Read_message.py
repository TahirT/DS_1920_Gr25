import cryptography
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
import sys


def main():
    type = input()




    if type.upper() == "READ-MESSAGE":
        print("funskionn")
        mesazhi = input("Sheno Mesazhin: ")
        marresi = input("Marresi: ")

        with open("Keys/key1.pem", 'rb') as key_file:
            private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=None,
                backend=default_backend()

            )
        public_key = private_key.public_key()


        # mesazhi1 =b"\x8d\xe2\x13\xab\xde\x92\x88(\xed3\xd0+9+\x13\x89c\x07.I\x1b\xe4Ao'\xbb\x84W@!Jl\x88\x05\xb7\xe1\x03\xf4\xa95\x00u\xed\xad\xc9\xe1o\x0c\x83O\x05\t6\x8eeH\xfb\xa1c\xf3\xfbs\x17\x8d\x95\xb31\xc9\xba9t\x92phR\x1d\x91\xdb\xd5\x8d\x1a/\x03\x8e_\xe5b\xf3h\xf4\xf1'}\x16\xf3<\xd9_N`\x1ax\x9d\x9d\xb9\xe8\xb8\xf5\x83\xff\xb9\x86T\xd25\xd2\xa4\xc0\xa5^=\x84\xb8\xfc \xc0\xc4)\x84\xef\x85\xc0\x06\xc6\xda\xad\xdc\xc1\xdb!\xcd\x93\xb8$=p'\xed\xf6S\x9b\x1f\xfap\x93\x9d\xc1x\x1da|\xce#\x11\nY_p\xfd*\x03h\x82\xd3\x02-\x03\r\xa0\xd0\xd2\xd5,\xd5\xaeJr#DG\xab\x9c\xb8g\x9au)\xd18[~\xcfB\x16\xfe5-\xf5C\xf9d\x1c\x15%\xf2T\xd2\xd1.\xd7\x88pncEh|\x18\x0e\x1e\x02\xc8\x924`\xdd\xe9/#,\x16C\x11q\xa7U\xf0\xcd\xbd|{,\xc3C\xe8I"

        mesazhi1 = eval(mesazhi)


        plaintext = private_key.decrypt(
            mesazhi1,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA1()),
                algorithm=hashes.SHA1(),

                label=None
            )

        )
        try:
            merr = open("Keys/" + marresi + ".xml")
            if merr.mode == "r":
                print("Mesazhi: " + str(plaintext))
        except:
                print("Gabim: Celesi privat "+ marresi +".xml nuk ekziston!")



def Provo():
    zgjedhja = input("Deshiron te provoshe perser(PO/JO):")
    if zgjedhja.upper() == "PO":
        main()
    else:
        print("----Procesi perfundoi-----")


if __name__ == '__main__':
    main()
