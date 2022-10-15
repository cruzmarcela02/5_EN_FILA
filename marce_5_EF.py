ANCHO_VENTANA = 300
ALTO_VENTANA = 300
SIZE = 300
TITLE = '5 EN FILA'
VACIO = ' '
CRUZ = 'X'
CIRCULO = 'O'
import gamelib


def juego_crear():
    """Inicializar el estado del juego"""
    juego = []
    for f in range(10):
        fila = []
        for c in range (10):
            fila.append('')
        
        juego.append(fila)
    return juego

def clonar_grilla(juego):
    '''Clonamos la la grilla de 10 x 10'''
    juego_clon = []
    for fila in juego:
        fila_clon = []
        for caracter in fila:
            fila_clon.append(caracter)
        juego_clon.append(fila_clon)
    return juego_clon


def mostrar_contenido():
    grilla = juego_crear()
    for fila in grilla:
        print(fila)
    #return grilla

#juego_crear()
#mostrar_contenido()




'''NO TE PODES OLVIDAR COMO VER RESULTADOS LPM'''
def numeros():
    for n in range(10):
        print(n)

#numeros() # printea del 0 al 9 -> 0123456789



'''
DISENO DE TABLERO - INTERFAZ
'''

def juego_mostrar(juego):
    """Actualizar la ventana"""
    gamelib.draw_text('5 en línea', 150, 20)
    dim = len(juego)
    for dimension in range (dim): #10
        gamelib.draw_line(dim * 30, 0, dim, 300) #Linea Vertical
        gamelib.draw_line(0, dim * 30, 300, dim) #Linea Horizontal
#gamelib.init(juego_mostrar(juego))

def detectar_posicion2(x,y):
    Jugada = 'X'
    grilla = juego_crear()
    if (x != y) and (0 <= x < 300) and (0 <= y < 300):
        posicion_f = x // 30
        posicion_c = y // 30
        grilla[posicion_f][posicion_c] = Jugada
    return grilla

#print(detectar_posicion2(150,150))

def detectar_posicion(x,y):

    if (x != y) and (0 <= x < 300) and (0 <= y < 300):
        posicion_f = x // 30
        posicion_c = y // 30
    return posicion_f, posicion_c # retorna en forma de tupla

#print(detectar_posicion(160,250))
















def juego_actualizar(juego, x, y):
    """Actualizar el estado del juego

    x e y son las coordenadas (en pixels) donde el usuario hizo click.
    Esta función determina si esas coordenadas corresponden a una celda
    del tablero; en ese caso determina el nuevo estado del juego y lo
    devuelve.
    """
    # En caso de y sea mayo a 300 no esta en el tablero por ende no afecta el juego
    if y > 300:
        return juego
    
    '''
    Obtenemos las coordenadas de la casilla a jugar
    '''
    if y < 300 and x < 300:
        #Traemos la ubicacion del click para una casilla
        ubi_fila , ubi_col = detectar_posicion(x,y)
    '''
    Si la casilla ya tiene una jugada entonces no de puede
    sobreponer una jugada
    '''
    if juego[ubi_fila][ubi_col] == VACIO:
        juego[ubi_fila][ubi_col] == CRUZ # en realidad va una jugada que va rotando
    

    
    

    '''
    Verificamos si hay algo en esa posicion, de haber alguna jugada devolveremos la casilla
        if juego[ubi_fila][ubi_col] == CRUZ or juego[ubi_fila][ubi_col] == CIRCULO:
            return juego
    '''
     


    return juego

