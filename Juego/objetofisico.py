import pyglet
import utiles
class ObjetoFisico(pyglet.sprite.Sprite):
    nonbre = "nombre"
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.velocidad_x , self.velocidad_y = 0.0,0.0
        self.muerto = False
    
    def colisiones(self):
        min_x = -self.image.width / 2
        min_y = -self.image.height / 2
        max_x = 800 + self.image.width / 2
        max_y = 600 + self.image.height / 2
        if self.x < min_x:
            self.x = max_x
        elif self.x > max_x:
            self.x = min_x
        if self.y < min_y:
            self.y = max_y
        elif self.y > max_y:
            self.y = min_y    
        
    def actualizar(self,tiempoDelta):
        self.x += self.velocidad_x * tiempoDelta
        self.y += self.velocidad_y * tiempoDelta
        self.colisiones()
        
    
    #Colisiones
    def colision_con(self, otro_objeto):
        distancia_colision = self.image.width/2 + otro_objeto.image.width/2
        distancia_actual = utiles.distancia(
            self.position,
            otro_objeto.position)
        colisiono = (distancia_actual <= distancia_colision)
        if colisiono:
            print(self.nonbre + " con " + otro_objeto.nombre) 
        return colisiono
    
    def manejador_colision_con(self,otro_objeto):
        self.muerto = True
        print("Muerto")
    
        