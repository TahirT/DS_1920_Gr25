

#NE PROCES E TUTJE

import sys
def main():
    print("Ju lutem vendosni njeren nga komanadat: uppercase, lowercase, capitalize, inverse, alternating")
    fjalia = input("Ne fillim vendosni nje fjali te qfardoshme:")
    print(fjalia)
    x = input("Tani vendos njeren nga komandat e dhena me larte:")
    komanda = x.upper()
    argumentet = ["UPPERCASE","LOWERCASE","CAPITALIZE","INVERSE","ALTERNATING"]
    if komanda in argumentet:
        print("Ke zgjedhur komanden " + komanda + " nga lista " + str(argumentet) + "\nRezultati: ")
    else:
        print("Gabim ,ju lutem vendosni nje komande valide!")
        main()
    if komanda == 'UPPERCASE':
        print(fjalia.upper())
    elif komanda == 'LOWERCASE':
        print(fjalia.lower())
    elif komanda == 'CAPITALIZE':
        print(fjalia.capitalize())
    elif komanda == 'INVERSE':
        print(fjalia.swapcase())

    elif komanda == 'ALTERNATING':

        def alternating_case(fjalia):
            res = ""
            i = 0
            for word in fjalia:
                i += 1
                if i % 2 == True:
                    res = res + word.lower()
                else:
                    res = res + word.upper()
            return res


        print(alternating_case(fjalia))


if __name__ == '__main__':
    main()
