# se recomienda poner la terminal lo mas grande, para poder ver toda la tabla
#-------------------------------79---------------------------------------------
# se asume que el jugador no va a volver a elegir las cartas que ya quito
# cuando el usuario elige mas >6 cartas aparece una fila mas
# a veces los puntajes salen mal puestos (cuanto se elige jugar con 3 cartas)
# con 'locked' me refiero a que no podra seguir hasta que cumpla la condicion
# imports

from random import shuffle
from tabulate import tabulate
from typing import Tuple

# variables
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
    someone = 0
    if (options == 1): 
        LCT = []
        for censure in range(numcard):
            LCT.append('¿?')
            LCT.append('¿?')
            someone += censure
        return LCT
    elif (options == 2): 
        y = 1
        LI = []
        for chance in range(numcard):
            LI.append(y)
            LI.append(y)
            someone += chance
            y += 1
        shuffle(LI)
        return(LI)
    elif (options == 3): 
        Clear = []
        for Empty in range(numcard):
            Clear.append('')
            Clear.append('')
            someone += Empty
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
        p += Show
        b += 1
        d += 10
    print(tabulate(Roster,headers=MyHeaders,tablefmt='fancy_grid'))

#las fases de los jugadores, el cual depende del numero del jugador
# cada vez que sale el ShowTable se muestra la tabla
def PlayerPhase(P) -> Tuple[bool,bool]:
    print("jugador: ",P)
    ShowTable(Game,rows,MyHeaders) 
    Ex = election(1) 
    while(True):# un while 'locked' para evitar que el jugador elija una coordenada
                # inexistente
        try:
            if(Game[Ex] == ''):
                ShowTable(Game,rows,MyHeaders)
                print(
                '(the card has already been taken)\n')
                Ex = election(1) 
            else:
                Game[Ex] = Mace[Ex] #se compara la coordenada con la 2  tablas
                break
        except:
            #cuando no esta el numero en la tabla
            print(
            '(there is no space for number in the table)\n')
            print(
            '(try again)')
            print('\n')
            ShowTable(Game,rows,MyHeaders)
            print('\n')
            Ex = election(1) #se le vuelve a repetie la eleccion
    ShowTable(Game,rows,MyHeaders)
    Xe = election(2)
    while(True): # lo mismo que en el while de arriba para la 2°carta
        try:
            if(Game[Xe] == ''):
                ShowTable(Game,rows,MyHeaders)
                print(
                '(the card has already been taken)\n')
                Xe = election(2)
            else:
                Game[Xe] = Mace[Xe]
                break
        except:
            print(
            '(there is no space for number in the table)\n')
            print(
            '(try again)')
            print('\n')
            ShowTable(Game,rows,MyHeaders)
            print('\n')
            Xe = election(2)
    while(Ex == Xe):
        print('ojo con elegir la misma coordenada\n' # para evitar elegir la misma coordenada y ganar un punto
        'be careful with choosing the same coordinate\n')
        ShowTable(Game,rows,MyHeaders)
        Xe = election(2) #se vuelve a repetir la segunda eleccion (elegir la segunda carta)
        while(True):
            try:
                if(Game[Xe] == ''):
                    ShowTable(Game,rows,MyHeaders)
                    print(
                    '(the card has already been taken)\n')
                    Xe = election(2)
                else:
                    Game[Xe] = Mace[Xe]
                    break
            except:
                print(
                '(there is no number in the table)\n')
                print(
                '(try again)')
                print('\n')
                ShowTable(Game,rows,MyHeaders)
                print('\n')
                Xe = election(2)
        if(Ex != Xe):
            break
    ShowTable(Game,rows,MyHeaders)
    #se usa una clase para retornar los bool, bool
    if (Mace[Ex] == Mace[Xe]):
        Game[Ex] = ''
        Game[Xe] = ''
        print(
        '(You won, player:', P, ', you win a point and continue)\n')
        return PLAYERS_TURNS.P1_P_P1_N if P == 1 else PLAYERS_TURNS.P2_P_P2_N
    Game[Ex] = '¿?'
    Game[Xe] = '¿?'
    print(
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
print('\ncolumnas maximas [0-9]\n'
'Max columns [0-9]')
print('\n')
# seleccion de cantidad de cartas y otros
card = int(input(
'(choose the number of cards): '))
# un while "locked" para obligar al jugador que ponga un numero mayor a 0
while (True):
    if (card < 1):
        print(
        '(choose a quantity greater than 0)\n')
        card = int(input(
        '(choose the number of cards): '))
    else:
        break
    
#----------variable extras -_-
cards = card * 2
rows = 0

Mace = GameSettings(card,2) #tabla con numeros
finish = GameSettings(card,3)#tabla vacia
Game = GameSettings(card,1) #tabla censurada
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
# si no las cartas del tablero (que serian 2 veces las cartas que ingreso el usuario)
print('cantidad de cartas: ',cards,'\n'
'(number of cards:', cards,')')
print('\n')

#juego
# se añaden puntos a los jugadores a los que ganan 
play = PlayerPhase(1)
if(play == PLAYERS_TURNS.P1_P_P1_N):
    Score1 += 1
    print(
    '(player 1 score:', Score1,')')
while Game != finish:
    #se añaden los puntos al ganar 
    # y no se añade nada al perder
    if(play == (True,True)):
        Score1 += 1
        print(
        '(player 1 score:', Score1,')')
        play = PlayerPhase(1)
    elif (play == (False,False)):
        Score2 += 1
        print(
        '(player 2 score:', Score2,')')
        play = PlayerPhase(2)
    elif (play == (True,False)):
        print(
        '(player 2 score:', Score2,')')
        play = PlayerPhase(2)
    elif (play == (False,True)):
        print(
        '(player 1 score:', Score1,')')
        play = PlayerPhase(1)
print('\n')
#puntajes y ganador
ShowTable(Game,rows,MyHeaders) #se muestra la tabla vacia
print('Resolucion del puntaje\n'
'Score resolution')
if (Score1 > Score2):
    if(card % 2 == 0):
        Score1 += 0
    else:
        Score1 += 1
    print(
    '(WINNER: --> Player 1 <--) \n\n')
    print(
    '(player 1 score:', Score1,')')
    print(
    '(player 2 score:', Score2,')')
elif (Score1 < Score2):
    if (card % 2 == 0):
        Score2 += 0
    else:
        Score2 += 1
    print(
    '(WINNER: --> Player 2 <--)\n\n')
    print(
    '(player 1 score:', Score1,')')
    print(
    '(player 2 score:', Score2,')')
else:
    print(
    'TIE\n')
    print(
    '(player 1 score:', Score1,')')
    print(
    '(player 2 score:', Score2,')')