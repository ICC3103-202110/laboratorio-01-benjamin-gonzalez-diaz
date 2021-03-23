# imports
import  random, sys
from random import shuffle
from tabulate import tabulate

# variables
y = 1
NumberOfCardsRemaining = 1
L = []
T = []
MyHeaders =['','0','1','2','3','4','5','6','7','8','9']

#funciones y definiciones
def election(l):
    print("elija la ",l,"° carta, seleccione las coordenadas")
    electionX = int(input("seleccione la coordenada x: "))
    electionY = int(input("seleccione la coordenada y: "))
    print("coordenada en X: ", electionX, "coordenada en Y: ", electionY)
    print('(',electionX,',',electionY,')')
    elections = (electionX*10+electionY)
    return elections


def GameTable(numcard, opt):
    if (opt == 1): 
        rand = random.randint(0,3)
        LCT = []
        for h in range(numcard):
            LCT.append('?')
            LCT.append('?')
        return LCT
    elif (opt == 2): 
        y = 1
        LI = []
        for m in range(numcard):
            LI.append(y)
            LI.append(y)
            y += 1
        shuffle(LI)
        return(LI)
    elif (opt == 3): 
        Clear = []
        for C in range(numcard):
            Clear.append('_')
            Clear.append('_')
        return Clear

def CreatedTable(List,Line,MyHeaders):
    Roster = []
    q = 0
    p = 10
    b = 0
    d = 10
    for CT in range(Line):
        register = List[q:d]
        register.insert(0,b)
        Roster.append(register)
        q += 10
        p += 1
        b += 1
        d += 10
    print(tabulate(Roster,headers=MyHeaders))

def PlayerPhase(P):
    print("jugador: ",P,"empieza")
    CreatedTable(Game,rows,MyHeaders)
    Ex = election(1)
    Game[Ex] = Mace[Ex]
    CreatedTable(Game,rows,MyHeaders)
    Xe = election(2)
    Game[Xe] = Mace[Xe]
    CreatedTable(Game,rows,MyHeaders)
    if (Mace[Ex] == Mace[Xe] and P == 1):
        Game[Ex] = '_'
        Game[Xe] = '_'
        print("Ganaste, jugador:",P," , toma las cartas, ganas un punto y sigues")
        return (True,True)

    elif (Mace[Ex] == Mace[Xe] and P == 2):
        Game[Ex] = '_'
        Game[Xe] = '_'
        print("Ganaste, jugador:",P," , toma las cartas, ganas un punto y sigues")
        return (False,False)

    elif (Mace[Ex] != Mace[Xe] and P == 2):
        Game[Ex] = '?'
        Game[Xe] = '?'
        print("perdiste, jugador ",P," , pasa el siguiente jugador")
        return (False,True)

    elif (Mace[Ex] != Mace[Xe] and P == 1):
        Game[Ex] = '?'
        Game[Xe] = '?'
        print("perdiste, jugador ",P," , pasa el siguiente jugador")
        return (True, False)

print('\n')
# jugadores
player1 = 0
player2 = 0

print('\n')
# seleccion de cantidad de cartas
card = int(input("elija la cantidad de cartas: "))
cards = card * 2
count = cards
rows = 0

Mace = GameTable(card,2)
finish = GameTable(card,3)
Game = GameTable(card,1)
if(cards >= 10):
    rows = int(cards/10)
    if( rows != (cards%10 == 0)):
        rows += 1
    print('se han generado: ',rows,'filas')
else:
    rows += 1
#print('se han generado: ',len(MyHeaders)-1,'columnas [del 0 al 9]')
print("cantidad de cartas: ",cards)
print('\n')
#juego

PlayerPhase(1)

print('\n')
#puntajes y ganador

print('Resolucion del puntaje')
if (player1 > player2):
    print("ganador: Jugador 1")
    print('puntaje: jugador1: ',player1)
    print('puntaje: jugador2: ',player2)
elif (player1 < player2):
    print("ganador: jugador 2")
    print('puntaje: jugador1: ',player1)
    print('puntaje: jugador2: ',player2)
else:
    print("empate")
    print('puntaje: jugador1: ',player1)
    print('puntaje: jugador2: ',player2)