#*********************************************Four Square Chiper************************************************************
alfabeti = ['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] 
#shkronja J


def teDhenat():  # merr te dhenat nga perdoruesi

    vlera = input()

    data = []

    for char in vlera.upper():
        if char.isalpha():
            data.append(char)
    return ''.join(data)
def MatricaK(qelsi): 
	
	matrica = []
	numruesi = 0
	alphaCount = 0
	
	if qelsi == '!':
		for char in alfabeti:
			matrica.append(char)
	else:
		for char in qelsi:
			matrica.append(char)
			numruesi += 1
		while (numruesi < 25):
			if alfabeti[alphaCount] not in qelsi:
				matrica.append(alfabeti[alphaCount])
				alphaCount += 1
				numruesi += 1
			else:
				alphaCount += 1
	
	return ''.join(matrica)

def shtypmatricen(matrica): 

	numruesi = 0
	for x in range(5):
		print("\n")
		for y in range(5):
			print (matrica[numruesi], end=' ')
			numruesi += 1
	print("\n\n")
			
	
	
def removeDuplicates(str): 
    rezultati=[]
    seen=set()
    for char in str:
        if char not in seen:
            seen.add(char)
            rezultati.append(char)
    return ''.join(rezultati)
	

	

def evaluate(ref1, ref2):	
	return ((int(ref1 / 5) * 5) + (ref2 % 5))

	
	
	
def kerko (ref, shkronja):
	numruesi = 0
	if shkronja == 'J':
		return -1
	for char in ref:
		if ref[numruesi] == shkronja:
			return numruesi
		numruesi += 1
	pass
	
	
	

	
	
	
#Encryption function


def encrypt(mesazhi, qelsi1, qelsi2):
    

	qelsi1 = removeDuplicates(qelsi1)
	matrica1 = MatricaK(qelsi1)
	
	
	qelsi2 = removeDuplicates(qelsi2)
	matrica2 = MatricaK(qelsi2)
	
	refmatrica = MatricaK('!')
	
	print ("*****qelsi 1 Block*****")
	shtypmatricen(matrica1)
	print ("*****qelsi 2 Block****")
	shtypmatricen(matrica2)
	print ("****Reference block*****")
	shtypmatricen(refmatrica)
	
	encrypted = []
	numruesi = 0
	
	set = []
	
	while (numruesi < len(mesazhi)):
		
		aPosition = kerko(refmatrica, mesazhi[numruesi])
		if numruesi != len(mesazhi)-1:
			bPosition = kerko(refmatrica, mesazhi[numruesi + 1])
		if mesazhi[numruesi] != 'J':
			set.append(matrica1[evaluate(aPosition,bPosition)])
		else:
			set.append('J')
		
		if numruesi == len(mesazhi) - 1:
			return ''.join(set)
		elif mesazhi[numruesi] != 'J':
			set.append(matrica2[evaluate(bPosition,aPosition)])
			#set.append(matrica1[evaluate(kerko(refmatrica,mesazhi[numruesi+1]),kerko(refmatrica,mesazhi[numruesi]))])
		else:
			set.append('J')
		
		numruesi += 2
		#encrypted.append(set)

	return ''.join(set)
	
	
# DECRYPTION function


def decrypt(mesazhi, qelsi1, qelsi2):
    

	qelsi1 = removeDuplicates(qelsi1)
	matrica1 = MatricaK(qelsi1)
	
	
	qelsi2 = removeDuplicates(qelsi2)
	matrica2 = MatricaK(qelsi2)
	
	refmatrica = MatricaK('!')
	
	#print ("*****qelsi 1 Block*****")
	#shtypmatricen(matrica1)
	#print ("*****qelsi 2 Block****")
	#shtypmatricen(matrica2)
	#print ("****Reference block*****")
	#shtypmatricen(refmatrica)
	
	#encrypted = []
	numruesi = 0
	
	set = []
	
	while (numruesi < len(mesazhi)):
		
		aPosition = kerko(matrica1, mesazhi[numruesi])
		if numruesi != len(mesazhi)-1:
			bPosition = kerko(matrica2, mesazhi[numruesi + 1])
		
		if mesazhi[numruesi] != 'J':
			set.append(refmatrica[evaluate(aPosition,bPosition)])
		else:
			set.append('J')
		

		if numruesi == len(mesazhi) - 1:
			return ''.join(set)
		elif mesazhi[numruesi] != 'J':
			set.append(refmatrica[evaluate(bPosition,aPosition)])
			#set.append(matrica1[evaluate(kerko(refmatrica,mesazhi[numruesi+1]),kerko(refmatrica,mesazhi[numruesi]))])
		else:
			set.append('J')
		
		numruesi += 2
		#encrypted.append(set)

	return ''.join(set)
#main function
def main():
    print("**** Four Square Cipher *******\n")

    print("Vendos qelsin e Pare: ", end=' ')
    qelsi1 = teDhenat()

    print("\nVendos qelsin e Dyte: ", end=' ')
    qelsi2 = teDhenat()

    print("\nVendos Mesazhin per te Enkriptuar (A-Z):", end=' ')
    mesazhi = teDhenat()

    Encr = encrypt(mesazhi, qelsi1, qelsi2)
    
    print ("\nMesazhi i Enkriptuar: ")
    print (Encr)

    print ("\nMesazhi i Dekriptuar ")

    Decr = decrypt(Encr,qelsi1,qelsi2)

    print (Decr)

if __name__ == "__main__":
    main()
