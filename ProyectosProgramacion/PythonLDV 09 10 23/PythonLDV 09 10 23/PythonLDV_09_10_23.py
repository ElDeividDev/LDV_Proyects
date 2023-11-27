
# Elegir Clases, en un ciclo infinito hasta que me maten
from asyncio.windows_events import NULL
from pydoc import visiblename
import random

print("-- Actividad 1 RPG --")

print("Juego: Elementales RPG")

_fuego = {"vida":15,"danio":50,"armadura":25,"clase":"fuego"}
_agua = {"vida":60,"danio":30,"armadura":25,"clase":"agua"}
_tierra = {"vida":100,"danio":20,"armadura":20,"clase":"tierra"}
_aire = {"vida":150,"danio":20,"armadura":0,"clase":"aire"}

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

def returnPossibleValueString (value):
    value = value.lower()
    value = value.replace(" ","")
    return value

def chooseAlly (value):
    value = returnPossibleValueString(value)
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

player = _Pychar[playerClass].copy()
enemy = _Enchar[enemyClass].copy()

# Estas variables sirven para identificar el maximo de armadura que un personaje puede llegar para no regenerar demas
playerArmaduraFull = player["armadura"]
enemyArmaduraFull = enemy["armadura"]

playerVidaReal = player["vida"] + player["armadura"]
enemyVidaReal = enemy["vida"] + enemy["armadura"]

enemiesBeat = 0
isGameOn = True;
while isGameOn:
    print("Jugador: \n-Vida:",playerVidaReal," \n-Danio:", player["danio"])
    print("Enemigo: \n-Vida:",enemyVidaReal," \n-Danio:", enemy["danio"] )
    input("Presione cualquier tecla para continuar")

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
    enemy["armadura"] = enemy["armadura"] - player["danio"]
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
    if (playerArmaduraFull > player["armadura"]):
        player["armadura"] += 5
        if (playerArmaduraFull < player["armadura"]):
            player["armadura"] = playerArmaduraFull
        print("Se regenero 5 de armadura")
    
print ("--- Game Over ---")

print ("Derrotaste a",enemiesBeat,"enemigos")
    
    

