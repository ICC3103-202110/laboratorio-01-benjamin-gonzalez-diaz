# imports
import  random, sys
from random import randint
#import numpy


# variables
y = 1
NumberOfCardsRemaining = 1
LH = [] # lista horizontal
L = []
T = []
LI = []

#funciones y definiciones
def election(l):
    print("elija la ",l,"° carta, seleccione las coordenadas")
    electionX = int(input("seleccione la coordenada x: "))
    electionY = int(input("seleccione la coordenada y: "))
    elections = (electionX,electionY)
    return elections


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


def RandomCards(numcard):
    y = 1
    for m in range(numcard):
        LI.append(y)
        LI.append(y)
        y += 1
    random.shuffle(LI)
    print(LI)

def allCards(C1,C2):
    z = 0
    z = C1 - C2
    return z

def orderplayer():
    print("jugador: empieza")    
    print(election(1))
    print(election(2))
# seleccion de cantidad de cartas
card = int(input("elija la cantidad de cartas: "))
cards = card * 2

count = cards
print("cantidad de cartas: ",cards)

# jugadores
player1 = 0
player2 = 0

# azar
RandomCards(card)

#luego se deberan poner en un tablero 

#juego
# # imprimir tablero
horizontal(card)
CreateTable(card)
ShowTable()
print("jugador 1 empieza")
while (NumberOfCardsRemaining <= card):
    k = election(1)
    k1 = election(2)
    print (k, k1)
    if(k[0] == k1[0] and k[1] == k1[1]):    # por mientras
        NumberOfCardsRemaining +=  card
        player1 += 1
        print("puntaje:",NumberOfCardsRemaining)
    
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