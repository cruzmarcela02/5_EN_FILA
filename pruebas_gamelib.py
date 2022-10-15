from turtle import color
import gamelib
'''
    Functions de gamelib
'''

# 1 Dibujar cosas
def dibuja_un_poligono():
    gamelib.resize(300,300)
    #gamelib.draw_begin()
    gamelib.draw_rectangle(120,170,170,120, fill='blue')
    #gamelib.draw_end()
    gamelib.wait(gamelib.EventType.KeyPress)

    #while gamelib.is_alive(): # Devuelve True si la pestana esta abierta
    while gamelib.loop():

        for event in gamelib.get_events():
            if event.type == gamelib.EventType.KeyPress and event.key == 'q':
                gamelib.draw_begin()
                gamelib.draw_rectangle(120,170,170,120, fill = 'red')
                gamelib.draw_end()
gamelib.init(dibuja_un_poligono) # inicializa gamelib