import math

print ("Ejercisio 1 --------------------------")

_inputPyr = input("Dame una palabra para saber si es un palindromo: ")

letters = {}

size = 0
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
    

print (firstHalf)
print (secondHalf)