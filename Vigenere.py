
# e paperfunduar  (ne process)...-------------

def mesazhi_qelsi():
    mesazhi = input("VEndose mesazhin: ").upper()
    qelsi = input("Vendose qelsin: ").upper()

    vlera_qelsit =""

    j=0
    for i in range(len(mesazhi)):
        if ord(mesazhi[i]) == 32:
            vlera_qelsit += " "
        else:
            if j < len(qelsi):
                vlera_qelsit += qelsi[j]
                j += 1
            else:
                j = 0
                vlera_qelsit += qelsi[j]
                j += 1
   # print(vlera_qelsit)
    return mesazhi, vlera_qelsit

def vigenere_table():
    table = []
    for i in range(26):
        table.append([])

    for rreshti in range(26):
        for kolona in range(26):
            if(rreshti + 65) + kolona > 90:
                table[rreshti].append(chr((rreshti + 65) + kolona - 26))
            else:
                table[rreshti].append(chr((rreshti+ 65) + kolona))

    # printimi i tabeles
    # for rreshti in table:
    #    for kolona in rreshti:
    #       print(kolona, end=" ")
    #  print(end="\n")

    return table

def cipher_enkriptimi(mesazhi, vlera_qelsit):
    table = vigenere_table()
    teksti_inkriptuar = ""

    for i in range(len(mesazhi)):
        if mesazhi[i] == chr(32):
            #injoron
            teksti_inkriptuar += " "
        else:
            rreshti = ord(mesazhi[i]) - 65
            kolona = ord(vlera_qelsit[i]) - 65
            teksti_inkriptuar += table[rreshti][kolona]

    print("Mesazhi i inkriptuar: " + teksti_inkriptuar)


def main():
    print("Qelesi dhe mesazhi duhet te jene String")
    choice = int(input("1.Enkriptimi\n2.Dekriptimi\n3.Zhgjidh(1 ,2): "))
    if choice == 1:
        print("--Enkriptimi--")
        mesazhi, vlera_qelsit = mesazhi_qelsi()
        cipher_enkriptimi(mesazhi, vlera_qelsit)

    elif choice == 2:
        print("--Dekriptimi--")

    else:
        print("Gabim ju lutem zgjidh njerin opsion: ")


if __name__ == "__main__":
    main()