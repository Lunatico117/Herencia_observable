#Esto trae la clase madre para heredarla
from model.Animal import Animal


class Pollito(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        self.tipo = "pollito"

    def hacer_sonido(self):
        return "Pio pio!"