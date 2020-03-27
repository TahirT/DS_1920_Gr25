def teDhenat():  # merr te dhenat nga perdoruesi

    vlera = input()

    data = []

    for char in vlera.upper():
        if char.isalpha():
            data.append(char)
    return ''.join(data)


def enncrypt(mesazhi, qelsi1, qelsi2):
    pass

def decrypt(Encr, qelsi1, qelsi2):
    pass

def main():
    print("**** Four Square Cipher *******\n")

    print("Vendos qelsin e Pare: ", end=' ')
    qelsi1 = teDhenat()

    print("\nVendos qelsin e Dyte: ", end=' ')
    qelsi2 = teDhenat()

    print("\nVendos Mesazhin per te Enkriptuar (A-Z):", end=' ')
    mesazhi = teDhenat()

    Encr = enncrypt(mesazhi, qelsi1, qelsi2)

    print (Encr)

    print ("\nVendos Mesazhin per te Dekriptuar (A- Z): ")

    Decr = decrypt(Encr,qelsi1,qelsi2)

    print (Decr)

if __name__ == "__main__":
    main()