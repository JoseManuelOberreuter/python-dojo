# Test rápido de Python #16
# -----------------------------------------------
# ¿Cuál es el resultado de este código?

# Código:
print(5 // 2)

# Opciones:
# A) 2.5
# B) 2
# C) 3



# 👇👇👇 SPOILER: no sigas bajando si no quieres ver la respuesta 👇👇👇

































































































































"""
Respuesta correcta: B) 2

Explicación:
El operador `//` en Python realiza una división entera, 
también conocida como división con redondeo hacia abajo o floor division.

Esto significa que el resultado será el cociente sin decimales, 
redondeado hacia el número entero más bajo (hacia abajo en la recta numérica),
incluso si el número es negativo.

En este caso:

    5 // 2

El resultado de 5 dividido por 2 es 2.5, pero como estamos usando `//`, 
el decimal se descarta y se obtiene:

    2

No se redondea al entero más cercano (eso sería 3), 
ni se mantiene el decimal. Simplemente se toma el número entero 
más bajo que no exceda el resultado real.

Ejemplos adicionales:

    10 // 3    → 3
    9 // 4     → 2
    5 // 2     → 2
    -5 // 2    → -3  (porque -2.5 se redondea hacia abajo, no hacia cero)

Consejo práctico:
Usa `//` cuando necesites obtener únicamente la parte entera de una división. 
Si necesitas el residuo, puedes combinarlo con el operador `%`:

    5 // 2 → 2
    5 % 2  → 1

Entre ambos puedes reconstruir el número original:

    (5 // 2) * 2 + (5 % 2) = 2 * 2 + 1 = 5
"""