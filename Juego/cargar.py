import pyglet
import recursos
import random
import math
import objetofisico
import utiles


def asteroides(num_asteroides,posicion_jugador, batch=None):
    asteroides = []
    for i in range(num_asteroides):
        asteroide_x,asteroide_y = posicion_jugador
        while utiles.distancia((asteroide_x,asteroide_y),posicion_jugador) < 100:
            asteroide_x = random.randint(0,800)
            asteroide_y = random.randint(0,600)            
        nuevo_asteroide = objetofisico.ObjetoFisico(img=recursos.asteroide_imagen,
                                               x=asteroide_x,y=asteroide_y,batch=batch)
        nuevo_asteroide.nombre = "Asteroide" + str(i) 
        nuevo_asteroide.rotation = random.randint(0,360)
        nuevo_asteroide.velocidad_x = random.random()*40
        nuevo_asteroide.velocidad_y = random.random()*40
        asteroides.append(nuevo_asteroide)
    return asteroides

        