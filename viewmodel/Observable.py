
class ListaAnimalesObservable:
    def __init__(self, animales_iniciales=None):
        # La lista de animales que se va a observar
        self._lista_animales = animales_iniciales or []
        # Los observadores (callbacks que serán notificados)
        self._observadores = []
    # Registra una función que quiere recibir actualizaciones.
    def agregar_observador(self, funcion_observadora):
        # Agrega una función que se ejecutará cada vez que cambie la lista.
        self._observadores.append(funcion_observadora)

    @property
    def animales(self):
        # Devuelve la lista actual de animales.
        return self._lista_animales

    @animales.setter
    def animales(self, nueva_lista):
        # Actualiza la lista y notifica a los observadores.
        self._lista_animales = nueva_lista
        for observador in list(self._observadores):
            observador(nueva_lista)
