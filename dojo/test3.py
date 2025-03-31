# Test rápido de Python #3
# -----------------------------------------------
# ¿Sabes qué imprime este código?

# Código:
def f(x=[]):
    x.append(1)
    return x

print(f())
print(f())

# Opciones:
# A) [1] [1]
# B) [1] [1, 1]
# C) [1, 1] [1, 1, 1]

# 👇👇👇 SPOILER: no sigas bajando si no quieres ver la respuesta 👇👇👇

































































































































"""
Respuesta correcta: B) [1] [1, 1]

Explicación:
En Python, los valores por defecto de los parámetros de una función se evalúan una sola vez, en el momento en que la función es definida, no cada vez que se llama.

En este caso, el valor por defecto del parámetro x es una lista vacía: x=[]

La primera vez que llamas f(), se usa esa lista vacía, se le agrega un 1 con append, y se retorna la lista resultante: [1]

La segunda vez que llamas f(), no se crea una nueva lista, sino que se reutiliza la misma lista que ya tenía un 1 dentro. Por eso, se agrega otro 1, resultando en [1, 1]

Este comportamiento puede parecer confuso o incluso un error, pero es completamente intencional en Python. Es muy importante tenerlo en cuenta al definir funciones con valores por defecto mutables como listas o diccionarios.

Consejo práctico:
Si necesitas que una función tenga un parámetro que comience siempre con una nueva lista vacía, es mejor usar None como valor por defecto y luego asignar la lista dentro de la función. Así:

    def f(x=None):
        if x is None:
            x = []
        x.append(1)
        return x

Este patrón evita el uso compartido accidental del mismo objeto entre llamadas.
"""
