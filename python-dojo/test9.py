# Test rápido de Python #9
# -----------------------------------------------
# ¿Cuál es el resultado de este código?

# Código:
print("".join(["a", "b", "c"]))

# Opciones:
# A) ["a", "b", "c"]
# B) "abc"
# C) "a b c"

# 👇👇👇 SPOILER: no sigas bajando si no quieres ver la respuesta 👇👇👇

































































































































"""
Respuesta correcta: B) "abc"

Explicación:
El método `.join()` en Python se usa para unir elementos de una lista (o cualquier iterable) 
en un solo string, utilizando como separador el string que invoca el método.

Su sintaxis general es:

    separador.join(lista)

En este caso:

    "".join(["a", "b", "c"])

Aquí, el separador es un string vacío (""), lo que significa que los elementos de la lista 
se van a unir sin nada entre ellos. Por lo tanto, se forma el string:

    "abc"

Veamos algunos ejemplos adicionales para entenderlo mejor:

    "-".join(["a", "b", "c"])   →  "a-b-c"
    " ".join(["hola", "mundo"]) → "hola mundo"
    "_".join(["1", "2", "3"])   → "1_2_3"

Consejo práctico:

`.join()` solo funciona con elementos que ya son strings. Si intentas pasarle una lista de enteros, 
obtendrás un error. Por ejemplo:

    "".join([1, 2, 3])  → TypeError

En ese caso, debes convertir los elementos a string primero:

    "".join(str(x) for x in [1, 2, 3])  → "123"

Este método es especialmente útil cuando necesitas transformar listas en cadenas, 
como al construir mensajes, procesar texto, o crear expresiones en formatos como CSV.
"""