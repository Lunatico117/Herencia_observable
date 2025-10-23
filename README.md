# Ejercicio de Práctica – Clases y herencia con MVVM y Firebase

## Descripción
Este proyecto es un ejercicio de práctica para aplicar varios conceptos de programación y arquitectura de software. Consiste en un sistema de registro y visualización de animales utilizando Python y Firebase Realtime Database.

## Conceptos y prácticas aplicadas
- **Clases y herencia:** Se crearon una clase padre `Animal` y subclases `Gato`, `Pollito` y `Oveja`, cada una con su propio comportamiento.  
- **MVVM (Model-View-ViewModel):** La lógica del programa se organizó siguiendo la arquitectura MVVM para separar la vista, la lógica de negocio y el manejo de datos.  
- **Observable:** Se implementó un observable para notificar automáticamente a la vista cuando la lista de animales cambia.  
- **Firebase Realtime Database:** Se guardan y recuperan los datos de los animales desde Firebase, permitiendo persistencia de la información en la nube.

## Funcionalidades
- Agregar animales (Gato, Pollito, Oveja) con nombre y edad.  
- Mostrar la lista completa de animales guardados en Firebase.  
- Cada animal puede realizar su sonido característico.

## Tecnologías utilizadas
- Python 3.x  
- Firebase Realtime Database  
- Biblioteca `firebase_admin` para la conexión con Firebase  

## Evidencia de funcionamiento a través de la terminal
En la siguiente imagen se puede ver la creación de un objeto `Gato` con sus atributos:
<img width="322" height="219" alt="Creación de un gato en la terminal" src="https://github.com/user-attachments/assets/6f70953d-0e90-4bfe-ae3e-3fb41f5e4de3" />

## Evidencia de base de datos a través de la terminal
En la siguiente imagen se puede ver los datos guardados en Realtime Database en la terminal
<img width="436" height="202" alt="image" src="https://github.com/user-attachments/assets/9786d6fd-1787-4584-8068-0f3a7e91e26b" />

## Evidencia de base de datos en Firebase
En la siguiente imagen se puede ver los datos guardados en Realtime Database en Firebase 
<img width="531" height="343" alt="image" src="https://github.com/user-attachments/assets/7c4cecfd-0305-4c28-b605-36970458c12e" />




