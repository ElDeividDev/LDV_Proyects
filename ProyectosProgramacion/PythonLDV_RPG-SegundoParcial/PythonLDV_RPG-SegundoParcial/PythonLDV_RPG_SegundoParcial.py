
# Elegir Clases, en un ciclo infinito hasta que me maten
from asyncio.windows_events import NULL
from pydoc import visiblename
import random
from tkinter import CURRENT

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

print("-- Actividad 1 RPG --")

print("Juego: Elementales RPG")

_Ab_1F = {"enemHealth":-45,"pyrHealth":0}
_Ab_2F = {"enemHealth":-25,"pyrHealth":15}
_Ab_3F = {"enemHealth":-75,"pyrHealth":-35}

_Ab_1Ag = {"enemHealth":-30,"pyrHealth":0}
_Ab_2Ag = {"enemHealth":15,"pyrHealth":35}
_Ab_3Ag = {"enemHealth":-45,"pyrHealth":-10}

_Ab_1T = {"enemHealth":-20,"pyrHealth":0}
_Ab_2T = {"enemHealth":0,"pyrHealth":20}
_Ab_3T = {"enemHealth":-40,"pyrHealth":-25}

_Ab_1Ai = {"enemHealth":-20,"pyrHealth":0}
_Ab_2Ai = {"enemHealth":20,"pyrHealth":40}
_Ab_3Ai = {"enemHealth":-40,"pyrHealth":-25}

_AbilsFuego = {"Abil1":_Ab_1F,"Abil2":_Ab_2F,"Abil3":_Ab_3F}
_AbilsAgua = {"Abil1":_Ab_1Ag,"Abil2":_Ab_2Ag,"Abil3":_Ab_3Ag}
_AbilsTierra = {"Abil1":_Ab_1T,"Abil2":_Ab_2T,"Abil3":_Ab_3T}
_AbilsAire = {"Abil1":_Ab_1Ai,"Abil2":_Ab_2Ai,"Abil3":_Ab_3Ai}

_fuego = {"vida":15,"danio":50,"armadura":25,"clase":"fuego","Abilities":_AbilsFuego}
_agua = {"vida":60,"danio":30,"armadura":25,"clase":"agua","Abilities":_AbilsAgua}
_tierra = {"vida":100,"danio":20,"armadura":20,"clase":"tierra","Abilities":_AbilsTierra}
_aire = {"vida":150,"danio":20,"armadura":0,"clase":"aire","Abilities":_AbilsAire}

_petroleo = {"vida":75,"danio":10,"armadura":0,"clase":"petroleo"}
_plastico = {"vida":40,"danio":5,"armadura":30,"clase":"plastico"}
_mercurio = {"vida":25,"danio":20,"armadura":10,"clase":"mercurio"}
_plomo = {"vida":50,"danio":20,"armadura":0,"clase":"plomo"}

_Pychar = {"fuego":_fuego,"agua":_agua,"tierra":_tierra,"aire":_aire}
_Enchar = {"basura":_petroleo,"plastico":_plastico,"mercurio":_mercurio,"plomo":_plomo}

print("Hola jugador bienvenido a elementales, el juego de luchar contra la contaminacion")
print("En el juego puedes elegir a 4 diferentes clases de elementales")
print("-- Clases --")
print("Fuego: \n-Vida:",_fuego["vida"]," \n-Danio:", _fuego["danio"], " \n-Vida extra regenerativa:", _fuego["armadura"])
print("Agua: \n-Vida:",_agua["vida"]," \n-Danio:", _agua["danio"], " \n-Vida extra regenerativa:", _agua["armadura"])
print("Tierra: \n-Vida:",_tierra["vida"]," \n-Danio:", _tierra["danio"], " \n-Vida extra regenerativa:", _tierra["armadura"])
print("Aire: \n-Vida:",_aire["vida"]," \n-Danio:", _aire["danio"], " \n-Vida extra regenerativa:", _aire["armadura"])

pInput = ""
# enemyClass = ""

def chooseAlly (value):
    value = SimplifyVarValue(value)
    if value.isnumeric() == True:
        print ("Por favor no escriba numeros en el programa")
        return "X"
    for x in _Pychar.keys():
        if value == x:
            return x
    print ("Por favor escriba un valor valido")
    return "X"

def chooseEnemy ():
    myClass = random.choice(list(_Enchar.keys()))
    return myClass

# Se elige la clase del personaje
print("Elige la clase del primer personaje: Escribe 'fuego', 'agua', 'tierra', o 'aire'")
while True:
    pInput = input(":: ")
    playerClass = chooseAlly(pInput)
    if playerClass != "X":
        break
