import pyglet, math

def distancia(punto_1=(0,0),punto_2=(0,0)):
    return math.sqrt(
        (punto_1[0]- punto_2[0]) ** 2 + 
        (punto_1[1]- punto_2[1]) ** 2)

