
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
    print(vlera_qelsit)
    return mesazhi, vlera_qelsit

def main():
    print("Qelesi dhe mesazhi duhet te jene String")
    choice = int(input("1.Enkriptimi\n2.Dekriptimi\n3.Zhgjidh(1 ,2): "))
    if choice == 1:
        print("--Enkriptimi--")
        message, mapped_key = mesazhi_qelsi()

    elif choice == 2:
        print("--Dekriptimi--")

    else:
        print("Gabim ju lutem zgjidh njrin opsion: ")


if __name__ == "__main__":
    main()