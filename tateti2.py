# Tablero de juego
tablero = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
# Tablero de ayuda
ayuda = [" Tablero de referencias ", " 0 1 2 ", " 3 4 5 ", " 6 7 8 "]
# Definicion del primer jugador
jugador1 = ""
# Definicion del segundo jugador
jugador2 = ""
# Definicion del ganador
Ganador = ""
# Counter para las rondas
counter = 0

# Funcion para asignar valores a cada jugador
def asignacionValores():
    global jugador1
    global jugador2
    decision = input("¿Qué figura sera el jugador 1? X u O ")
    if decision == "x" or decision == "X":
        jugador1 = "X"
        jugador2 = "O"
    else:
        jugador1 = "O"
        jugador2 = "X"

    print("El jugador 1 será " + jugador1)
    print("El jugador 2 será " + jugador2)
    print("El jugador que comienza la partida será el jugador 1")


# Funcion para mostrar el tablero en su estado actual al momento de ser llamada
def verTablero():
    for x in tablero:
        print(x)


# Funcion para enseñar un tablero con numeros correspondientes a las posiciones del tablero
def verAyuda():
    for j in ayuda:
        print(j, end="\n")


# Funcion para analizar los movimientos, el estado del tablero y definir un ganador cuando sea posible
def posicion1():
    ficha = int(input("jugador 1 ingrese el numero donde colocará su ficha "))
    if ficha < 3:
        if tablero[0][ficha] != "-":
            print("ocupado")
            posicion1()
        else:
            tablero[0][ficha] = jugador1
    elif ficha >= 3 and ficha <= 5:
        if tablero[1][ficha - 3] != "-":
            print("ocupado")
            posicion1()
        else:
            tablero[1][ficha - 3] = jugador1
    elif ficha > 5 and ficha <= 8:
        if tablero[2][ficha - 6] != "-":
            print("ocupado")
            posicion1()
        else:
            tablero[2][ficha - 6] = jugador1


def posicion2():
    ficha = int(input("jugador 2 ingrese el numero donde colocará su ficha "))
    if ficha < 3:
        if tablero[0][ficha] != "-":
            print("ocupado")
            posicion2()
        else:
            tablero[0][ficha] = jugador2
    elif ficha >= 3 and ficha <= 5:
        if tablero[1][ficha - 3] != "-":
            print("ocupado")
            posicion2()
        else:
            tablero[1][ficha - 3] = jugador2
    elif ficha > 5 and ficha <= 8:
        if tablero[2][ficha - 6] != "-":
            print("ocupado")
            posicion2()
        else:
            tablero[2][ficha - 6] = jugador2


def ganadorJuego():
    global Ganador
    GanadorHorizontal()
    GanadorVertical()
    GanadorDiagonal()


# Funcion para definir si hay algun ganador en sentido vertical
def GanadorVertical():
    global Ganador
    if (
        tablero[0][0] == jugador1
        and tablero[1][0] == jugador1
        and tablero[2][0] == jugador1
    ):
        Ganador = jugador1
    elif (
        tablero[0][0] == jugador2
        and tablero[1][0] == jugador2
        and tablero[2][0] == jugador2
    ):
        Ganador = jugador2
    elif (
        tablero[0][1] == jugador1
        and tablero[1][1] == jugador1
        and tablero[2][1] == jugador1
    ):
        Ganador = jugador1
    elif (
        tablero[0][1] == jugador2
        and tablero[1][1] == jugador2
        and tablero[2][1] == jugador2
    ):
        Ganador = jugador2
    elif (
        tablero[0][2] == jugador1
        and tablero[1][2] == jugador1
        and tablero[2][2] == jugador1
    ):
        Ganador = jugador1
    elif (
        tablero[0][2] == jugador2
        and tablero[1][2] == jugador2
        and tablero[2][2] == jugador2
    ):
        Ganador = jugador2


# Funcion para definir si hay algun ganador en sentido horizontal
def GanadorHorizontal():
    global Ganador
    if (
        tablero[0][0] == jugador1
        and tablero[0][1] == jugador1
        and tablero[0][2] == jugador1
    ):
        Ganador = jugador1
    elif (
        tablero[0][0] == jugador2
        and tablero[0][1] == jugador2
        and tablero[0][2] == jugador2
    ):
        Ganador = jugador2
    elif (
        tablero[1][0] == jugador1
        and tablero[1][1] == jugador1
        and tablero[1][2] == jugador1
    ):
        Ganador = jugador1
    elif (
        tablero[1][0] == jugador2
        and tablero[1][1] == jugador2
        and tablero[1][2] == jugador2
    ):
        Ganador = jugador2
    elif (
        tablero[2][0] == jugador1
        and tablero[2][1] == jugador1
        and tablero[2][2] == jugador1
    ):
        Ganador = jugador1
    elif (
        tablero[2][0] == jugador2
        and tablero[2][1] == jugador2
        and tablero[2][2] == jugador2
    ):
        Ganador = jugador2


# Funcion para definir si hay algun ganador en sentido diagonal
def GanadorDiagonal():
    global Ganador
    if (
        tablero[0][0] == jugador1
        and tablero[1][1] == jugador1
        and tablero[2][2] == jugador1
    ):
        Ganador = jugador1
    elif (
        tablero[0][0] == jugador2
        and tablero[1][1] == jugador2
        and tablero[2][2] == jugador2
    ):
        Ganador = jugador2
    elif (
        tablero[2][0] == jugador1
        and tablero[1][1] == jugador1
        and tablero[0][2] == jugador1
    ):
        Ganador = jugador1
    elif (
        tablero[2][0] == jugador1
        and tablero[1][1] == jugador1
        and tablero[0][2] == jugador2
    ):
        Ganador = jugador2


# Ejecucion de la asignacion previo a jugar
asignacionValores()

# Funcion que desarrolla el juego hasta haber un ganador
def jugar():
    global ficha
    global counter
    while Ganador == "":
        verTablero()
        verAyuda()
        posicion1()
        counter += 1
        ganadorJuego()
        if Ganador != "":
            print("Felicitaciones jugador 1 has ganado")
            break
        if counter >= 9 and Ganador == "":
            print("Han empatado")
            break
        verTablero()
        verAyuda()
        posicion2()
        counter += 1
        ganadorJuego()
        if Ganador != "":
            print("Felicitaciones jugador 2 has ganado")
            break
        if counter >= 9 and Ganador == "":
            print("empate")
            break


jugar()
