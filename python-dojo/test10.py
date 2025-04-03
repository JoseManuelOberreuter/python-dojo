# Test rápido de Python #10
# -----------------------------------------------
# ¿Cuál es el resultado de este código?

# Código:
print({1, 2, 3} & {2, 3, 4})

# Opciones:
# A) {1, 2, 3, 4}
# B) {2, 3}
# C) {1, 4}


# 👇👇👇 SPOILER: no sigas bajando si no quieres ver la respuesta 👇👇👇

































































































































"""
Respuesta correcta: B) {2, 3}

Explicación:
Este código usa el operador `&` entre dos sets (conjuntos) en Python.  
El operador `&` representa la **intersección** entre dos conjuntos, es decir, 
devuelve un nuevo set que contiene **solo los elementos que están presentes en ambos**.

En este caso:

    {1, 2, 3} & {2, 3, 4}

Ambos sets tienen los elementos 2 y 3 en común. Por lo tanto, la intersección es:

    {2, 3}

Este tipo de operación es muy útil cuando necesitas encontrar coincidencias entre colecciones, listas o grupos de datos únicos.

Otras operaciones útiles entre sets:

- Unión (todos los elementos, sin repetir):

      {1, 2, 3} | {3, 4, 5}  →  {1, 2, 3, 4, 5}

- Diferencia (elementos que están en el primer set pero no en el segundo):

      {1, 2, 3} - {2, 3}     →  {1}

- Diferencia simétrica (elementos que están en un set u otro, pero no en ambos):

      {1, 2, 3} ^ {2, 3, 4}  →  {1, 4}

Consejo práctico:
Los sets en Python eliminan automáticamente los elementos duplicados, y tienen un rendimiento muy eficiente para búsquedas y operaciones lógicas. Son ideales cuando necesitas trabajar con colecciones únicas y comparar contenido entre grupos.
"""