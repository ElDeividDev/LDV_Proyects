var = "30"
var2 = "-10"

varInt = int(var) - int(var2) # Para sumar numeros si son strings de numeros

print (varInt)

# Ejercisio 1
print ("Ejercisio 1 ----------------------")

var3 = input("Escribe algo: ")

var3.isalpha() # Determina si la variable string es de letras

var3.isnumeric() # Determina si la variable string es de numeros

if var3.isnumeric():
    print ("Tu escrito son numeros")
    print ("Escribiste el numero: ", end = "")
    print ("'",var3,"'")
else:
    print ("Tu escrito no son numeros")
if var3.isalpha():
    print ("Tu escrito son letras")
    print ("Escribiste la palabra: ", end = "")
    print ("'",var3,"'")
    if var3 == "pito":
        print ("por cierto, no sea grosero")
else:
    print ("Tu escrito no son letras")
    
# Ejersicio 2
print ("Ejercisio 2 ----------------------")

num1 = input("Escribe un numero entero: ")
num2 = input("Escribe otro numero entero: ")
result = 0


if num1.isnumeric():
    if num2.isnumeric():
        result = int(num1) + int(num2)
        print ("La suma de tus nos numeros es ", result)
    else:
        print ("El segundo numero '", num2, "' no es un numero, me enganiaste tonto")
else:
    print ("El primer numero '", num1, "' no es un numero, me enganiaste tonto")

# Bucle
print ("Ejercisio 3 Tarea ----------------------")


userData = input ("Escribe un numero para sumar o escriba 'Stop' para detenerse: ")

savedData = 0;
while userData != "Stop":
    if userData.isnumeric():
       print("Tu numero actual es: ", int(userData) + int(savedData))
       savedData = int(userData) + int(savedData)
       print("--------------")
    else:
        print ("Eso no fue un numero")
    userData = input ("Escribe un numero para sumar o escriba 'Stop' para detenerse: ")
    
print ("Gracias por jugar, tu numero final fue: ", savedData)

resultado = 0
resultado += 1 # resultado = resultado + 1
# print (resultado)

# al utilizar un "Continue" en un While actua como un return, detiene todo el código e inicia desde el inicio
# al utilizar un Try con un Exception intenta todo en el try y si sale error entonces ejecuta todo dentro de Exception, si no entonces solo lo ignora y ejecuta todo lo de try
# al utilizar "Break" en un While es el romper con el While y continuar con lo que sigue despues del while
# "elif" es practicamente un "else if" transformado, es una estupidez pero así funciona en pyton