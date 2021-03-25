# se recomienda poner la terminal mas grande o que se vea mas 
#-------------------------------79---------------------------------------------
# imports

from random import shuffle
from tabulate import tabulate
from typing import Tuple

# variables

NumberOfCardsRemaining = 0
MyHeaders =['','0','1','2','3','4','5','6','7','8','9']

#esta clase es para resumir los turnos de los jugadores
class PLAYERS_TURNS:
    P1_P_P1_N = (True,True) 
    P1_P_P2_N = (True,False)
    P2_P_P2_N = (False,False)
    P2_P_P1_N = (False,True)


#funciones y definiciones
def election(l):
    #ojo con los strings y las comillas
    print('elija la ',l,'° carta, seleccione las coordenadas\n'
    '(choose the ', l,' ° card, select the coordinates)\n')
    #se elije la coordenada x (filas)
    electionX = int(input('seleccione la coordenada x (filas): \n'
    '(select x coordinate): '))
    #se elije la coordenada y (columnas)
    electionY = int(input('seleccione la coordenada y (columnas): \n'
    '(select y coordinate):  '))
    #se muestra la coordenada puesta por el usuario
    print("coordenada en X: ",electionX, "coordenada en Y: ",electionY, '\n'
    '(X coordinate: ',electionX,' Y coordinate: ',electionY, ')\n')
    print('(',electionX,',',electionY,')')
    elections = (electionX*10+electionY)
    #retorna un numero 
    return elections

#las diferentes tipos de tablas (censurada, vacia y con numeros)
def GameSettings(numcard, options):
    if (options == 1): 
        LCT = []
        for censure in range(numcard):
            LCT.append('?')
            LCT.append('?')
        return LCT
    elif (options == 2): 
        y = 1
        LI = []
        for chance in range(numcard):
            LI.append(y)
            LI.append(y)
            y += 1
        shuffle(LI)
        return(LI)
    elif (options == 3): 
        Clear = []
        for Empty in range(numcard):
            Clear.append('')
            Clear.append('')
        return Clear

#se muestra la tabla con el tabulate
def ShowTable(List,Line,MyHeaders):
    Roster = []
    q = 0
    p = 10
    b = 0
    d = 10
    for Show in range(Line):
        register = List[q:d]
        register.insert(0,b)
        Roster.append(register)
        q += 10
        p += 1
        b += 1
        d += 10
    print(tabulate(Roster,headers=MyHeaders,tablefmt='fancy_grid'))

#las fases de los jugadores, el cual depende del numero del jugador
def PlayerPhase(P) -> Tuple[bool,bool]:
    print("jugador: ",P)
    ShowTable(Game,rows,MyHeaders)
    Ex = election(1)
    while(True):
        try:
            Game[Ex] = Mace[Ex]
            break
        except:
            print('no existe el número en la tabla \n'
            '(there is no number in the table)\n')
            print('intentelo otra vez \n'
            '(try again)')
            print('\n')
            ShowTable(Game,rows,MyHeaders)
            print('\n')
            Ex = election(1)
    ShowTable(Game,rows,MyHeaders)
    Xe = election(2)
    while(True):
        try:
            Game[Xe] = Mace[Xe]
            break
        except:
            print('no existe el número en la tabla \n'
            '(there is no number in the table)\n')
            print('intentelo otra vez \n'
            '(try again)')
            print('\n')
            ShowTable(Game,rows,MyHeaders)
            print('\n')
            Xe = election(2)
    ShowTable(Game,rows,MyHeaders)
    #se usa una clase para retornar los bool, bool
    if (Mace[Ex] == Mace[Xe]):
        Game[Ex] = ''
        Game[Xe] = ''
        print('Ganaste, jugador: ',P,' ,ganas un punto y sigues \n'
        '(You won, player:', P, ', you win a point and continue)\n')
        return PLAYERS_TURNS.P1_P_P1_N if P == 1 else PLAYERS_TURNS.P2_P_P2_N
    Game[Ex] = '?'
    Game[Xe] = '?'
    print('perdiste, jugador: ',P,' , pasa el siguiente jugador \n'
    '(you lost, player:', P, ', pass the next player)\n')
    return PLAYERS_TURNS.P1_P_P2_N if P == 1 else PLAYERS_TURNS.P2_P_P1_N

