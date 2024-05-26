import gc
class Nodo:
    def __init__(self,valor):
        self.valor = valor
        self.siguiente = None
        
        
#!Referencia cíclica:
a = Nodo(1)
b = Nodo(2)
a.siguiente = b
b.siguiente = a

#TODO Elimino referencias
del a
del b

gc.collect()