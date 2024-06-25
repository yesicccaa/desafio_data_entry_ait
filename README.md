# AIT Solutions

## Desafío Técnico - Data Entry

¡Hola y bienvenido/a al desafío técnico para el puesto de Data Entry! Este ejercicio está diseñado para evaluar tus habilidades en Python, Selenium y SQL. A continuación, encontrarás los pasos y requerimientos del desafío. Lee atentamente y sigue las instrucciones para completarlo con éxito.

## Introducción

En este desafío, deberás automatizar la descarga y procesamiento de listas de precios de distintos proveedores, limpiar y transformar los datos, y finalmente, actualizar una base de datos con la información procesada. El objetivo es evaluar tu capacidad para trabajar con herramientas de automatización, procesamiento de datos y bases de datos.

El repositorio del proyecto se encuentra en [GitHub](https://github.com/elianagarcia5/desafio_data_entry_ait).

## Objetivo General

Implementar el código Python necesario que realice las siguientes tareas:

1. Descarga de listas de precios de proveedores desde una página web.
2. Procesamiento y limpieza de las listas de precios.
3. Generación de archivos .xlsx con información consolidada.
4. Envío de las listas de precios procesadas a una API.
5. (Opcional) Actualización de una base de datos SQL con la información de las listas.

## Requisitos

- **Python**: el código que desarrolles debe estar escrito en Python y debe poder ejecutarse de forma local.
- **Bibliotecas**: Utilizar bibliotecas estándar de Python y cualquier otra biblioteca necesaria que consideres adecuada.

Para completar el desafío, deberás hacer un fork del repositorio de GitHub y subir tu solución. Incluye todos los archivos que consideres necesarios y agrega un archivo README.md con las respuestas de las preguntas a desarrollar. Además, se valora la inclusión de instrucciones claras para que el evaluador pueda probar la implementación.

## Criterios de Evaluación

- Eficiencia y claridad en el procesamiento de datos con Python.
- Correcta utilización de herramientas para automatización y procesamiento de datos.
- Documentación y claridad en la presentación del código.
- Registro de logs y/o mensajes que indiquen el estado y avance de la ejecución del código.
- Manejo de errores y excepciones.
- Buenas prácticas de programación y comentarios.
- Creatividad en la solución y optimización del proceso.

## Consignas

### Primera Parte: Automatización

#### Descarga de Listas de Precios

Deberás ingresar a la siguiente página web [Desafío Data Entry Front](https://desafiodataentryfront.vercel.app/) que tiene un listado de 3 proveedores de autopartes. Cada proveedor tiene un enlace para descargar su lista de precios. Tu tarea es descargar las listas de precios de todos los proveedores.

Para obtener la lista de algunos proveedores es necesario iniciar sesión en la página, utiliza las siguientes credenciales:

- **Usuario**: desafiodataentry
- **Contraseña**: desafiodataentrypass

#### Procesamiento de Listas de Precios

Las listas de precios descargadas tendrán diferentes formatos y estructuras. Tu objetivo es procesarlas y realizar todas las operaciones necesarias para obtener un formato estándar.

El resultado final de descargar y procesar cada lista de precios debe ser un archivo .xlsx con las siguientes características:

- **Nombre del archivo**: nombre del proveedor + fecha de hoy.
- **Columnas**: CODIGO, DESCRIPCION, MARCA, PRECIO.

##### Notas:

- La columna PRECIO debe usar un punto (.) como separador de decimales, y ningún separador de miles.
- La columna DESCRIPCION debe tener un máximo de 100 caracteres.
- La columna DESCRIPCION debe ser la combinación de las columnas “Descripción” y “Rubro” de la lista original del proveedor Mundo RepCar.
- La lista del proveedor Autofix se descarga con una hoja por cada Marca seleccionada en la página. Se deberán descargar todas las marcas y unificarlas en una misma hoja de cálculo. Además, se debe agregar la columna MARCA a cada artículo según el nombre de la hoja en la que se encontraba el mismo.

#### Subida de Listas a una API

Una vez que se procesan las listas de precios y se obtienen los archivos .xlsx finales, debes enviarlos a un endpoint de una API mediante una request POST.

- **URL de la API**: https://desafio.somosait.com/api/upload/
- El archivo se debe subir utilizando una request form-data con el nombre "file".
- La API analizará el archivo subido para validar que al menos estén presentes las columnas CODIGO, DESCRIPCIÓN, MARCA y PRECIO. En caso de que falte alguna de las columnas, se recibirá una respuesta con un error 400 y el mensaje "Missing required columns".
- La API realizará la subida de la lista a Google Drive. En caso de que la subida sea exitosa, se recibirá una respuesta con status 200 y el link de Google Drive para acceder al archivo subido.

##### Ejemplo de respuesta de la API:

```json
{
  "link": "https://docs.google.com/spreadsheets/d/16x-vqqjgT_URIbasRn2RTqbGCzeCbQhf6qOjYtYdzew/edit?usp=sharing"
}
```

### Segunda Parte: SQL

En el repositorio encontrarás un archivo .sql para que puedas crear una base de datos “DesafioDataEntry” con varias tablas y datos. La base de datos tiene las siguientes tablas:

- **Repuesto**: id, codigo, descripción, id_marca, precio, proveedor_id, id_ultima_actualizacion.
- **Proveedor**: id, nombre.
- **Actualización**: id, fecha, id_proveedor.
- **Marca**: id, nombre.

#### Tareas

1. Crear la base de datos a partir del script SQL del repositorio.
2. Implementar las sentencias SQL que cumplan con cada ítem a continuación:
   - Obtener todos los Repuestos del Proveedor Autofix cuyo precio no se haya actualizado en el último mes.
   - Actualizar los Repuestos de las Marcas “ELEXA”, “BERU”, “SH”, “MASTERFILT” y “RN” realizando un incremento del 15% en sus precios.
   - Obtener el promedio de precios de los repuestos por cada marca.
   - Obtener los repuestos que no tienen una descripción asignada (descripción es NULL o vacía).
   - Contar el número de repuestos de cada proveedor y mostrar sólo aquellos proveedores que tienen al menos 1000 repuestos.
   - Obtener el repuesto más caro de cada proveedor.
   - Aplicar un recargo del 30% en los artículos de los proveedores AutoRepuestos Express y Automax cuyo precio sea mayor a $50000 y menor a $100000.

### BONUS: Subida de Listas a la Base de Datos

Esta consigna es opcional pero suma puntos para valorar tu perfil. El objetivo es cargar los artículos de las listas de precios procesadas en la primera parte del desafío en la base de datos de la segunda parte del desafío. Debes desarrollar el código necesario para procesar los archivos .xlsx generados y actualizar la base de datos SQL, realizando las siguientes actualizaciones en la misma:

- Agregar los repuestos nuevos que no estén en la base de datos. Se debe indicar el codigo, descripción, marca, precio, proveedor y última actualización.
- Actualizar el precio de los repuestos existentes para que coincidan con el de la lista de precios.

Siéntete libre de modificar la estructura de la base de datos si lo crees necesario, siempre y cuando se cumpla con el objetivo de la consigna.

¡Buena suerte y esperamos tu solución!
