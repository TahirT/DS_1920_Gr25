

#NE PROCES E TUTJE

import sys

print("Ju lutem vendosni njeren nga komanadat: uppercase, lowercase, capitalize, inverse, alternating")
fjalia = input("Ne fillim vendosni nje fjali te qfardoshme:")
print(fjalia)
komanda = input("Tani vendos njeren nga komandat e dhena me larte:")

argumentet = ["uppercase","lowercase","capitalize","inverse","alternating"]
if komanda in argumentet:
    print("Ke zgjedhur komanden " + komanda + " nga lista " + str(argumentet) + "\nRezultati: ")
else:
    print("Gabim ,ju lutem vendosni nje komande valide!")
if komanda == 'uppercase':
    print(fjalia.upper())
elif komanda == 'lowercase':
    print(fjalia.lower())
elif komanda == 'capitalize':
    print(fjalia.capitalize())
elif komanda == 'inverse':
    print(fjalia.swapcase())

elif komanda == 'alternating':

    def to_alternating_case(fjalia):
        res = ""
        i = 0
        for word in fjalia:
            i += 1
            if i % 2 == True:
                res = res + word.lower()
            else:
                res = res + word.upper()
        return res


    print(to_alternating_case(fjalia))

