# Test rápido de Python #5
# -----------------------------------------------
# ¿Cuál es el resultado de este código?

# Código:
x = [1, 2, 3]
print(x[::-1])

# Opciones:
# A) [3, 2, 1]
# B) [1, 2, 3]
# C) Error

# 👇👇👇 SPOILER: no sigas bajando si no quieres ver la respuesta 👇👇👇

































































































































"""
Respuesta correcta: A) [3, 2, 1]

Explicación:
Este código utiliza el operador de slicing (rebanado) en listas, una característica muy poderosa y común en Python.

La sintaxis de slicing es:

    lista[inicio:fin:paso]

Si omites los valores de inicio y fin, y solo colocas un paso negativo (como -1), Python interpreta que deseas recorrer la lista de atrás hacia adelante.

Por eso, la expresión:

    x[::-1]

crea una **nueva lista** con los elementos de x, pero en orden invertido.

En este caso:

    x = [1, 2, 3]
    x[::-1] devuelve [3, 2, 1]

Esto no modifica la lista original, solo genera una copia invertida.

Este truco es muy útil para invertir listas, strings o cualquier objeto que soporte slicing.

Ejemplos:

    "hola"[::-1]       → "aloh"
    [True, False][::-1] → [False, True]

Consejo práctico:
Si necesitas invertir una lista en el lugar (modificando la original), puedes usar:

    x.reverse()

Pero si solo necesitas una copia invertida y dejar la original intacta, el slicing con paso negativo es la opción ideal.
"""