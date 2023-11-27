import math

# len te da la longitud de una lista

# for x in range (len(word)): word[x]

# .lower() va a trasnformar mayusculas a minusculas
# .upper() lo opuesto a lower, transforma minusculas a mayusculas
# .replace() va a buscar lo que pidas y la reemplaza por lo que pidas
# .replace(original, new)

print ("Ejercisio 1 --------------------------")

_inputPyr = input("Dame una palabra para saber si es un palindromo: ")

letters = {}

size = 0

_inputPyr = _inputPyr.lower()
_inputPyr = _inputPyr.replace(" ","")
_inputPyr = _inputPyr.replace(".","")
_inputPyr = _inputPyr.replace(",","")

# Necesitamos saber cuantas letras hay en la palabra
# Y cuales son estas palabras

# Checa la cantidad de palabras y además 
for x in _inputPyr:
    print (x)
    size += 1
    letters[size] = x

print (letters)
print (size)
halfSize = size/2
print (halfSize)

# Checa si tiene decimales para ignorar el caracter central
if halfSize != int(halfSize):
    print ("Jaja tiene decimales")
    numIgnor = math.ceil(halfSize)
    print (numIgnor)
else: 
    numIgnor = -1 # Num Ignor es ignorado
    

firstHalf = ""
secondHalf = ""

adder = 0

for x in range(int(halfSize)):
    adder += 1
    if x == numIgnor - 1:
        continue
    firstHalf += letters[adder]
    secondHalf += letters[size - adder +1]


if firstHalf == secondHalf:
    print ("Si es Pangamandapio, digo palindromo")
else:
    print ("No es palindromo")
    
print ("La cantidad de letras que tiene tu palabra es: " ,size)

print (firstHalf)
print (secondHalf)


print ("Ejercisio 2 ------------------------")

# cuando un for o while no es interrumpido con un "break" entonces accede al else si existe

for x in range(3):
    print ("Hola")
    if x == 5:
        break
else:
    print ("Queso")
    
# .split("a") Esta funcion separa un string en multiples strings donde separa el string por cada vez que encuentre "a" o cualquier cosa dentro de split
# .join Lo contrario de split, sirve para juntar cosas en la lista en un string, lo que existe en la variable y por cada union de la variable estara juntado por esta
# list = {hel,oue,uwu} : var = POP : var.join(list) ::  var now is = helPOPouePOPuwu

var = "alavanza al senior"

myVarList = var.split("a")

print (myVarList)
    
# -----------------------

var2 = " "

myVarList2 = {"harry","no","sabe","maguia"}

myJoinList = var2.join(myVarList2)

print (myJoinList)
