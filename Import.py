import sys
import requests
import os.path

def main():
        print("-----------------------------------------------------------------------------\nVendos Komanden: ")
        inputi = input()
        komanda = inputi.split()
        try:
            importOrExport = komanda[0].strip()
            createKey = komanda[1].strip()
            fromKey = komanda[2].strip()
            if importOrExport.upper().strip() == "IMPORT-KEY":
                # Marrja e qelsit publik dhe vendosja ne nje file te caktuar
                # Marrja e qelsit permes metodes GET
                    if fromKey.startswith("http" or "https"):
                        contentFromUrl = requests.get(fromKey).content
                        print(contentFromUrl)
                        f = open("Keys/" + createKey + ".xml", "wb")
                        f.write(contentFromUrl)
                        f.close()
                        print("Qelesi publik u ruajt ne fajllin " + "Keys/" + createKey + ".xml")
                        zgjedhja = input("Deshiron te provoshe perser(PO/JO):")
                        if zgjedhja.upper() == "PO":
                            main()
                        else:
                            sys.exit()
                    f = open("Keys/" + fromKey , "r")
                    content = f.read()
                    f.close()
                    if("BEGIN PRIVATE KEY" in content):
                        # Marrja e qelsit privat dhe vendosja ne nje file te caktuar
                        f = open("Keys/" + fromKey, "r")
                        content = f.read()
                        f.close()
                        if os.path.isfile("Keys/" + createKey + ".xml"):
                            print("Gabim: Celesi " + createKey + " egziston paraprakisht.")
                            zgjedhja = input("Deshiron te provoshe perser(PO/JO):")
                            if zgjedhja.upper() == "PO":
                                main()
                            else:
                                sys.exit()
                        f = open("Keys/" + createKey + ".xml", "w")
                        f.write(content)
                        print("Qelesi privat u ruajt ne fajllin " + "Keys/" + createKey + ".xml")
                        f.close()
                        zgjedhja = input("Deshiron te provoshe perser(PO/JO):")
                        if zgjedhja.upper() == "PO":
                            main()
                        else:
                            sys.exit()
                    else:
                        #Marrja e qelsit publik
                        if os.path.isfile("Keys/" + createKey + ".pub.xml"):
                            print("Gabim: Celesi " + createKey + " egziston paraprakisht.")
                            zgjedhja = input("Deshiron te provoshe perser(PO/JO):")
                            if zgjedhja.upper() == "PO":
                                main()
                            else:
                                sys.exit()
                        f = open("Keys/" + createKey + ".pub.xml", "w")
                        f.write(content)
                        print("Qelesi publik u ruajt ne fajllin " + "Keys/" + createKey + ".pub.xml")
                        f.close()
                        zgjedhja = input("Deshiron te provoshe perser(PO/JO):")
                        if zgjedhja.upper() == "PO":
                            main()
                        else:
                            sys.exit()
            else:
                print("Komanda duhet te jet import-key!" + "\n")
                zgjedhja = input("Deshiron te provoshe perser(PO/JO):")
                if zgjedhja.upper() == "PO":
                    main()
                else:
                    sys.exit()
        except:
            print("Jepni te gjitha vlerat e nevojshme!")
            zgjedhja = input("Deshiron te provoshe perser(PO/JO):")
            if zgjedhja.upper() == "PO":
                main()
            else:
                sys.exit()

if __name__ =="__main__":
    main()