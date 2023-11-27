import random

P_Statements = [
    "abracadabra",
    "ganso",
    "hipopotomonstrosesquipedaliofobia",
    "esternocleidomastoideo",
    "tu",
    "creeper",
    "oscar"
    ]

# Elige una palabra aleatoria de la lista de Statements
myStatemnt = random.choice(P_Statements) 

myGuessStatement = [] # La lista de chars de intentos

for x in myStatemnt:
    myGuessStatement.append("_")

PTryAmount = 7 # La cantidad de intentos
PInpt = "" # El input del jugador
isSolved = False # Checa si esta resuelto o no
PPassTest = False # Si la palabra que eligio existia en el enunciado

print ("--- Inicio del programa ---")

print ("Bienvenido al ahorcado, tienes 7 intentos para adivinar el enunciado antes de ser ahorcado")

# Bucle de juego
while True:
    # Imprime la palabra y espera al input del jugador
    print (myGuessStatement)
    print ("Te quedan", PTryAmount, "Intentos, adivina poniendo una letra :: ")
    PInpt = input()
    # Encontrar todas las veces que esa letra aparece en la frase
    i = 0
    for x in myStatemnt:
        if x == PInpt:
            myGuessStatement[i] = PInpt
            PPassTest = True
        i += 1
    if PPassTest == True:
        PPassTest = False
    else:
        PTryAmount -= 1
    # Checar si esta resuelta la palabra
    isSolved = True
    for x in myGuessStatement:
        if x == "_":
            isSolved = False
            break
    # Si se resolvio entonces celebrar victoria y salir del bucle
    if isSolved or PTryAmount <= 0:
        break
    
    
# Checa si se gano o perdio
if isSolved:
    print ("Felicidades, adivinaste la palabra")
else:
    print ("Rayos, has sido ahorcado")
    
print ("La palabra era", myStatemnt)
            
print ("--- Finalizacion del programa ---")
        
        