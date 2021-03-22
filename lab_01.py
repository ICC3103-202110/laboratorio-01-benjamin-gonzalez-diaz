# imports
import  random
from random import randint
from random import shuffle

# variables
y = 20
LH = [] # lista horizontal
L = []
T = []

#funciones y definiciones
def election():
    election = float(input("seleccion una coordenada (por ejemplo: 5.6): "))
    print(election)
    return ''

def CreateTable(numCard):
    for i in range(numCard):
        LINE = []
        for j in range(numCard):
            LINE.append("*")
        T.append(LINE)


def  ShowTable():
    for i in T:
        for j in i:
            print( j, end= " ")
        print()
    print('')


def horizontal(count):
    for x in range(count):
        LH.append(x)
    print(LH)

# seleccion de cantidad de cartas
card = int(input("elija la cantidad de cartas: "))
cards = card * 2
count = cards
print("cantidad de cartas: ",cards)

# jugadores
player1 = 0
player2 = 0

# azar
ran = random.randint(0,cards)
ran1 = random.randint(0,cards)

# imprimir tablero


horizontal(count)
CreateTable(cards)
ShowTable()



#juego
#while (True)
print("jugador1: empieza")

print(election())

#puntajes y ganador

if (player1 > player2):
    print("ganador: Jugador 1")
    print(player1)
    print(player2)
elif (player1 < player2):
    print("ganador: jugador 2")
    print(player1)
    print(player2)
else:
    print("empate")
    print(player1)
    print(player2)