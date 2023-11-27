import math
from tokenize import group

# def [nombre](a,b,c): / def significa define
# return result / Tiene que regresar el tipo de funcion

#def supersuma(a,b):
#    result = a + b
#    return result

#print (supersuma(10,20))

def Introduction():
    print ("Escribe 'End' si quieres terminar")
    print ("Escribe 'Pal' si quieres saber si una palabra es un polinomio")
    print ("Escribe 'Fac' si quieres saber el factorial de un numero")
    
def myInput():
    data = input(":: ")
    return data

def simplifyMyWord(word):
    word = word.lower()
    word = word.replace(" ","")
    word = word.replace(".","")
    word = word.replace(",","")
    return word

def defineHowManyWords(word):
    group = {}
    group = word.split(" ")
    return len(group)
    

def polindromoFunction(_inputPyr):
    letters = {}
    size = 0
    wordsQuantity = defineHowManyWords(_inputPyr)
    print ("La cantidad de palabras que tiene tu oracion es: ", wordsQuantity)
    _inputPyr = simplifyMyWord(_inputPyr)
    firstHalf = ""
    secondHalf = ""
    adder = 0
    for x in _inputPyr:
        size += 1
        letters[size] = x

    halfSize = size/2

    # Checa si tiene decimales para ignorar el caracter central
    if halfSize != int(halfSize):
        numIgnor = math.ceil(halfSize)
    else: 
        numIgnor = -1 # Num Ignor es ignorado
    
    for x in range(int(halfSize)):
        adder += 1
        if x == numIgnor - 1:
            continue
        firstHalf += letters[adder]
        secondHalf += letters[size - adder +1]

    print ("La cantidad de letras que tiene tu oracion es: " ,size)

    if firstHalf == secondHalf:
        return True
    else:
        return False
    
def factorialFunction(myNum):
    while myNum.isalpha() == True:
        myNum = input("Escribe un numero para darte el factor: ")

    myNumber = int(myNum)

    result = 1

    for x in range(myNumber,0,-1):
        result *= x

    return result
    
pyrInput = ""
polInput = ""
isPol = False
facInput = ""
facNum = 0
endProgram = False

print ("Ejercisio 1 ----------------------------")

print ("Hola buenas tardes, bienvenido al mejor programa del mundo")

while endProgram == False:
    Introduction()
    pyrInput = myInput()
    pyrInput = simplifyMyWord(pyrInput)
    
    if pyrInput == "end":
        break
    elif pyrInput == "pal":
        print ("Escriba la palabra que quiera checar si es un palindromo o no")
        polInput = myInput()
        isPol = polindromoFunction(polInput)
        if isPol:
            print ("Tu oracion fue un palindromo")
        else:
            print ("Tu oracion no fue un palindromo")
        
    elif pyrInput == "fac":
        print ("Escriba el numero que quiera factorializar")
        facInput = myInput()
        facNum = factorialFunction(facInput)
        print ("el factorial de " ,facInput , " fue ", facNum)
    else:
        print ("El valor agregado no aplica, cheque la ortografia")
        
    
print ("gracias por utilizarme, hasta luego :)")
    