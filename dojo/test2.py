# Test rápido de Python #2
# -----------------------------------------------
# ¿Cuál es el resultado de este código?

# Código:
x = [1, 2, 3]
y = x
y.append(4)
print(x)

# Opciones:
# A) [1, 2, 3]
# B) [1, 2, 3, 4]
# C) Error












































































"""
Respuesta correcta: B) [1, 2, 3, 4]

Explicación:
En Python, las listas son objetos mutables. 
Cuando haces `y = x`, no se crea una nueva lista,
sino que `y` y `x` apuntan al mismo objeto en memoria.
Por eso, al hacer `y.append(4)`, también cambia `x`.
"""