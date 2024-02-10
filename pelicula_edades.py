"""
Película por edades
A partir de las siguientes especificaciones, crea la lógica para recomendar una película dependiendo de la edad dada por el usuario.

<table> <thead> <tr> <th>Rango de edad</th> <th>Película</th> </tr> </thead> <tbody> <tr> <td><= 16</td> <td>"Coco"*</td> </tr> <tr> <td>17 −− 25</td> <td>"Avengers: Endgame"</td> </tr> <tr> <td>26 −− 40</td> <td>"Matrix"</td> </tr> <tr> <td>41 −− 60</td> <td>"El libro verde"</td> </tr> <tr> <td>> 60</td> <td>"Un golpe con estilo"</td> </tr> </tbody> </table>
Ejemplo:

Entrada:

Edad: 14

Salida:

Coco

Entrada:

Edad: 28

Salida:

Matrix

"""

# Tu código va aquí
edad = int(input("Ingrese tu edad:  "))

if edad < 17:
    print("Coco")
elif edad > 16 and edad < 26:
    print("Avenger: Endgame")
elif edad > 25 and edad < 41:
    print("Matrix")
elif edad > 40 and edad < 61:
    print("El libro verde")
elif edad > 59:
    print("Un golpe con estilo")
