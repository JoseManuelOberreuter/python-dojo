# Test rápido de Python #12
# -----------------------------------------------
# ¿Cuál es el resultado de este código?

# Código:
print(len(" "))

# Opciones:
# A) 1
# B) 0
# C) Error



# 👇👇👇 SPOILER: no sigas bajando si no quieres ver la respuesta 👇👇👇

































































































































"""
Respuesta correcta: A) 1

Explicación:
La función `len()` en Python se utiliza para obtener la longitud de un objeto, 
como una lista, tupla o string. Cuando se aplica a un string, devuelve el número de caracteres que contiene.

En este caso, el string `" "` contiene un solo carácter, que es un espacio.

Aunque visualmente parezca "vacío", un espacio en blanco es un carácter válido y 
cuenta para el cálculo de la longitud. Por eso:

    len(" ") = 1

Comparaciones útiles:

    len("")       → 0   (string vacío)
    len("a")      → 1
    len(" a ")    → 3   (espacio + letra + espacio)
    len("   ")    → 3   (tres espacios)

Consejo práctico:
Este tipo de test es útil para recordar que Python no ignora espacios en blanco dentro de strings, 
a menos que tú lo hagas explícitamente usando métodos como `.strip()`, `.lstrip()` o `.rstrip()`.

Por ejemplo:

    len(" hola ") → 6
    len(" hola ".strip()) → 4
"""