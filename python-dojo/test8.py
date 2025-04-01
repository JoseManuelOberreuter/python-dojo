# Test rápido de Python #8
# -----------------------------------------------
# ¿Cuál es el resultado de este código?

# Código:
x = [[]] * 3
x[0].append(1)
print(x)

# Opciones:
# A) [[1], [], []]
# B) [[1], [1], [1]]
# C) [[], [], [1]]




# 👇👇👇 SPOILER: no sigas bajando si no quieres ver la respuesta 👇👇👇

































































































































"""
Respuesta correcta: B) [[1], [1], [1]]

Explicación:
Este ejercicio evalúa cómo se comportan las listas al ser multiplicadas con el operador `*`.

Primero veamos esta línea:

    x = [[]] * 3

Podrías pensar que estás creando una lista con tres listas vacías independientes. Pero en realidad, estás creando tres referencias al mismo objeto de lista.
Es decir, todas las posiciones de la lista `x` apuntan exactamente a la misma sublista en memoria.

Podemos confirmarlo usando `id()`:

    print(id(x[0]), id(x[1]), id(x[2]))

Verás que todos tienen el mismo identificador, lo que significa que son el mismo objeto.

Luego haces:

    x[0].append(1)

Esto modifica esa sublista compartida, que es la misma para todas las posiciones. Por eso, cuando imprimes `x`, el resultado es:

    [[1], [1], [1]]

Cada elemento de la lista principal muestra el mismo contenido, porque todos apuntan a la misma sublista.

Este es un comportamiento común que genera confusión, especialmente cuando se usa `*` para "copiar" listas que contienen estructuras mutables.

Consejo práctico:
Si quieres crear varias listas vacías independientes, usa una comprensión de listas en lugar de la multiplicación:

    x = [[] for _ in range(3)]

Así garantizas que cada sublista es un objeto distinto. Ahora sí, al hacer `x[0].append(1)`, solo la primera sublista se verá modificada:

    [[1], [], []]
"""