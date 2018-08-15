import pyglet
import recursos, cargar,jugador

batch_principal = pyglet.graphics.Batch()

ventana_juego = recursos.ventana_juego
nave_jugador = pyglet.sprite.Sprite(img=recursos.nave_imagen,x=400,y=300)
asteroides  = cargar.asteroides(5,nave_jugador.position,batch_principal)


nave_jugador = jugador.Jugador(x=400, y=300,batch=batch_principal);
objetos_juego = [nave_jugador] + asteroides
ventana_juego.push_handlers(nave_jugador)




@ventana_juego.event
def on_draw():
    ventana_juego.clear()
   
    batch_principal.draw()


def actualizar(dt):
    for obj in objetos_juego:
        #print(obj.nombre)
        obj.actualizar(dt)
    #Funcion que agrega objetos a lista para posterio comparacion
    for i in range(len(objetos_juego)):
        for j in range (i+1,len(objetos_juego)):
            #objeto1 = objetos_juego[i]
            objeto2 = objetos_juego[j]
    objeto1 = objetos_juego[0]
    objeto1.colision_con(objeto2)
       
    ##print(objeto2.nombre)
    ##print(objeto1.nombre)  
    
    


if __name__ == '__main__':
    
    pyglet.clock.schedule_interval(actualizar,1/120.0)
    pyglet.app.run()
        