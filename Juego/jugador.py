import math
import pyglet
from pyglet.window import key
import objetofisico,recursos,balas
class Jugador(objetofisico.ObjetoFisico):  
    nombre = "Jugador"
    def __init__(self,*args,**kwargs):
        super().__init__(img=recursos.nave_imagen,*args,**kwargs)
        self.llama_motor = pyglet.sprite.Sprite(img=recursos.llama_imagen,*args,**kwargs)
        self.llama_motor.visible = False
        self.scale = 0.6
        self.llama_motor.scale = 0.6
        self.velocidad_bala = 700.0
        #self.bala = pyglet.sprite.Sprite(img=recursos.bala_imagen,*args,**kwargs)
    
    #Funcion que elimina el jugador con la llama_motor
    def borrar(self):
        self.llama_motor.delete()
        super(Jugador, self).delete()
    
    def Disparar(self):
        radian = -math.radians(self.rotation)
        radio_nave = self.image.width/2
        bala_x = self.x + math.cos(radian) * radio_nave
        bala_y = self.y + math.sin(radian) * radio_nave
        #Intancia la bala imagen que es un sprite porque el objeto fisico hereda de sprite
        nueva_bala = balas.Bala(x=400,y=300,batch=self.batch)
        velx = (self.velocidad_x + math.cos(radian) * self.velocidad_bala)
        vely = (self.velocidad_y + math.sin(radian) * self.velocidad_bala)
        #nueva_bala.velocidad_x = velx
        #nueva_bala.velocidad_y = vely
        print("se disparo")
        
    aceleracion = 300.0
    velocidad_rotacion = 200.0        
    teclas = dict(izq = False,der = False, arriba = False, espacio = False)
   
    #Funciones para movimiento
    def on_key_press(self,symbol,modifiers):
        if symbol == key.UP:
            self.teclas['arriba'] = True
            self.llama_motor.visible = True
        elif symbol == key.LEFT:
            self.teclas['izq'] = True            
        elif symbol == key.RIGHT:
            self.teclas['der'] = True 
        elif symbol == key.SPACE:
            self.teclas['espacio'] = True              
            
    def on_key_release(self,symbol,modifiers):
        if symbol == key.UP:
            self.teclas['arriba'] = False
            self.llama_motor.visible = False
        elif symbol == key.LEFT:
            self.teclas['izq'] = False         
        elif symbol == key.RIGHT:
            self.teclas['der'] = False
        elif symbol == key.SPACE:
            self.teclas['espacio'] = False          
            
    def actualizar(self,dt):
        super(Jugador,self).actualizar(dt)
        
        if self.teclas['izq']:
            self.rotation -= self.velocidad_rotacion * dt
        if self.teclas['der']:
            self.rotation += self.velocidad_rotacion * dt
        if self.teclas['arriba']:
            angulo_randian = -math.radians(self.rotation)
            fuerza_x = math.cos(angulo_randian) * self.aceleracion * dt
            fuerza_y = math.sin(angulo_randian) * self.aceleracion * dt
            self.velocidad_x += fuerza_x
            self.velocidad_y += fuerza_y
            self.llama_motor.visible = True
            self.llama_motor.rotation = self.rotation
            self.llama_motor.x = self.x
            self.llama_motor.y = self.y
            
        if self.teclas['espacio']:    
            self.Disparar()