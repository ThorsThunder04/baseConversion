

# exercice 6
def binToDec(binNumLst):
    lenCount = -1 # -1 car on veut la longeur -1 pour calculer le decimal
    for i in binNumLst: # enregistre la longeur du list
        lenCount += 1
    
    resultNum = 0
    for num in binNumLst: # calcule le decimal
        resultNum += num*2**lenCount
        lenCount -= 1
    
    return resultNum # retourne le resultat

#print(binToDec([1,1,0,1])) # -> 13


# exercice 7
def decToBinLst(num):
    binary = []
    tempQuotient = num # nombre qui sera divisé au prochain tour

    while (tempQuotient != 0): # calculation du mot binair
        binary += [tempQuotient % 2]
        tempQuotient = tempQuotient // 2

    binary.reverse()
    return binary

# print(decToBinLst(123)) # -> [1, 1, 1, 1, 0, 1, 1]


# exercice 8
def decToBinStr(num):
    binary = ""
    tempQuotient = num # nombre qui sera divisé au prochain tour

    while (tempQuotient != 0): # calculation du mot binair
        binary += str(tempQuotient % 2)
        tempQuotient = tempQuotient // 2

    binary = list(binary)
    binary.reverse()
    return ''.join(binary) 

# print(decToBinStr(420)) # -> 110100100


# exercice 9
def octToBin(octNum):
    lenCount = -1
    for i in str(octNum): # enregistre la longeur du nombre octal
        lenCount += 1
    

    numberLst = [i for i in range(10)]
    strNumberLst = [str(i) for i in range(10)]

    base8Dec = 0
    for num in str(octNum): # transforme du base8 en decimal

        for index in range(10): # pour utiliser le nombre sans utiliser int()
            if (num == strNumberLst[index]):
                base8Dec += numberLst[index]*8**lenCount
                lenCount -= 1

    # le calcule du base2 peut etre fait avec decToBinStr(base8Dec)
    base8Binary = ""
    tempQuotient = base8Dec # nombre qui sera divisé au prochain tour

    while (tempQuotient != 0): # calculation du mot binair
        base8Binary += str(tempQuotient % 2)
        tempQuotient = tempQuotient // 2

    base8Binary = list(base8Binary)
    base8Binary.reverse()
    return ''.join(base8Binary)
    

# print(octToBin(32)) # -> 11010


# exercice 10
def hexToBin(hexVal): # suposent que la valeur est un string
    hexLen = -1
    for i in hexVal: # enregistre la longeur du valeur hexadecimal
        hexLen += 1
    
    hexLetterNum = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15} # contient les valeurs des lettres base16

    numberLst = [i for i in range(10)]
    strNumberLst = [str(i) for i in range(10)]

    base16Dec = 0 
    for value in hexVal: # transforme le base16 en decimal
        if (value in strNumberLst):
            for index in range(10): # pour utiliser le nombre sans utiliser int()
                if (value == strNumberLst[index]):
                    base16Dec += numberLst[index]*16**hexLen
                    hexLen -= 1
                            
        elif value.lower() in hexLetterNum: # calcule le decimal du lettre
            base16Dec += hexLetterNum[value.lower()]*16**hexLen
            hexLen -= 1
    
    # le calcule du base2 peut aussi etre fait avec decToBinStr(base16Dec)
    base16Binary = ""
    tempQuotient = base16Dec # nombre qui sera divisé au prochain tour

    while (tempQuotient != 0): # calculation du mot binaire
        base16Binary += str(tempQuotient % 2)
        tempQuotient = tempQuotient // 2

    base16Binary = list(base16Binary)
    base16Binary.reverse()
    return ''.join(base16Binary)


# print(hexToBin('8f')) # -> 10001111

