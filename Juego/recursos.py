import pyglet


ventana_juego = pyglet.window.Window()

pyglet.resource.path = ['../recursos']
pyglet.resource.reindex()

nave_imagen = pyglet.resource.image("Nave.png")
asteroide_imagen = pyglet.resource.image("Asteroide.png")
llama_imagen = pyglet.resource.image("LlamaMotor.png")
bala_imagen = pyglet.resource.image("Bala.png")

def centroImagen(imagen):
    imagen.anchor_x = imagen.width // 2
    imagen.anchor_y = imagen.height // 2
centroImagen(nave_imagen)
centroImagen(asteroide_imagen)
centroImagen(llama_imagen)
centroImagen(bala_imagen)

puntos_etiqueta = pyglet.text.Label(text="Punto: 0",x=10,y=575)
nivel_etiqueta = pyglet.text.Label(text="Asteroides",
                                   x=400,y=575,anchor_x ='center')




