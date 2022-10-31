# Tomi: Un array con tres posiciones de la sgte manera
# 012,
# 345,
# 678
# Tomi: El cliente tiene una opción para elegir el nro de la posición a completar
# Tomi: Opción para elegir con que empezar si x u o

import random


class Juego:
    def __init__(self):
        # Imprimir tablero
        self.tablero = [['-', '-', '-'],
                        ['-', '-', '-'],
                        ['-', '-', '-']]
        self.ayuda = [' Tablero de referencias ', " 0 1 2 ",
                      ' 3 4 5 ', ' 6 7 8 ']
        self.jugadores = ["jugador 1", "jugador 2"]
        # self.comienzo = random.choice(self.jugadores)

        # Mostras el tablero vacio
        for x in self.tablero:
            print(x)

        # Mostras el tablero de referencias
        for j in self.ayuda:
            print(j, end="\n")

        # Asignacion de valores
        self.jugador1 = ''
        self.jugador2 = ''

        decision = input('¿Qué figura sera el jugador 1? X u O ')
        if decision == 'x' or decision == "X":
            self.jugador1 = 'X'
            self.jugador2 = 'O'
        else:
            self.jugador1 = 'O'
            self.jugador2 = 'X'

        print('El jugador 1 será ' + self.jugador1)
        print('El jugador 2 será ' + self.jugador2)

        # Decision aleatoria de quien comienza la partida
        print('El jugador que comienza la partida será el jugador 1')

        # Comienzo del juego
        # Como determinar que simbolo es el primero y asi continuamente

        while True:
            for j in self.ayuda:
                print(j, end="\n")

            self.ficha = int(
                input('jugador 1 ingrese el numero donde colocará su primera ficha '))

            if self.ficha < 3:
                self.tablero[0][self.ficha] = self.jugador1
            elif self.ficha >= 3 and self.ficha <= 5:
                self.tablero[1][self.ficha - 3] = self.jugador1
            else:
                self.tablero[2][self.ficha - 6] = self.jugador1

            for x in self.tablero:
                print(x)

            # Swtich Case para revisar quien gana y cortar el bucle while
                # En horizontal
            if self.tablero[0][0] == self.jugador1 and self.tablero[0][1] == self.jugador1 and self.tablero[0][2] == self.jugador1:
                break
            elif self.tablero[0][0] == self.jugador2 and self.tablero[0][1] == self.jugador2 and self.tablero[0][2] == self.jugador2:
                break
            elif self.tablero[1][0] == self.jugador1 and self.tablero[1][1] == self.jugador1 and self.tablero[1][2] == self.jugador1:
                break
            elif self.tablero[1][0] == self.jugador2 and self.tablero[1][1] == self.jugador2 and self.tablero[1][2] == self.jugador2:
                break
            elif self.tablero[2][0] == self.jugador1 and self.tablero[2][1] == self.jugador1 and self.tablero[2][2] == self.jugador1:
                break
            elif self.tablero[2][0] == self.jugador2 and self.tablero[2][1] == self.jugador2 and self.tablero[2][2] == self.jugador2:
                break

                # En vertical
            if self.tablero[0][0] == self.jugador1 and self.tablero[1][0] == self.jugador1 and self.tablero[2][0] == self.jugador1:
                break
            elif self.tablero[0][0] == self.jugador2 and self.tablero[1][0] == self.jugador2 and self.tablero[2][0] == self.jugador2:
                break
            elif self.tablero[0][1] == self.jugador1 and self.tablero[1][1] == self.jugador1 and self.tablero[2][1] == self.jugador1:
                break
            elif self.tablero[0][1] == self.jugador2 and self.tablero[1][1] == self.jugador2 and self.tablero[2][1] == self.jugador2:
                break
            elif self.tablero[0][2] == self.jugador1 and self.tablero[1][2] == self.jugador1 and self.tablero[2][2] == self.jugador1:
                break
            elif self.tablero[0][2] == self.jugador2 and self.tablero[1][2] == self.jugador2 and self.tablero[2][2] == self.jugador2:
                break

                # En diagonal
            if self.tablero[0][0] == self.jugador1 and self.tablero[1][1] == self.jugador1 and self.tablero[2][2] == self.jugador1:
                break
            elif self.tablero[0][0] == self.jugador2 and self.tablero[1][1] == self.jugador2 and self.tablero[2][2] == self.jugador2:
                break
            elif self.tablero[2][0] == self.jugador1 and self.tablero[1][1] == self.jugador1 and self.tablero[0][2] == self.jugador1:
                break
            elif self.tablero[2][0] == self.jugador1 and self.tablero[1][1] == self.jugador1 and self.tablero[0][2] == self.jugador2:
                break

            for j in self.ayuda:
                print(j, end="\n")

            self.ficha = int(
                input('jugador 2 ingrese el numero donde colocará su primera ficha '))

            if self.ficha < 3:
                self.tablero[0][self.ficha] = self.jugador2
            elif self.ficha >= 3 and self.ficha <= 5:
                self.tablero[1][self.ficha - 3] = self.jugador2
            else:
                self.tablero[2][self.ficha - 6] = self.jugador2

            for x in self.tablero:
                print(x)

            # Swtich Case para revisar quien gana y cortar el bucle while
                # En horizontal
            if self.tablero[0][0] == self.jugador1 and self.tablero[0][1] == self.jugador1 and self.tablero[0][2] == self.jugador1:
                break
            elif self.tablero[0][0] == self.jugador2 and self.tablero[0][1] == self.jugador2 and self.tablero[0][2] == self.jugador2:
                break
            elif self.tablero[1][0] == self.jugador1 and self.tablero[1][1] == self.jugador1 and self.tablero[1][2] == self.jugador1:
                break
            elif self.tablero[1][0] == self.jugador2 and self.tablero[1][1] == self.jugador2 and self.tablero[1][2] == self.jugador2:
                break
            elif self.tablero[2][0] == self.jugador1 and self.tablero[2][1] == self.jugador1 and self.tablero[2][2] == self.jugador1:
                break
            elif self.tablero[2][0] == self.jugador2 and self.tablero[2][1] == self.jugador2 and self.tablero[2][2] == self.jugador2:
                break

                # En vertical
            if self.tablero[0][0] == self.jugador1 and self.tablero[1][0] == self.jugador1 and self.tablero[2][0] == self.jugador1:
                break
            elif self.tablero[0][0] == self.jugador2 and self.tablero[1][0] == self.jugador2 and self.tablero[2][0] == self.jugador2:
                break
            elif self.tablero[0][1] == self.jugador1 and self.tablero[1][1] == self.jugador1 and self.tablero[2][1] == self.jugador1:
                break
            elif self.tablero[0][1] == self.jugador2 and self.tablero[1][1] == self.jugador2 and self.tablero[2][1] == self.jugador2:
                break
            elif self.tablero[0][2] == self.jugador1 and self.tablero[1][2] == self.jugador1 and self.tablero[2][2] == self.jugador1:
                break
            elif self.tablero[0][2] == self.jugador2 and self.tablero[1][2] == self.jugador2 and self.tablero[2][2] == self.jugador2:
                break

        print('Felicitaciones ganaste')


tateti = Juego()
