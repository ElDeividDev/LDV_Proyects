lista = []

data = ""

print ("Ejersicio 1 --------")

while data != "Stop":
    data = input("Escribe algo (escribe 'Stop' para parar) - ")
    if data == "Stop":
        break # Detener el while aqui
    print (data)
    lista.append(data)
print (lista)

print ("Ejersicio 2 --------")

# Programa que pida datos al usuario; estos pueden ser cualquier cosa
# Van a almacenar estos datos en categorías diferentes, si son palabras se organizan en una lista de numeros
# Si son numeros enteros en una lista de numeros, si son float, etc.

print ("Hola bienvenido al organizador automatico")
print ("Introduzca cualquier dato y se organizara automaticamente")
print ("Escriba 'Stop' para detener el programa")

nums = []
words = []
other = []

pInput = ""

while True:
    pInput = input("Dato: ")
    if pInput == "Stop":
        break # Detener el while aqui
    if pInput.isnumeric():
        print ("Tu dato fue numerico")
        nums.append(int(pInput))
    elif pInput.isalpha():
        print ("Tu dato fue una palabra")
        words.append(pInput)
    else:
        print ("Tu dato fue no definido")
        other.append(pInput)
        
print ("Estos fueron tus datos organizados: ")
print ("Datos numericos: ", nums)
print ("Palabras: ", words)
print ("Otros: ", other)

