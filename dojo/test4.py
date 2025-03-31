# Test rápido de Python #4
# -----------------------------------------------
# ¿Cuál es el resultado de este código?

# Código:
print(bool("False"))

# Opciones:
# A) True
# B) False
# C) Error

# 👇👇👇 SPOILER: no sigas bajando si no quieres ver la respuesta 👇👇👇

































































































































"""
Respuesta correcta: A) True

Explicación:
En Python, la función bool() convierte un valor a su equivalente booleano, y sigue reglas claras:

- Cualquier string vacío ("") se evalúa como False
- Cualquier string que contenga al menos un carácter se evalúa como True

En este caso, el string es "False", que aunque semánticamente representa algo falso, no está vacío. Por lo tanto, Python lo considera como True.

Es decir:

    bool("False")  →  True

Esto puede parecer confuso para principiantes, porque el contenido del string sugiere lo contrario. Pero recuerda: Python no evalúa el significado del texto dentro del string, solo verifica si hay contenido.

Otros ejemplos:

    bool("True")     →  True
    bool("0")        →  True
    bool("anything") →  True
    bool("")         →  False

Consejo práctico:
Siempre que trabajes con strings y valores booleanos, asegúrate de no confundir el contenido del string con su evaluación lógica. Si necesitas verificar el valor del contenido, debes compararlo directamente:

    if my_string == "False":
        # Esto sí evalúa el texto
"""
