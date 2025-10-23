#Esto trae la clase madre para heredarla
from model.Animal import Animal

class Gato(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        self.tipo = "gato"   

    def hacer_sonido(self):
        return "Miau!"