# imports
import  random
from random import randint


#funciones y definiciones
def election():
    election = float(input("seleccion una coordenada (por ejemplo: 5.6): "))
    print(election)
    return ''

# seleccion de cantidad de cartas
card = int(input("elija la cantidad de cartas: "))
cards = card * 2
print("cantidad de cartas: ",cards)

# jugadores
player1 = 0
player2 = 0

# azar
ran = random.randint(0,cards)
ran1 = random.randint(0,cards)

# Creacion de la matriz, L = listas
y = 20
Lx = []
Ly = []
L = []
z = ('   1| 2| 3| 4| 5')
print(z)
for i in range(1):
    for j in range(5):
        L.append(ran)
    print(i+1, (L))



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