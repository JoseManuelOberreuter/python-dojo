# Test rápido de Python #15
# -----------------------------------------------
# ¿Cuál es el resultado de este código?

# Código:
a = [1, 2]
b = a[:]
b[0] = 99
print(a)

# Opciones:
# A) [99, 2]
# B) [1, 99] 
# C) [1, 2]




# 👇👇👇 SPOILER: no sigas bajando si no quieres ver la respuesta 👇👇👇

































































































































"""
Respuesta correcta: B) [1, 2]

Explicación:
Este ejercicio trata sobre copias superficiales de listas. En Python, cuando haces una copia con slicing (`[:]`), 
creas una nueva lista que contiene los mismos elementos, pero es un objeto diferente en memoria.

Analicemos el código paso a paso:

    a = [1, 2]

Se crea una lista `a`.

    b = a[:]

Aquí se genera una nueva lista `b`, con los mismos elementos de `a`. Esta operación es conocida como copia superficial o "shallow copy". 
La lista `b` tiene los mismos valores que `a`, pero no es la misma lista.

    b[0] = 99

Modificamos el primer valor de la lista `b`. Esto no afecta a `a`, ya que son listas diferentes.

Por lo tanto, cuando imprimimos `a`, sigue siendo:

    [1, 2]

Esto demuestra que copiar una lista con `[:]` permite trabajar con una copia independiente.

Consejo práctico:
- Si los elementos dentro de la lista son tipos inmutables (como números o strings), la copia superficial es suficiente.
- Si los elementos son estructuras mutables (listas, diccionarios, etc.), y necesitas evitar referencias compartidas, considera usar el módulo `copy` con `copy.deepcopy()`.

Ejemplo:

    import copy
    nueva_lista = copy.deepcopy(lista_original)

"""