# Test rápido de Python #11
# -----------------------------------------------
# ¿Cuál es el resultado de este código?

# Código:
print(2**3**2)

# Opciones:
# A) 64
# B) 512
# C) 256



# 👇👇👇 SPOILER: no sigas bajando si no quieres ver la respuesta 👇👇👇

































































































































"""
Respuesta correcta: B) 512

Explicación:
Este ejercicio evalúa tu comprensión sobre la precedencia y asociatividad de los operadores en Python, 
especialmente el operador de exponenciación (`**`).

La expresión:

    2**3**2

no se evalúa de izquierda a derecha como podrías pensar, sino de derecha a izquierda, 
porque el operador `**` es **asociativo por la derecha**.

Entonces Python interpreta esta expresión como:

    2 ** (3 ** 2)

y no como:

    (2 ** 3) ** 2

Vamos a resolverlo paso a paso:

    3 ** 2 = 9
    2 ** 9 = 512

Por lo tanto, el resultado final es:

    512

Comparación:
Si lo hubieras interpretado de izquierda a derecha:

    (2 ** 3) ** 2 = 8 ** 2 = 64   → Incorrecto

Consejo práctico:
Cuando trabajes con múltiples operaciones de potencias encadenadas, 
recuerda que `**` se evalúa desde la derecha. Si quieres cambiar ese comportamiento, 
debes usar paréntesis explícitos para forzar el orden que deseas.

Ejemplo:

    (2 ** 3) ** 2   → 64
    2 ** (3 ** 2)   → 512
"""
