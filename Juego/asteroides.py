import pyglet

ventana_juego = pyglet.window.Window()

pyglet.resource.path = ['../recursos']
pyglet.resource.reindex()

nave_imagen = pyglet.resource.image("Nave.png")

def centroImagen(imagen):
    imagen.anchor_x = imagen.width // 2
    imagen.anchor_y = imagen.height // 2

centroImagen(nave_imagen)

puntos_etiqueta = pyglet.text.Label(text="Punto: 0",x=10,y=575)
nivel_etiqueta = pyglet.text.Label(text="Asteroides",
                                   x=400,y=575,anchor_x ='center')




@ventana_juego.event
def on_draw():
    #ventana_juego.clear()
    puntos_etiqueta.draw()
    nivel_etiqueta.draw()
    

##if __name__ == '__main__':
   ## pyglet.app.run()
pyglet.app.run()


   
if not objeto1.muerto and not objeto2.muerto:
    if objeto1.colision_con(objeto2):
        objeto1.manejador_colision_con(objeto2)
        objeto2.manejador_colision_con(objeto1)
for para_remover in [obj for obj in objetos_juego if obj.muerto]:
    #para_remover.borrar()
    objetos_juego.remove(para_remover)