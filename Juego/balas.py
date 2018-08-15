import pyglet
import recursos
import objetofisico

class Bala(objetofisico.ObjetoFisico):
    """Balas disparadas por el jugador"""
    def __init__(self, *args, **kwargs):
        super(Bala,self).__init__(recursos.bala_imagen,*args,**kwargs)
       
       
   
    