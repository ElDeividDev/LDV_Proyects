myMatrix = [[2,3,4],[5,6,7],[8,9,42069]]

print ("---------- Ejercisio Imprimir matrix 1 -----------")

var1 = 0
var2 = 0
res = 0
for x in range(0,9,1):
    res = myMatrix[0][0] * myMatrix[var1][var2]
    print (myMatrix[0][0], " * ", myMatrix[var1][var2], " = ", res)
    var1 = var1 + 1
    if (var1 >= 3):
        var1 = 0
        var2 = var2 + 1
    
input("")
print ("---------- Ejercisio Imprimir matrix 2 -----------")

for x in range(0,3,1):
    for y in range (0,3,1):
        res = myMatrix[0][0] * myMatrix[x][y]
        print (myMatrix[0][0], " * ", myMatrix[x][y], " = ", res)

input("") 
print ("---------- Ejercisio Imprimir matrix 3 -----------")

print (myMatrix[0][0], " * ", myMatrix[0][0], " = ", myMatrix[0][0] * myMatrix[0][0])
print (myMatrix[0][0], " * ", myMatrix[1][0], " = ", myMatrix[0][0] * myMatrix[1][0])
print (myMatrix[0][0], " * ", myMatrix[2][0], " = ", myMatrix[0][0] * myMatrix[2][0])
print (myMatrix[0][0], " * ", myMatrix[0][1], " = ", myMatrix[0][0] * myMatrix[0][1])
print (myMatrix[0][0], " * ", myMatrix[1][1], " = ", myMatrix[0][0] * myMatrix[1][1])
print (myMatrix[0][0], " * ", myMatrix[2][1], " = ", myMatrix[0][0] * myMatrix[2][1])
print (myMatrix[0][0], " * ", myMatrix[0][2], " = ", myMatrix[0][0] * myMatrix[0][2])
print (myMatrix[0][0], " * ", myMatrix[1][2], " = ", myMatrix[0][0] * myMatrix[1][2])
print (myMatrix[0][0], " * ", myMatrix[2][2], " = ", myMatrix[0][0] * myMatrix[2][2])