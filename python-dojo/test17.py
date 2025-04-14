# Test rápido de Python #17
# -----------------------------------------------
# ¿Cuál es el resultado de este código?

# Código:
print(all([True, 1, ""]))

# Opciones:
# A) True
# B) False
# C) Error



# 👇👇👇 SPOILER: no sigas bajando si no quieres ver la respuesta 👇👇👇

































































































































"""
Respuesta correcta: B) False

Explicación:
La función `all()` recibe un iterable (como una lista o tupla) y devuelve `True` 
solo si todos los elementos del iterable son verdaderos. 
Si alguno es considerado falso, devuelve `False`.

En este caso evaluamos:

    all([True, 1, ""])

Desglosemos los valores:

- `True` → verdadero
- `1` → verdadero (en Python, cualquier número distinto de cero es `True`)
- `""` → falso (un string vacío es considerado `False`)

Como hay un valor falsy (`""`), el resultado de `all()` será `False`.

Recordemos que en Python se consideran `False` los siguientes valores:

- `0`
- `0.0`
- `None`
- `""` (string vacío)
- `[]` (lista vacía)
- `{}` (diccionario vacío)
- `set()` (conjunto vacío)
- cualquier objeto personalizado con `__bool__()` o `__len__()` que devuelva `False` o `0`

Todo lo demás es `True`.

Ejemplos adicionales:

    all([1, 2, 3])         → True
    all([1, 0, 3])         → False
    all([])               → True (porque no hay elementos falsos)
    all(["texto", ""])    → False

Consejo práctico:
`all()` es útil para verificar si todos los elementos cumplen una condición, por ejemplo:

    all(x > 0 for x in [1, 2, 3]) → True
    all(x > 0 for x in [0, 2, 3]) → False

En contraste, si quieres saber si al menos uno es verdadero, puedes usar `any()`:

    any([False, False, True]) → True
"""
