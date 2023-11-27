import random

matOfBools = [[False, False],[False, False]]

randomRow = random.choice(matOfBools)
randomBool = random.choice(randomRow)

row_index = matOfBools.index(randomRow)
colindex = randomRow.index(randomBool)

matOfBools[row_index][colindex] = True

print ("De 4 elementos en 2 listas uno de ellos acaba de transformarse en verdadero, cual es?")

print ("- * * -")
print ("- * * -")

resRow = input ("Escribe la lista del elemento que crees que cambio, la lista 1 o la 2 :: ")
resBool = input ("Escribe el elemento que crees que cambio, el 1 o el 2 :: ")

resRow = int(resRow)
resRow = resRow - 1

resBool = int(resBool)
resBool = resBool - 1

if matOfBools[resRow][resBool]:
    print ("Felicidades, adivinaste el correcto")
else:
    print ("Lastima, no le atinaste al correcto")
    
print (matOfBools[0])
print (matOfBools[1])