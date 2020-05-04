import Four_square_cipher
import Vigenere
import sys
import Case
import Create_user
import Export_Key


def Provo():
    zgjedhja = input("Deshiron te provoshe perser(PO/JO):")
    if zgjedhja.upper() == "PO":
        main()
    else:
        print("----Procesi perfundoi-----")


def main():
    print("Sheno cilin fajll do te ekzekutosh: ")
    sys.argv = input("vendos emrin e fajllit:").upper()
    if sys.argv == "VIGENERE" :
        Vigenere.main()
        Provo()
    elif sys.argv == "FOUR_SQUARE_CIPHER":
        Four_square_cipher.main()
        Provo()
    elif sys.argv.upper() == "CREATE_USER":
        Create_user.main()
        Provo()

    elif sys.argv.upper() == "EXPORT_KEY":
        Export_Key.main()
        Provo()

    elif sys.argv == "CASE":
        Case.main()
        Provo()

    else:
        print("Vendos vlera valide ")
        main()

if __name__ == "__main__":
    main()
