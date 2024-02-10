"""
Dado un año específico por el usuario en consola, cree la lógica para verificar si el año es bisiesto o ordinario. En la salida debe mostrar ¡Año bisiesto! en caso de que lo sea, y ¡Año ordinario! si no lo es.

Pista:

Tenga en cuenta que los años bisiesto son divisibles por 4 pero no por 100, o si es divisible por 400.

Ejemplo:

Entrada:

Año: 2021

Salida:

¡Año ordinario!

Entrada:

Año: 2000

Salida:

¡Año bisiesto!
"""

year = int(input("Ingrese un año: "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f"El año {year} es bisiesto")
else:
    print(f"El año {year} no es bisiesto")
