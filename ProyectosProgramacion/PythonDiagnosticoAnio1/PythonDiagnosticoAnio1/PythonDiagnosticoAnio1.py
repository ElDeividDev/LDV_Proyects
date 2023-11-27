import math

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
        print ("Tu palabra es un palindromo")
        return 
    else:
        print ("Tu palabra no es un palindromo")
        return
    
def masacorporal(myWeight,myHeight):
    heightSquared = float(myHeight) * float(myHeight)
    corpMass = float(myWeight) / heightSquared
    return corpMass
    
def checarNombreAGrupo(inputName,inputSex):
    isGroupA = False
    # Si es menor o igual a m en posicion del alfabeto
    if ord(inputName) - ord('a') + 1 <= 13:
        if inputSex == "m":
            isGroupA = True
    elif ord(inputName) - ord('a') + 1 > 13:
        if inputSex == "h":
            isGroupA = True
        
    if isGroupA == True:
        return "Felicidades, eres parte del grupo A"
    else:
        return "Que lastima, eres parte del grupo B"
    
def fibonachi(pNum):
    num1F = 0
    num2F = 1
    print (num1F)
    print (num2F)
    currentResult = 0
    while currentResult <= pNum:
        currentResult = num1F + num2F
        print (currentResult)
        num1F = num2F
        num2F = currentResult
    return "Gracias, llegamos al numero ", currentResult, "Para poder llegar a ", pNum

def parimpar(myNumberGoal):
    print ("Primero con numeros pares")
    evenNum = 2
    print (evenNum)
    while evenNum < myNumberGoal:
        evenNum += 2
        print (evenNum)
    print ("Ahora con numeros impares")
    oddNum = 1
    print (oddNum)
    while oddNum < myNumberGoal:
        oddNum += 2
        print (oddNum)
        
def funcionTriangular(myNumberGoal):
    currentNum = 1

    while myNumberGoal > currentNum:
        for x in range(currentNum):
            print ("*",end="")
        print ("")
        currentNum += 1

def ABCespecial(abc):
    i = 3
    while i <= len(abc):
        del abc[i - 1]
        i += 2 
    print (abc)
    
def imprimirdatosdelista(lista):
    print (lista)
    
def datosindividuo():
    dataList = []
    requirmentsList = []
    requirmentsList[0] = "Proporcione su nombre por favor"
    requirmentsList[1] = "Proporcione su edad por favor"
    requirmentsList[2] = "Proporcione su sexualidad por favor"
    requirmentsList[3] = "Proporcione su numero de telefono por favor"
    requirmentsList[4] = "Proporcione su correo electronico por favor"
    requirmentsList[5] = "Proporcione su tipo de sangre por favor"
    for x in range(5):
        pInput = input(requirmentsList[x])
        dataList.append(pInput)
        imprimirdatosdelista(dataList)
    print ("Gracias, ahora que tenemos su informacion puede sacrificar su alma a satanas y por fin pertenecer a la sociedad")

print ("Ejercisio 1 ----------------------")

print ("Hola usuario, bienvenido a este programa")
print ("Porfavor proporcione su peso en kg y altura en metros")

pInput1 = input ("Peso: ")
pInput2 = input ("Altura: ")
result = masacorporal(pInput1,pInput2)
print ("Tu indice de masa corporal es ", result)


print ("Ejercisio 2 ---------------------")

print ("Hola alumno, bienvenido a la escuela, se le proporcionara un grupo")
print ("Para estar en el mejor grupo de todos, el A, El grupo A esta formado por las mujeres con un nombre anterior a la M y")
print ("los hombres con un nombre posterior a la N")

pInput1 = input("Escriba la primer letra de su nombre: ")
pInput1 = pInput1.lower()
print (pInput1)
pInput2 = input("Escriba su sexualidad con M o H: ")
pInput2 = pInput2.lower()
print (pInput2)
result = checarNombreAGrupo(pInput1,pInput1)
print (result)


print ("Ejercisio 3 ---------------------")

print ("Por favor escriba un numero entero, vamos a llegar a este por la serie fibonacci")
pInput1 = input ("Num: ")
pInput1 = int(pInput1)
result = fibonachi(pInput1)
print (result)

print ("Ejercisio 4 ---------------------")

print ("Por favor escriba un numero entero, vamos a llegar a este por numeros pares y luego impares")
pInput1 = input ("Num: ")
pInput1 = int(pInput1)
parimpar(pInput1)

print ("Ejercisio 5 ---------------------")

print ("Por favor escriba un numero entero, vamos a dibujar un triangulo y el numero sera la base de este")
pInput1 = input ("Num: ")
pInput1 = int(pInput1)
funcionTriangular(pInput1)

print ("Ejercisio 6 --------------------")

print ("Voy a escribir el abecedario sin las posiciones de multiplos de 3")
print ("No escribas nada, lo voy a hacer solito")

abecedario = list("abcdefghijklmnopqrstuvwxyz")
ABCespecial(abecedario)

print ("Ejercisio 7 --------------------")

print ("Por favor escriba un a frase o palabra para identificar si esta es un palindromo o no")
pInput1 = input ("Oracion: ")
polindromoFunction(pInput1)

print ("Ejercisio 8 --------------------")

print ("Bienvenido a la base de datos globalizada")
datosindividuo()


