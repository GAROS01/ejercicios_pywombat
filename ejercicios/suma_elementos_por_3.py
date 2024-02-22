"""
Desarrolla un script el cual permita la lectura de un número entero (n) e imprima en consola el resultado de n + (n * n) + (n * n * n)

Ejemplo.

Ingresa un número: 2
El resultado de la operación es: 14

Ingresa un número: 20
El resultado de la operación es: 8420
"""


def suma(numero):
    resultado = numero + (numero * numero) + (numero * numero * numero)
    print(resultado)


suma(numero=20)
