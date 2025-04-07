# Test rápido de Python #14
# -----------------------------------------------
# ¿Cuál es el resultado de este código?

# Código:
print(dict.fromkeys("abc", 0))

# Opciones:
# A) {'abc': 0}
# B) {'a': 0, 'b': 0, 'c': 0}
# C) {'a': None, 'b': None, 'c': None}



# 👇👇👇 SPOILER: no sigas bajando si no quieres ver la respuesta 👇👇👇

































































































































"""
Respuesta correcta: B) {'a': 0, 'b': 0, 'c': 0}

Explicación:
El método `dict.fromkeys()` permite crear un diccionario nuevo usando una secuencia de claves, 
y asigna a todas ellas un mismo valor.

Su sintaxis es:

    dict.fromkeys(iterable, valor_por_defecto)

En este caso:

    dict.fromkeys("abc", 0)

La función toma cada carácter de la cadena `"abc"` y los usa como claves del diccionario. 
A cada una se le asigna el valor `0`. El resultado es:

    {'a': 0, 'b': 0, 'c': 0}

Comparaciones útiles:

    dict.fromkeys([1, 2, 3], "x") → {1: 'x', 2: 'x', 3: 'x'}
    dict.fromkeys("hello", True) → {'h': True, 'e': True, 'l': True, 'o': True}

Nota importante:
Si el valor por defecto es un objeto mutable (como una lista), todas las claves compartirán la misma referencia. 
Esto puede causar problemas si luego modificas una de ellas.

Por ejemplo:

    d = dict.fromkeys("ab", [])
    d['a'].append(1)
    print(d)  → {'a': [1], 'b': [1]}

Esto sucede porque tanto 'a' como 'b' apuntan a la misma lista. 
Si quieres evitar esto, debes usar una comprensión de diccionario:

    d = {k: [] for k in "ab"}

Consejo práctico:
`dict.fromkeys()` es muy útil para inicializar rápidamente estructuras donde todas 
las claves comienzan con el mismo valor, como contadores, registros vacíos o banderas.
"""