"""
Dado el siguiente string.

Title: 'Nuevo ejercicio'
Desarrolla un programa en Python que permita generar un nuevo string con todos los caracteres después de los dos puntos (:). El programa deberá imprimir en consola el nuevo string.

Ejemplo.

python main.py
'Nuevo ejercicio'
"""

texto = "Title: 'Nuevo ejercicio'"
nuevo_texto = ""
banderin = False

for i in texto:
    if i == ":":
        banderin = True
    elif banderin:
        nuevo_texto += i

print(nuevo_texto)
