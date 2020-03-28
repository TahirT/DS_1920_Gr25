import Four_square_cipher
import Vigenere
import sys
import Case

def main():
    print("Sheno cilin fajll do te ekzekutosh: ")
    sys.argv = input("vendos emrin e fajllit:").upper()
    if sys.argv == "VIGENERE" :
        Vigenere.main()

    elif sys.argv == "FOUR_SQUARE_CIPHER":
        Four_square_cipher.main()

    elif sys.argv == "CASE":
        Case.main()

    x = input("******Deshiron te provosh perseri: ").upper()
    if x == 'YES':
        main()
    elif x == 'NO':
        print("******Processi perfundoi*******")
        exit()

    else:
        print("Vendos vlera valide ")
        main()

if __name__ == "__main__":
    main()

