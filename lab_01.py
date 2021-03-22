import  random
from random import randint

# comprobacion de cartas
cartas = int(input("elija la cantidad de cartas (debe ser par)"))
while (True):
    if (cartas % 2 == 0):
        break
    else:
        cartas = int(input("elija la cantidad de cartas (debe ser par)"))

# jugadores
jugador1 = 0
jugador2 = 0

# azar
ran = random.randint(0,cartas)
ran1 = random.randint(0,cartas)

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

    