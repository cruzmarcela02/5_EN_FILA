import re
import gamelib

ANCHO_VENTANA = 300
ALTO_VENTANA = 340
TITLE = '5 EN FILA'
VACIO = ''
CRUZ = 'X'
CIRCULO = 'O'

'''
Diseno del grilla 10 x 10 - Lista de lista de cadena
'''

def juego_crear():
    """Inicializar el estado del juego"""
    grilla = []
    for filas in range(10):
        fila = []
        for columnas in range (10):
            fila.append(VACIO)
        
        grilla.append(fila)
    turno_jugador = True

    mi_juego = {
        'grilla' : grilla,
        'turno': turno_jugador,
        'jugador': CRUZ,
    }
    
    return mi_juego


def detectar_posicion(x,y):

    if  (0 <= x < 300) and (0 <= y < 300):
        posicion_columna = x // 30 
        posicion_fila = y // 30 
        return posicion_fila, posicion_columna # retorna en forma de tupla
    else:
        return None,None

def hay_jugada(juego, posicion_fila, posicion_columna):
    '''Devolvera True si hay X - O, si no hay nada devuelve False -- (juego,x,y)'''
    return juego[posicion_fila][posicion_columna] == CRUZ or juego[posicion_fila][posicion_columna] == CIRCULO


def se_acabo(juego):
    '''
    Devuelve True si todas las casillas fueron ocupadas.
    '''
    for fila in juego:
        for columnas in fila:
            if columnas == VACIO:
                return False
    return True

def detectar_centro_interfaz(ubicacion_fila, ubicacion_columna):
    centro_x = (ubicacion_columna * 30) + 15
    centro_y = (ubicacion_fila * 30) + 15
    return centro_x, centro_y

def juego_actualizar(juego, x, y):
    """Actualizar el estado del juego

    x e y son las coordenadas (en pixels) donde el usuario hizo click.
    Esta función determina si esas coordenadas corresponden a una celda
    del tablero; en ese caso determina el nuevo estado del juego y lo
    devuelve.
    """

    '''
    Obtenemos las coordenadas de la casilla a jugar
    '''

    ubicacion_fila, ubicacion_columna = detectar_posicion(x,y)
    if ubicacion_fila == None or ubicacion_columna == None:
        return juego
    
    grilla = juego['grilla']

    
    if juego['turno'] == True:
        '''
        Jugada valida, cuando la casilla esta vacia.
        Jugada invalida, cuando la casilla ya tiene un valor. X - O
        '''
        
        if not hay_jugada(grilla, ubicacion_fila, ubicacion_columna):
            grilla[ubicacion_fila][ubicacion_columna] = CRUZ
            juego['turno'] = False
            juego['jugador'] = CIRCULO
            print(grilla)
    else:
        '''
        Si la casilla ya tiene una jugada entonces no de puede
        sobreponer una jugada
        '''
        if not hay_jugada(grilla, ubicacion_fila, ubicacion_columna):
            grilla[ubicacion_fila][ubicacion_columna] = CIRCULO
            juego['turno'] = True
            juego['jugador'] = CRUZ
            print(grilla)
    
         
    
    
    return juego


def juego_mostrar(juego):
    """Actualizar la ventana"""
    #gamelib.draw_text('5 en línea', 150, 20)

    '''LO QUE HAGO YO'''
    grilla = juego['grilla']
    for linea in range (0,301,30):

        gamelib.draw_line(linea,0,linea,300)
        gamelib.draw_line(0,linea,300,linea)

    for f in range(10):
        for c in range(10):
            x , y = detectar_centro_interfaz(f,c)
            gamelib.draw_text(f"{grilla[f][c]}", x, y )
    
    gamelib.draw_text(f'Es turno de: {juego["jugador"]}', 150, 320) # si hacemos click aca ce cierra y da error


def main():
    gamelib.title(TITLE) # Esto le pone el titulo a la ventana
    juego = juego_crear()

    # Ajustar el tamaño de la ventana
    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)

    # Mientras la ventana esté abierta:
    while gamelib.is_alive():
        # Todas las instrucciones que dibujen algo en la pantalla deben ir
        # entre `draw_begin()` y `draw_end()`:
        gamelib.draw_begin()
        juego_mostrar(juego)
        gamelib.draw_end()

        # Terminamos de dibujar la ventana, ahora procesamos los eventos (si el
        # usuario presionó una tecla o un botón del mouse, etc).

        # Esperamos hasta que ocurra un evento
        ev = gamelib.wait()

        if not ev:
            # El usuario cerró la ventana.
            break

        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            # El usuario presionó la tecla Escape, cerrar la aplicación.
            break

        if ev.type == gamelib.EventType.ButtonPress:
            # El usuario presionó un botón del mouse
            x, y = ev.x, ev.y # averiguamos la posición donde se hizo click

            juego = juego_actualizar(juego, x, y)

gamelib.init(main)
