
# Calculadora de David Alejandro Esponda Ochoa

Pinpt = ""
operationType = 0
val1 = 0
val2 = 0
res = 0
closeProgram = False

def Calculate(_value1,_value2,_type):
    res = 0
    if _type == 0: # Suma
        res = _value1 + _value2
    elif _type == 1: # Resta
        res = _value1 - _value2
    elif _type == 2: # Multiplicacion
        res = _value1 * _value2
    elif _type == 3: # Division
        try:
            res = _value1 / _value2
        except :
            res = "Sintax Error"
    elif _type == 4: # Potencia
        try:
            res = _value1 ** _value2
        except :
            res = "Sintax Error"
    elif _type == 5: # Raiz
        try:
            _value2 = 1 / _value2
        except :
            _value2 = 0
        try:
            res = _value1 ** _value2
        except :
            res = "Sintax Error"
    
    return res

def CheckVarType(myVar):
    isValid = False
    if myVar.isalnum() == True:
        if myVar.isalpha() == True:
            isValid = False
        elif myVar.isnumeric() == True:
            isValid = True

    return isValid

def SimplifyVarValue(myVar):
    myVar = myVar.replace(" ","")
    myVar = myVar.replace(",","")
    myVar = myVar.replace(".","")
    myVar = myVar.lower()
    return (myVar)

def VerifyInput(myVar):
    canBeUsed = False
    myVar = SimplifyVarValue(myVar)
    if CheckVarType(myVar) == True:
        canBeUsed = True
    else:
        print (" - Su valor no es correcto, checa la ortografia o el uso de caracteres - ")
    return canBeUsed
        

# Introduccion
print (" --- Bienvenido a la mejor calculadora del mundo ---")
print (" - Aqui puedes hacer operaciones con dos numeros -")


while True:
    while True:
        print (" - Para hacer operaciones esriba; 0:Suma, 1:Resta, 2:Multiplicacion, 3:Division, 4:Potencia, 5:Raiz -")
        print (" - Escribe 'Exit' para salir de la calculadora -")
        Pinpt = input (" :: ")
        Pinpt = SimplifyVarValue(Pinpt)
        if Pinpt == "exit":
            closeProgram = True
            break
        if VerifyInput(Pinpt) == True:
            Pinpt = int(Pinpt) # Valor se vuelve numerico
            if Pinpt < 6 and Pinpt > -1:
                print(" - Valor Valido - ")
            else:
                print(" - Escriba un numero entero dentro del rango permitido")
                continue
            operationType = Pinpt # Se iguala al tipo de operacion
            break
    if closeProgram == True:
        break
    while True:
        print (" - Escriba el PRIMER numero de su operacion")
        Pinpt = input (" :: ")
        if VerifyInput(Pinpt) == True:
            Pinpt = float(Pinpt) # Valor se vuelve numerico
            val1 = Pinpt # Se iguala al tipo de operacion
            break
    while True:
        print (" - Escriba el SEGUNDO numero de su operacion")
        Pinpt = input (" :: ")
        if VerifyInput(Pinpt) == True:
            Pinpt = float(Pinpt) # Valor se vuelve numerico
            val2 = Pinpt # Se iguala al tipo de operacion
            break
    res = Calculate(val1,val2,operationType)
    print (" - Su respuesta es:", res, "--")
    

print (" --- Gracias por utilizar la calculadora, hasta luego :) --- ")
        