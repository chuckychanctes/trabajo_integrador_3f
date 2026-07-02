# Trabajo Integrador – Python
Este repositorio contiene mis dos mini aplicaciones hechas para la materia Introducción a Python – TECNO 3F.

## Aplicación 1: Tickets (Obligatoria)
¿Qué hace?
* Es un sistema muy básico para crear y leer tickets.
* Sirve como ejemplo de cómo guardar datos en memoria y mostrarlos después.

## Cómo funciona
Al iniciar, aparece un menú con 3 opciones:

* Generar un nuevo ticket
* Leer un ticket
* Salir

## Cuando genero un ticket, me pide:
- Nombre
- Sector
- Asunto
- Mensaje

* El programa le asigna un número aleatorio entre 1000 y 9999.
* Ese número hay que recordarlo para poder leer el ticket después.
* Si elijo leer ticket, escribo el número y me muestra los datos guardados.
* Si pongo salir, me pide confirmación y termina.

### Ejemplo de uso
* Código
Hola, bienvenido al sistema de Tickets
- 1 - Generar un Nuevo Ticket
- 2 - Leer un Ticket
- 3 - Salir
- Seleccione: 1

- Ingrese su Nombre: Gabriel
- Ingrese su Sector: Tecno3f
- Ingrese el Asunto: Pc
- Ingrese el Mensaje: No enciende la pc

* Se generó el siguiente Ticket:
- Nº Ticket: 6694
- Recordar su número de Ticket

## Aplicación 2: Generador de Contraseñas (Optativa)
* ¿Qué hace?
Genera contraseñas aleatorias según lo que el usuario elija.

* Cómo funciona
Aparece un menú con opciones:

Solo letras
Solo números
Letras y números
Letras, números y caracteres especiales
Salir

* Elijo una opción y me devuelve una contraseña de 8 caracteres (por defecto).
* Puedo repetir las veces que quiera.

Ejemplo de uso
Código
--- Generador de Contraseñas ---
1. Solo letras
2. Solo números
3. Letras y números
4. Letras, números y caracteres especiales
0. Salir
Seleccione una opción: 3

Contraseña generada: a9B7k2Qx

## Cómo ejecutar
Clonar el repositorio o descargarlo.
Entrar a la carpeta de cada aplicación:
Tickets/main.py
Password/main.py

## Ejecutar con Python:
Código
python main.py

## Notas
Todo está hecho con lo básico de Python, sin librerías externas.
Los tickets se guardan solo mientras el programa está abierto (no se usan archivos ni bases de datos).
El generador de contraseñas usa el módulo random y string que vienen con Python.