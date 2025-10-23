# Importamos el ViewModel
from viewmodel.AnimalViewModel import AnimalViewModel  

# Función que se ejecuta para ver la lista de animales
def mostrar_animales_desde_firebase(animal_viewmodel):
    lista_animales = animal_viewmodel.obtener_animales_desde_firebase()  # Pedimos la lista al ViewModel

    if not lista_animales:  # Si la lista está vacía
        print("No hay animales registrados en Firebase.")
        return

    print("Lista de animales desde Firebase:")  
    for animal in lista_animales:  # Recorre cada objeto Animal
        print(f" - El {animal.tipo} {animal.nombre}, tiene {animal.edad} años y dice: ({animal.hacer_sonido()})")


# Función que se ejecuta cada vez que cambia la lista de animales
def mostrar_lista_actualizada(animales):
    print("\nLista actualizada:")
    for animal in animales:
        # Mostramos nombre y sonido de cada animal
        print(f" - El {animal.tipo} {animal.nombre}, tiene {animal.edad} años y dice: ({animal.hacer_sonido()})")

def ejecutar_vista():
    # Creamos la instancia del ViewModel
    vm = AnimalViewModel()
    
    # Nos suscribimos al observable para que llame a mostrar_lista_actualizada cada vez que cambie la lista
    vm.animales_observable.agregar_observador(mostrar_lista_actualizada)

    # Ciclo principal de la vista (interacción con usuario)
    while True:
        print("1. Agregar animal")
        print("2. Mostrar animales")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tipo = input("Tipo: ")
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            vm.agregar_animal(tipo, nombre, edad)
        elif opcion == "2":
            mostrar_animales_desde_firebase(vm)
        elif opcion == "3":
            break
        else:
            print("Opción inválida.")
