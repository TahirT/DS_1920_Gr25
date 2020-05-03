import sys


def main():
    print("-----------------------------------------------------------------------------\n")
    inputi = input()
    komanda = inputi.split()

    try:
        vlera = komanda[0]
        lloji = komanda[1]
        emri = komanda[2]
        ruaj = komanda[3]+".xml"


        if vlera.upper() == "EXPORT-KEY":
            if lloji.upper() == "PUBLIC":
                emri1 = emri + ".pub.xml"
                file = open("Keys/"+ emri1,"r")
                if file.mode == "r":
                    permbajtja = file.read()
                    f = open(ruaj,"a+")
                    f.write(permbajtja)
                    print("Qelesi publik u ruajt ne fajllin "+ruaj)
                    Provo()

            elif lloji.upper() == "PRIVATE":
                emri1 = emri + ".xml"
                file = open("Keys/" + emri1, "r")
                if file.mode == "r":
                    permbajtja = file.read()
                    f = open(ruaj, "a+")
                    f.write(permbajtja)
                    print("Qelesi privat u ruajt ne fajllin " + ruaj)
                    Provo()
        else:
            print("Gabim ju lutem vendosni komanda valide shemb(export-key public filan fiskteku)\n")
            Provo()
    except:
        print("Gabim ju lutem vendosni komanda valide shemb(export-key public filan fiskteku)\n")
        Provo()
def Provo():
            zgjedhja = input("Deshiron te provoshe perser(PO/JO):")
            if zgjedhja.upper() == "PO":
                main()
            else:
                print("----Procesi perfundoi-----")

if __name__ =="__main__":
    main()