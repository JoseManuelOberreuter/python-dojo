# Test rápido de Python #7
# -----------------------------------------------
# ¿Cuál es el resultado de este código?

# Código:
print("a" > "Z")

# Opciones:
# A) True
# B) False
# C) Error

# 👇👇👇 SPOILER: no sigas bajando si no quieres ver la respuesta 👇👇👇
































































































































"""
Respuesta correcta: A) True

Explicación:
En Python, los strings se pueden comparar 
usando operadores como <, >, ==, etc.  
Estas comparaciones se hacen carácter 
por carácter según el valor Unicode de cada carácter.

Unicode es un estándar que asigna un número único a cada carácter 
que ves en pantalla, ya sea una letra, símbolo o emoji. Por ejemplo:

>>> ord("a") → 97
>>> ord("Z") → 90

La función `ord()` te permite conocer el valor numérico Unicode de un carácter.

En el ejemplo del código:

>>> "a" > "Z"

Python compara directamente los valores Unicode del primer carácter de cada string.  
Como `ord("a") = 97` y `ord("Z") = 90`, entonces `97 > 90` y el resultado es `True`.

Esto sorprende a muchos principiantes, porque en el alfabeto latino la letra "Z" viene después de la "a", pero Unicode no está ordenado según el alfabeto sino según una tabla numérica estandarizada.

En Unicode, todos los caracteres mayúsculos del alfabeto inglés (A–Z) tienen valores del 65 al 90.  
En cambio, las letras minúsculas (a–z) tienen valores del 97 al 122.  
Por eso cualquier letra minúscula es considerada "mayor" que cualquier mayúscula al compararlas directamente.

Ejemplos útiles:

>>> print("b" > "A")   → True      (98 > 65)
>>> print("Z" < "a")   → True      (90 < 97)
>>> print("apple" > "Apple") → True  (97 > 65, por la primera letra)

🧠Consejo:
Si quieres comparar cadenas de texto sin importar si están en mayúscula o minúscula, lo mejor es convertir ambas a minúsculas o mayúsculas antes de compararlas. Por ejemplo:

>>> "a".lower() > "Z".lower() → False   (porque ahora comparas "a" y "z")

Así te aseguras de una comparación más natural y predecible desde el punto de vista del usuario.
"""