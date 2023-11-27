import math

print ("-------Ejercisios de Introduccion a Scripting-------")

print ("Ejercisios de tipos de datos:")

def Ejers1Operation(nom1,nom2,dem1,dem2):
    result1 = (nom1 + nom2) / (dem1 * dem2)
    result2 = result1 * result1
    return result2

print ("Ejercisio 1 ----------")
Pinput1 = 3
Pinput2 = 2

Pinput3 = 2
Pinput4 = 5

print (Ejers1Operation(Pinput1, Pinput2, Pinput3, Pinput4))

def Ejers2HourCalcul(hourAmount, hourValue):
    result = hourAmount * hourValue
    returnValue = result
    return returnValue

print ("Ejercisio 2 ----------")

print ("Vamos a calcular que tanto gano el dia de hoy")

Pinput1 = input("Cuantas horas trabajo? ")
Pinput2 = input("Cuanto vale la hora? ")
res = Ejers2HourCalcul(int(Pinput1),int(Pinput2))

print ("Este dia merece de paga", res ,"pesos")

def Ejers3Adding(numGoal):
    result = (numGoal * (numGoal + 1)) / 2
    return result

print ("Ejercisio 3 ----------")

print ("Vamos a hacer una suma desde 1 hasta que el numero que me indique")
Pinput1 = input("Escriba el numero para empezar a sumar hasta el ")

res = Ejers3Adding(int(Pinput1))
print ("El numero final fue: ", res)

def Ejers4Juguete(pay,muni):
    peso1 = pay * 112
    peso2 = muni * 75
    suma = peso1 + peso2
    return suma

print ("Ejercisio 4 ----------")

print ("Tenemos que checar el siguiente paquete de la jugueteria")

Pinput1 = input("Cuantos payasos pidieron? ")
Pinput2 = input("Cuantas muniecas pidieron? ")

res = Ejers4Juguete(int(Pinput1), int(Pinput2))

print ("El peso del paquete sera ", res)

def Ejers5Ruleof3(quantity):
    value1 = quantity
    value2 = 4
    resultOperation = (quantity * value2) / 100
    result = quantity - resultOperation
    return result

print ("Ejercisio 5 ----------")

print ("Bienvenido al banco, cuanto dinero quiere depositar en su nueva cuenta de ahorros?")
print ("Va a haber un interes al anio, se le informara cual sera la cantidad de dinero en siguientes anios")
Pinput1 = input(": ")

val1 = Ejers5Ruleof3(int(Pinput1))
val2 = Ejers5Ruleof3(val1)
val3 = Ejers5Ruleof3(val2)

print ("ahorros el primer anio: ", val1)
print ("ahorros el segundo anio: ", val2)
print ("ahorros el tercer anio: ", val3)

print ("Ejercisios Strings:")

print ("Ejercisio 1 ----------")

Pinput1 = input("Escriba su nombre: ")
val2 = 0

val1 = Pinput1.upper()
for x in val1:
    val2 += 1

print (val1, "Tiene ", val2, "letras")

print ("Ejercisio 2 ----------")

print ("Escriba la lista de objetos que le robo a su tio, digo que tiene de compras")
print ("Separe los elementos por comas, los espacios seran eliminados asi que de preferencia utilice una palabra por elemento")
Pinput1 = input (": ")

Pinput1 = Pinput1.replace(" ","")

Plist1 = {}
Plist1 = Pinput1.split(",")

for x in range(len(Plist1)):
    print (Plist1[x])
    
print ("Ejercisios de condicionales:")

print ("Ejercisio 1 ----------")

print ("Dame tu edad")

Pinput1 = input ("Edad: ")

Pinput1 = int(Pinput1)

if Pinput1 >= 18:
    print ("eres mayor de edad")
else:
    print ("eres menor de edad")

print ("Ejercisio 2 ----------")

print ("Hola soy un hacker, la contrasenia disponible es 'caca'")
Pinput1 = input ("Deme la contrasenia pa ingresar al gobierno papu: ")

Pinput1 = Pinput1.replace(" ","")
Pinput1 = Pinput1.lower

if (Pinput1 == "caca"):
    print ("Accedistes al gobernio de los papus")
else:
    print ("No accedistes, eres malvado y te vamos a matar maniana")
    
print ("Ejercisio 3 ----------")

Pinput = input("Ingresa un numero para saber si es par o impar: ")

Pinput = int(Pinput)

val1 = Pinput/2
val2 = int(val1)

if val1 == val2:
    print ("Tu numero es par")
else:
    print ("Tu numero no es par")
    
print ("Ejercisio 4 ----------")

print ("Bienvenido a empresa los chamacos peludos")

Pinput1 = input("Ingrese su puntuacion final: del 0.0 al 1.0: ")

val1 = float(Pinput1)

if val1 < 0.4:
    print ("Tu rendimiento fue inaceptable, eres una deshonrra")
elif val1 < 0.6:
    print ("Tu rendimiento fue aceptable, eres una gran herramienta para la compania")
else:
    print ("Tu rendimiento fue exepcional, eres de confianza")
    
val2 = (2400 * val1)