print('\n')
#--------------------------------***--------------------------------------------------
# los jugadores parten con 0 puntos cada uno
# jugadores
Score1 = 0 # puntaje jugador 1
Score2 = 0 # puntaje jugador 2

#empieza el juego
print('BIENVENIDO A JUEGO EL MEMORICE\n'
'(WELCOME TO THE MEMORICE GAME)')
print('\n')
# seleccion de cantidad de cartas y otros
card = int(input('elija la cantidad de cartas: \n'
'(choose the number of cards): '))
# un while "lock" para obligar al jugador que ponga un numero mayor a 0
while (True):
    if (card < 1):
        print('elija una cantidad mayor a 0\n'
        '(choose a quantity greater than 0)\n')
        card = int(input('elija la cantidad de cartas: \n'
        '(choose the number of cards): '))
    else:
        break
    
#----------variable extras -_-
cards = card * 2
rows = 0

Mace = GameSettings(card,2)
finish = GameSettings(card,3)
Game = GameSettings(card,1)
#------------------------
#pequeño algoritmo para ver la cantidad de filas que deberia tener la tabla (por ejemplo si el usuario pide
#13 cartas va seran 2 filas (10 columnas - 4 columnas)
# [probablemente se añada una fila]
if(cards >= 10):
    rows = int(cards/10)
    if( rows != (cards%10 == 0)):
        rows += 1
    print('se han generado: ',rows,'filas \n'
    '(have been generated:', rows, 'rows)')
else:
    rows += 1

# se muestran la cantidad de cartas totales (no las que ingreso el usuario)
print('cantidad de cartas: ',cards,'\n'
'(number of cards:', cards,')')
print('\n')

#juego
# se añaden puntos a los jugadores a los que ganan 
play = PlayerPhase(1)
if(play == PLAYERS_TURNS.P1_P_P1_N):
    Score1 += 1
    print('puntaje del jugador1: ', Score1,'\n'
    '(player1 score:', Score1,')')
while Game != finish:
    if(play == (True,True)):
        Score1 += 1
        print('puntaje del jugador1: ', Score1,'\n'
        '(player1 score:', Score1,')')
        play = PlayerPhase(1)
    elif (play == (False,False)):
        Score2 += 1
        print('puntaje del jugador2: ', Score2, '\n'
        '(player 2 score:', Score2,')')
        play = PlayerPhase(2)
    elif (play == (True,False)):
        print('puntaje del jugador2: ', Score2, '\n'
        '(player 2 score:', Score2,')')
        play = PlayerPhase(2)
    elif (play == (False,True)):
        print('puntaje del jugador1: ', Score1,'\n'
        '(player1 score:', Score1,')')
        play = PlayerPhase(1)
print('\n')
#puntajes y ganador
ShowTable(Game,rows,MyHeaders) #se muestra la tabla vacia
print('Resolucion del puntaje\n'
'Score resolution')
if (Score1 > Score2):
    Score1 += 1
    print("GANADOR: --> Jugador 1 <-- \n"
    '(WINNER: --> Player 1 <--)')
    print('puntaje jugador1: ',Score1,'\n'
    '(player1 score:', Score1,')')
    print('puntaje jugador2: ',Score2,'\n'
    '(player 2 score:', Score2,')')
elif (Score1 < Score2):
    Score2 += 1
    print("GANADOR: -->jugador 2 <--\n"
    '(WINNER: --> Player 2 <--)')
    print('puntaje jugador1: ',Score1,'\n'
    '(player1 score:', Score1,')')
    print('puntaje jugador2: ',Score2,'\n'
    '(player 2 score:', Score2,')')
else:
    print('EMPATE\n'
    'TIE')
    print('puntaje jugador1: ',Score1,'\n'
    '(player1 score:', Score1,')')
    print('puntaje jugador2: ',Score2,'\n'
    '(player 2 score:', Score2,')')