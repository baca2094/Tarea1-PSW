# Tarea1-PSW

## Información del estudiante

**Nombre:** Branco Antonio Catalán Arrué <br/>
**Correo:** branco.catalan.13@sansano.usm.cl

## Instalación

La función a ejecutar se encuentra en un archivo .py, por lo cual no necesita una instalación previa, solamente encontrarse en el mismo proyecto o carpeta del "main" que lo utilizará. Al tratarse de un archivo .py se necesitará, evidentemente, tener python instalado (en lo posible python3). Las pruebas fueron llevadas en ambiente Linux, por lo cual en base a esto se realizará la explicación siguiente.

## Instrucciones de uso

La función se debe importar desde otro archivo o desde la terminal. La manera de probarlo fue a través de otro archivo .py que leía un archivo .txt que contenía los Strings de prueba junto a su respuesta correcta, pero la explicación de uso se llevará a cabo pensando en la ejecución de python3 desde la terminal.

1. Abrir terminal ojalá en la misma carpeta donde se encuentre el archivo Tarea1BACA.py.
2. Ejecutar python3 (el comanso es el mismo, "python3").
3. Importar la función (o el archivo completo, como se desee) *compareStrings*.
4. Para utilizar desde consola se pueden usar dos variables (que sean strings) o bien escribir los strings explícitamente dentro de la función. Por ejemplo:

```
braulio@braulio-VirtualBox: ~/Documentos/Tarea1_PSW$ python3
Python 3.8.2 (default, Jul 16 2020, 14:00:26)
[GCC 9.3.0] on linux
Type "help", copyright", "credits" or "license" for more information.
>>> from Tarea1BACA import compareStrings
>>> compareStrings("Esta frase es corta", "Esta frase es más larga")
'Esta frase es más larga'
>>> a = "Esta frase debería ser más larga"
>>> b = "Esta frase es más corta"
>>> compareStrings(a,b)
'Esta frase debería ser más larga'
```
