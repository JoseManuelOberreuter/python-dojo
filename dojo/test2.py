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

# 👇👇👇 SPOILER: no sigas bajando si no quieres ver la respuesta 👇👇👇




































































































"""
Respuesta correcta: B) [1, 2, 3, 4]

Explicación:
En Python, las listas son objetos mutables, lo que significa que pueden cambiar después de ser creadas.

Cuando escribes:

    y = x

no estás creando una copia nueva de la lista, sino que estás haciendo que **`y` apunte al mismo objeto en memoria que `x`**. Es decir, tanto `x` como `y` hacen referencia a la misma lista.

Luego, cuando haces:

    y.append(4)

estás modificando la lista compartida por ambas variables. Por lo tanto, cuando imprimes `x`, ves el resultado:

    [1, 2, 3, 4]

✅ Ambas variables apuntan al mismo objeto, así que cualquier cambio que hagas a través de `y` se verá reflejado también en `x`.

🧠 Consejo práctico:
Si quieres hacer una copia independiente de una lista, puedes usar slicing (`[:]`) o la función `copy()`:

```python
x = [1, 2, 3]
y = x[:]        # Copia con slicing
# o
y = x.copy()    # Copia con método built-in
"""