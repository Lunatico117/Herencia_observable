# Esto carga las variables de entorno para interactuar con el sistema operativo
import os
from dotenv import load_dotenv 
# Autenticación y acceso a Firebase Realtime Database                
import firebase_admin
from firebase_admin import credentials, db
# Importamos nuestras subclases de Animal
from model.Gato import Gato                     
from model.Pollito import Pollito
from model.Oveja import Oveja
# Nuestro observable para la lista de animales
from viewmodel.Observable import ListaAnimalesObservable  

class AnimalViewModel:
    def __init__(self):
        # Cargar las variables definidas en .env (FIREBASE_KEY_PATH y FIREBASE_DB_URL)
        load_dotenv()
        firebase_key_path = os.getenv("FIREBASE_KEY_PATH")  # Ruta a la clave privada JSON
        firebase_db_url = os.getenv("FIREBASE_DB_URL")      # URL de la base de datos

        # Se inicializa el Firebase usando la clave privada y el URL
        cred = credentials.Certificate(firebase_key_path)
        if not firebase_admin._apps:  # Evita inicializar varias veces si ya estaba inicializado
            firebase_admin.initialize_app(cred, {"databaseURL": firebase_db_url})

        # Creamos una referencia a la ruta "/animales" en Firebase
        self.animales_ref = db.reference("/animales")

        # Creamos el observable que mantendrá la lista de animales y notificará cambios
        self.animales_observable = ListaAnimalesObservable()

    def agregar_animal(self, tipo, nombre, edad):
        # Dependiendo del tipo, creamos la instancia correspondiente
        if tipo.lower() == "gato":
            animal = Gato(nombre, edad)
        elif tipo.lower() == "pollito":
            animal = Pollito(nombre, edad)
        elif tipo.lower() == "oveja":
            animal = Oveja(nombre, edad)
        else:
            # Manejo de error si el tipo es inválido
            raise ValueError("Tipo de animal no reconocido")  

        # Guardamos el animal en Firebase
        self.animales_ref.push({
            "tipo": tipo,
            "nombre": animal.nombre,
            "edad": animal.edad,
            "sonido": animal.hacer_sonido()
        })

        
        # Actualizamos la lista en el observable
        nueva_lista = self.animales_observable.animales + [animal]
        self.animales_observable.animales = nueva_lista  # Esto dispara la notificación a la vista


    def obtener_animales_desde_firebase(self):
 
        snapshot_animales = self.animales_ref.get()  # Obtiene todos los registros de la ruta '/animales' en Firebase

        lista_animales_objetos = []  # Lista vacía donde se almacenarán las instancias de animales

        if snapshot_animales:  # Verifica si hay datos en la base
            for datos_animal in snapshot_animales.values():  # Recorremos cada registro de Firebase
                tipo_animal = datos_animal.get("tipo", "").lower()  # Tipo de animal en minúscula
                nombre_animal = datos_animal.get("nombre", "")      # Nombre del animal
                edad_animal = datos_animal.get("edad", 0)           # Edad del animal

                # Crear la instancia correspondiente según el tipo
                if tipo_animal == "gato":
                    animal_objeto = Gato(nombre_animal, edad_animal)
                elif tipo_animal == "pollito":
                    animal_objeto = Pollito(nombre_animal, edad_animal)
                elif tipo_animal == "oveja":
                    animal_objeto = Oveja(nombre_animal, edad_animal)
                else:
                    continue  # Ignora tipos desconocidos

                lista_animales_objetos.append(animal_objeto)  # Añade el objeto a la lista

        return lista_animales_objetos  # Devuelve la lista de objetos Animal
