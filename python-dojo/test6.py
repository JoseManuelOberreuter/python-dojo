# Test rápido de Python #6
# -----------------------------------------------
# ¿Cuál es el resultado de este código?

# Código:
print(0.1 + 0.2 == 0.3)

# Opciones:
# A) True
# B) False
# C) Error

# 👇👇👇 SPOILER: no sigas bajando si no quieres ver la respuesta 👇👇👇




































































































"""
Respuesta correcta: B) False

Explicación:
Aunque podrías esperar que 0.1 + 0.2 sea igual a 0.3, en realidad no lo es.

Esto se debe a cómo los números de punto flotante se representan internamente
en la mayoría de los lenguajes de programación, incluido Python. Los números
decimales como 0.1 y 0.2 **no pueden representarse con precisión exacta en binario**,
así como 1/3 no puede representarse exactamente en decimal (0.333...).

Por ejemplo, cuando haces:

>>> print(0.1 + 0.2)
0.30000000000000004

Este pequeño error es suficiente para que la comparación `0.1 + 0.2 == 0.3`
devuelva `False`, porque:

>>> 0.1 + 0.2  →  0.30000000000000004  
>>> 0.3        →  0.3

Y Python detecta que estos dos valores no son exactamente iguales.

🧠 Consejo: Si necesitas comparar números flotantes en Python,
es mejor usar un margen de error (tolerancia), por ejemplo:

abs((0.1 + 0.2) - 0.3) < 1e-9  # Esto devuelve True

Esto se conoce como comparación con tolerancia o comparación segura de floats. 
"""