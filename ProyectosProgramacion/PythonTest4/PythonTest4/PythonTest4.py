#A = [0,0]

#for x in A:
    #print ("Hehe")

#for x in range(3):
    #print ("Hoho")
    
# range (int)
# range (start, end, add)

# Range que empiece en 6 y termina en 50 llendo de 2 en 2
# range (6,50,2)

# Numero factorial : 25! = 25*24*23*22*21... etc.

# Ejercisio1 Sacar el numero factorial del numero que fue introducido

print ("Ejercisio1 -----------")
_pInput = input("Escribe un numero para darte el factor: ")

while _pInput.isalpha() == True:
    _pInput = input("PORFAVOR Escribe un numero para darte el factor: ")

print ("Ok gracias")

myNum = int(_pInput)

result = 1

for x in range(myNum,0,-1):
    result *= x
    print ("Vamos a multiplicar el numero por: ", x)
    print ("El numero actual es: ", result)
    
print ("Gracias por jugar, el factor de ", _pInput, " fue: ", result)