# Se elige la clase del enemigo inicial
enemyClass = chooseEnemy()

# Se elige al jugador y al enemigo
player = _Pychar[playerClass].copy()
enemy = _Enchar[enemyClass].copy()

myAbils = player["Abilities"].copy()

myAbil1 = myAbils["Abil1"].copy()
myAbil2 = myAbils["Abil2"].copy()
myAbil3 = myAbils["Abil3"].copy()

# Estas variables sirven para identificar el maximo de armadura que un personaje puede llegar para no regenerar demas
playerArmaduraFull = player["armadura"]
enemyArmaduraFull = enemy["armadura"]

playerVidaReal = player["vida"] + player["armadura"]
enemyVidaReal = enemy["vida"] + enemy["armadura"]

currentAbilDamage = 0
currentAbilHeal = 0

enemiesBeat = 0
isGameOn = True;
gameInput = ""
while isGameOn:
    print("Jugador: \n-Vida:",playerVidaReal," \n-Danio:", player["danio"])
    print("Enemigo: \n-Vida:",enemyVidaReal," \n-Danio:", enemy["danio"] )
    
    player["armadura"] = player["armadura"] - enemy["danio"]
    if player["armadura"] < 0:
        player["vida"] = player["vida"] + player["armadura"]
        player["armadura"] = 0
    playerVidaReal = player["vida"] + player["armadura"]
    print("Nos atacan, tenemos:",playerVidaReal,"de vida")
    if playerVidaReal <= 0:
        print ("Ya valimos")
        break
    
    # El jugador ataca al enemigo
    print ("Elige uno de las habilidades: \n-Escribe 1: Habilidad1: danio al enemigo:",-myAbil1["enemHealth"],", curacion al jugador: ",myAbil1["pyrHealth"],"\n-Escribe 2: Habilidad2: danio al enemigo",-myAbil2["enemHealth"],", curacion al jugador: ",myAbil2["pyrHealth"],"\n-Escribe 3: Habilidad3: danio al enemigo",-myAbil3["enemHealth"],", curacion al jugador: ",myAbil3["pyrHealth"])
    gameInput = input(":: ")
    if VerifyInput(gameInput):
        gameInput = int(gameInput)
        if gameInput == 1:
            currentAbilDamage = myAbil1["enemHealth"]
            currentAbilHeal = myAbil1["pyrHealth"]
        if gameInput == 1:
            currentAbilDamage = myAbil2["enemHealth"]
            currentAbilHeal = myAbil2["pyrHealth"]
        if gameInput == 1:
            currentAbilDamage = myAbil3["enemHealth"]
            currentAbilHeal = myAbil3["pyrHealth"]
    
    player["vida"] = player["vida"] + currentAbilHeal
    enemy["armadura"] = enemy["armadura"] + currentAbilDamage
    if enemy["armadura"] < 0:
        enemy["vida"] = enemy["vida"] + enemy["armadura"]
        enemy["armadura"]
    enemyVidaReal = enemy["vida"] + enemy["armadura"]
    print("Se ataca al enemigo, tiene:",enemyVidaReal,"de vida")
    if enemyVidaReal <= 0:
        print ("Aparece un nuevo enemigo")
        enemyClass = chooseEnemy()
        enemy = _Enchar[enemyClass].copy()
        enemyArmaduraFull = enemy["armadura"]
        enemyVidaReal = enemy["vida"] + enemy["armadura"]
        enemiesBeat += 1
        continue
    
    if (enemyArmaduraFull > enemy["armadura"]):
        enemy["armadura"] += 5
        if (enemyArmaduraFull < enemy["armadura"]):
            enemy["armadura"] = enemyArmaduraFull
        print("El enemigo regenero 5 de armadura")

    if player["armadura"] < 0:
        player["vida"] = player["vida"] + player["armadura"]
        player["armadura"] = 0
    playerVidaReal = player["vida"] + player["armadura"]
    print("Checamos nuestra vida, tenemos:",playerVidaReal,"de vida")
    if playerVidaReal <= 0:
        print ("Ya valimos")
        break
    
    if (playerArmaduraFull > player["armadura"]):
        player["armadura"] += 5
        if (playerArmaduraFull < player["armadura"]):
            player["armadura"] = playerArmaduraFull
        print("Se regenero 5 de armadura")
    
print ("--- Game Over ---")

print ("Derrotaste a",enemiesBeat,"enemigos")
    
    


