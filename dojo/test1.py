# Test rápido de Python #1
# -----------------------------------------------
# ¿Cuál es el resultado de este código?

# Código:
print("5" * 3)

# Opciones:
# A) 15
# B) 555
# C) Error

# 👇👇👇 SPOILER: no sigas bajando si no quieres ver la respuesta 👇👇👇




































































































"""
Respuesta correcta: B) 555

Explicación:
En Python, cuando multiplicas un string por un número entero,
el resultado no es una operación matemática, sino una operación de repetición del string.

En este caso:

    "5" * 3

significa "repite el string '5' tres veces".  
Por lo tanto, el resultado es el string:

    "555"

No se convierte en número, ni se realiza una suma o multiplicación numérica.

Este comportamiento es válido con cualquier string. Por ejemplo:

    "abc" * 2 → "abcabc"  
    "ha" * 4  → "hahahaha"

🚫 Importante: si intentaras multiplicar un string por otro string (`"5" * "3"`), obtendrías un error, ya que solo se puede multiplicar un string por un número entero.

🧠 Consejo práctico:
Este comportamiento es útil para crear separadores visuales, como:

print("-" * 30)  

# Imprime ------------------------------
"""
