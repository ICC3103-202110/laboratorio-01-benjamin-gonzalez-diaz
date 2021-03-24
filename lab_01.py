# imports
import  random, sys
from random import shuffle
from tabulate import tabulate
from typing import Tuple

# variables
y = 1
NumberOfCardsRemaining = 0
parity = 3
L = []
T = []
MyHeaders =['','0','1','2','3','4','5','6','7','8','9']

class PLAYERS_TURNS:
    P1_P_P1_N = (True,True) 
    P1_P_P2_N = (True,False)
    P2_P_P2_N = (False,False)
    P2_P_P1_N = (False,True)


#funciones y definiciones
def election(l):
    print("elija la ",l,"° carta, seleccione las coordenadas")
    electionX = int(input("seleccione la coordenada x: "))
    electionY = int(input("seleccione la coordenada y: "))
    print("coordenada en X: ", electionX, "coordenada en Y: ", electionY)
    print('(',electionX,',',electionY,')')
    elections = (electionX*10+electionY)
    return elections


def GameTable(numcard, options):
    if (options == 1): 
        rand = random.randint(0,3)
        LCT = []
        for h in range(numcard):
            LCT.append('?')
            LCT.append('?')
        return LCT
    elif (options == 2): 
        y = 1
        LI = []
        for m in range(numcard):
            LI.append(y)
            LI.append(y)
            y += 1
        shuffle(LI)
        return(LI)
    elif (options == 3): 
        Clear = []
        for C in range(numcard):
            Clear.append('')
            Clear.append('')
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
    print(tabulate(Roster,headers=MyHeaders,tablefmt='fancy_grid'))

def PlayerPhase(P) -> Tuple[bool,bool]:
    print("jugador: ",P)
    CreatedTable(Game,rows,MyHeaders)
    Ex = election(1)
    while(True):
        try:
            Game[Ex] = Mace[Ex]
            break
        except:
            print('no existe el número en la tabla')
            print('intentelo otra vez')
            print('\n')
            CreatedTable(Game,rows,MyHeaders)
            print('\n')
            Ex = election(1)
    CreatedTable(Game,rows,MyHeaders)
    Xe = election(2)
    while(True):
        try:
            Game[Xe] = Mace[Xe]
            break
        except:
            print('no existe el numero en la tabla')
            print('intentelo otra vez')
            print('\n')
            CreatedTable(Game,rows,MyHeaders)
            print('\n')
            Xe = election(2)
    CreatedTable(Game,rows,MyHeaders)

    if (Mace[Ex] == Mace[Xe]):
        Game[Ex] = ''
        Game[Xe] = ''
        print("Ganaste, jugador:",P," , toma las cartas, ganas un punto y sigues")
        return PLAYERS_TURNS.P1_P_P1_N if P == 1 else PLAYERS_TURNS.P2_P_P2_N
    Game[Ex] = '?'
    Game[Xe] = '?'
    print("perdiste, jugador ",P," , pasa el siguiente jugador")
    return PLAYERS_TURNS.P1_P_P2_N if P == 1 else PLAYERS_TURNS.P2_P_P1_N

print('\n')

# jugadores
player1 = 0
player2 = 0

print('\n')

# seleccion de cantidad de cartas y otros
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
print('cantidad de cartas: ,cards')
print('\n')
#juego

play = PlayerPhase(1)
if(play == PLAYERS_TURNS.P1_P_P1_N):
    player1 += 1
    print('puntaje del jugador1: ', player1)
while Game != finish:
    if(play == (True,True)):
        player1 += 1
        print('puntaje del jugador1: ', player1)
        play = PlayerPhase(1)
    elif (play == (False,False)):
        player2 += 1
        print('puntaje del jugador2: ', player2)
        play = PlayerPhase(2)
    elif (play == (True,False)):
        print('puntaje del jugador2: ', player2)
        play = PlayerPhase(2)
    elif (play == (False,True)):
        print('puntaje del jugador1: ', player1)
        play = PlayerPhase(1)
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