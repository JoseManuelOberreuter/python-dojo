# Test rápido de Python #13
# -----------------------------------------------
# ¿Cuál es el resultado de este código?

# Código:
a = (1)
b = (1,)
print(type(a))
print(type(b))

# Opciones:
# A) Ambos son tuples
# B) b es int y a es tuple
# C) a es int y b es tuple




# 👇👇👇 SPOILER: no sigas bajando si no quieres ver la respuesta 👇👇👇

































































































































"""
Respuesta correcta: C) a es int y b es tuple

Explicación:
En Python, los paréntesis por sí solos no definen una tupla. Lo que define una tupla es la coma.  
Esto puede resultar confuso porque visualmente `a = (1)` parece una tupla, pero en realidad no lo es.

Analicemos el código:

    a = (1)

Aquí, los paréntesis simplemente agrupan una expresión. Python lo interpreta como:

    a = 1

Por eso, `type(a)` devuelve:

    <class 'int'>

Ahora, en:

    b = (1,)

Esa coma después del 1 sí le indica a Python que queremos una tupla, aunque solo tenga un elemento. Así que:

    type(b) → <class 'tuple'>

Esto se aplica incluso sin paréntesis:

    c = 1,
    type(c) → <class 'tuple'>

Comparaciones útiles:

    (1)     → int
    (1,)    → tuple
    (1, 2)  → tuple
    1,      → tuple

Consejo práctico:
Siempre que necesites crear una tupla de un solo elemento, 
no olvides la coma. Sin ella, estarás asignando simplemente un número (u otro tipo de dato) y no una tupla.
"""