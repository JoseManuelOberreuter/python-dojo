# Test rápido de Python #3
# -----------------------------------------------
# ¿Cuál es el resultado de este código?

# Código:
def f(x=[]):
    x.append(1)
    return x

print(f())
print(f())

# Opciones:
# A) [1] [1]
# B) [1] [1, 1]
# C) [1, 1] [1, 1, 1]

# 👇👇👇 SPOILER: no sigas bajando si no quieres ver la respuesta 👇👇👇





































































































"""
Respuesta correcta: B) [1] [1, 1]

Explicación:
El valor por defecto `x=[]` se evalúa solo una vez, 
cuando se define la función. Por eso, cada vez que llamas `f()`, 
usa y modifica la misma lista.
Después de la primera llamada, `x` es [1], 
y la segunda vez se le agrega otro 1, resultando en [1, 1].
"""