print ("Tu paga final sera de: ", val2, "pesos")

print ("Ejercisio 5 ----------")

print ("Bienvenido al local: juegos pedorros")

Pinput1 = input("Ingrese su edad para poder jugar: ")

val1 = int(Pinput1)

if val1 < 4:
    print ("felicidades, usted entra gratis")
elif val1 > 4 and val1 < 18:
    print ("Serian 50 pesos para la entrada")
else:
    print ("Serian 10 pesos para la entrada")
    
def addingredient(stringIng):
    canIng = False
    print ("Le gustaria que su pizza tubiera", stringIng, "?")
    Pinpt = input ("escriba 'si' o 'no' ")
    if Pinpt == "si":
        canIng = True
    return canIng

print ("Ejercisio 6 ----------")

print ("Oui bienvenidos a la pizzeria Bella Napoli")
print ("Vendemos pizzas vegetarianas y no vegetarianas:")
print ("Cualquier ingrediente puede ser removido si gusta")

print ("-- Pizza Vegetariana: Pimiento y Tofu --")
print ("-- Pizza Normal: Peperoni, Jamon, Salmon --")

Pinput1 = input("Que pizza elegira: escriba 'v' para la vegetariana y 'n' para la normal ")

ing1 = False
ing2 = False
ing3 = False

if Pinput1 == "v":
    ing1 = addingredient("Peperoni")
    ing2 = addingredient("Jamon")
    ing3 = addingredient("Salmon")
    print ("Tu pizza tiene los siguientes ingredientes")
    print ("Queso")
    if ing1 == True:
        print ("Peperoni")
    if ing2 == True:
        print ("Jamon")
    if ing3 == True:
        print ("Salmon")
    print ("Estara lista en unos minutos")
elif Pinput1 == "n":
    ing1 = addingredient("Pimineto")
    ing2 = addingredient("Tofu")
    print ("Tu pizza tiene los siguientes ingredientes")
    print ("Queso")
    if ing1 == True:
        print ("Pimineto")
    if ing2 == True:
        print ("Tofu")
    print ("Estara lista en unos minutos")
    
print ("Finalizacion de Ejercisios ----------")

print ("Inicio de Ejercisios bucles ----------")

print ("Ejercisio 1 ----------")

Pinput = input ("Dame tu nombre, extranio, para ver si es divertido :: ")

for x in range(10):
    print (Pinput)
    
print ("jaja, si es divertido")

print ("Ejercisio 2 ----------")

print ("Ok extranio, vamos a contar en reversa hasta llegar al 0, dame un numero entero")

Pinput = input(":: ")

var1 = int(Pinput)

for x in range(var1,0,-1):
    print (x)
    
print ("Que divertido!")

print ("Ejercisio 3 ----------")

input ("Te voy a mostrar las tablas de multiplicar mas poderosas, estas listo?")

for x in range(1,10,1):
    print ("")
    for y in range(1,10,1):
        print (x * y , end=" - ")
       
print ("")
print ("Me quedo chido verdad?")

print ("Ejercisio 4 y 5 supongo ----------")

print ("Hola usuario, soy el muro de fuego que protege al sistema de diversion automatizada")
print ("Solo lo puedo dejar jugar si usted ingresa la contrasenia correcta: ")

print (" << Hola, soy el hacker de nuevo, la contrasenia es 'nosleep'")

var1 = False
var2 = 0
Plist1 = {}
Plist1[0] = 'n'
Plist1[1] = 'o'
Plist1[2] = 's'
Plist1[3] = 'l'
Plist1[4] = 'e'
Plist1[5] = 'e'
Plist1[6] = 'p'
Plist2 = {}

while var1 == False:
    Pinput = input("Contrasenia: ")
    for x in Pinput:
        # Tambien podria utilizar append pero queria ver otros metodos
        Plist2[var2] = x
        var2 += 1
        
    var2 = 0
    print (Plist1)
    print (Plist2)
    if Plist2 == Plist1:
        print ("Contrasenia correcta")
        var1 = True
    else:
        print ("Contrasenia incorrecta")
        Plist2 = {}
        
print ("Puede continuar con su programa")

print ("Ejercisio 6 ----------")

var1 = 0
print ("Vamos a seguir jugando amigo, dime una frase que te guste")
Pinput1 = input(":: ")
print ("Ahora dame tu letra favorita")
Pinput2 = input(":: ")

Plist1 = []
for x in Pinput1:
    if x == Pinput2:
        var1 += 1
        
print ("Sabias que la cantidad de veces que se repite tu letra favorita en esa frase es", var1, "veces?")

print ("Ejercisio 7 ----------")

print ("Ok, ahora dame toda la informacion que se te plazca la guardare hasta que me digas 'Salir' ahi terminara nuestra diversion :(")
var1 = False
Plist1 = []

while var1 == False:
    Pinput = input (":: ")
    if Pinput == "Salir":
        var1 = True
        continue
    Plist1.append(Pinput)
    print (Plist1)
    
print ("Hasta luego amigo, te extraniare")

print ("Finalizacion de Ejercisios bucles ----------")

print ("Finalizacion del programa ----------")