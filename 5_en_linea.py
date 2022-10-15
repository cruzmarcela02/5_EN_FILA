import re
import gamelib

ANCHO_VENTANA = 300
ALTO_VENTANA = 340
SIZE = 300
TITLE = '5 EN FILA'
VACIO = ''
CRUZ = 'X'
CIRCULO = 'O'
turno_x = True

'''
Diseno del grilla 10 x 10 
Lista de lista de cadenas
[
    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
]
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
        'tablero' : grilla,
        'turno': turno_jugador,
        'jugador': CRUZ,
    }
    
    return mi_juego


def detectar_posicion(x,y):

    if  (0 <= x < 300) and (0 <= y < 300):
        posicion_columna = x // 30 
        posicion_fila = y // 30 
    return posicion_fila, posicion_columna # retorna en forma de tupla


def hay_jugada(juego, posicion_fila, posicion_columna):
    '''Devolvera True si hay X - O, si no hay nada devuelve False -- (juego,x,y)'''
    #pos_x , pos_y = detectar_posicion(x,y)
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
    
    '''
    Jugada valida, cuando la casilla esta vacia.
    ------invalida, cuando la casilla ya tiene un valor. X - O
    '''
    grilla = juego['tablero']
    
    if juego['turno'] == True:
        
        if not hay_jugada(grilla, ubicacion_fila, ubicacion_columna):
            grilla[ubicacion_fila][ubicacion_columna] = CRUZ
            juego['turno'] = False
            juego['jugador'] = CIRCULO
            print(grilla)
    else:

        if not hay_jugada(grilla, ubicacion_fila, ubicacion_columna):
            grilla[ubicacion_fila][ubicacion_columna] = CIRCULO
            juego['turno'] = True
            juego['jugador'] = CRUZ
            print(grilla)
    
         
    
    
    '''
    Si la casilla ya tiene una jugada entonces no de puede
    sobreponer una jugada
    '''
    
    

    return juego


def juego_mostrar(juego):
    """Actualizar la ventana"""
    #gamelib.draw_text('5 en línea', 150, 20)

    '''LO QUE HAGO YO'''
    grilla = juego_crear() 
    for linea in range (0,301,30):

        gamelib.draw_line(linea,0,linea,300)
        gamelib.draw_line(0,linea,300,linea)
    
    
    
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
