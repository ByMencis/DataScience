# EJERCICIO 1

"""
    Decribe una variable con nombre "notas" que tenga el valor -3
    muestra su valor
"""

from re import L
import string


notas = -3
print(notas)

# EJERCICIO 2

"""
    Imprime los valores de "s" es igual 25, de "y" es igual a 10, poniendo la siguiente salida:
    El valor de "s" es "valor de s" y el valor de y es "valor de y"
"""

s = 25
y = 10
print(f'el valor de s es {s} y el valor de y es {y}')
print('el valor de s es ' + str(s) + ' y el valor de y es ' + str(y))
print('el valor de s es ', s, ' y el valor de y es ', y)
print(f'el valor de s es %s y el valor de y es %s' %(s, y))

# EJERCICIO 3

"""
    Declarar una variable con nombre "name",
    que tenga el valor de Juan "El profesor"
"""
name = "juan",  "el profesor"
print(name)

# EJERCICIO 4

"""
    Concatena las siguientes palabras formando un sola:
    Juan "El profesor"
"""
name = "juan " + "el profesor"
print(name)

# EJERCICIO 5

"""
    Teniendo la siguientes palabras: no cuentes los días, haz que los días cuenten
     · Pon las primeras letras de cada palabra en mayúsculas
     · Pon todas las letras en mayúsculas
     · Pon todas las letras en minúculas
"""
letra = "no cuentes los días, haz que los días cuenten"

print(letra)
print(letra.lower())
print(letra.title())
print(letra.upper())


# EJERCICIO 6

"""
    Realiza la suma de 26 y 35
    Realiza la multiplicación de 26 y 35
    Realiza la operación de 2 + 32 por 10
    Saca el resultado de 3 elevado a 9
    Redondea el resultado anterior a dos decimales
    Muestra de que tipo se trata
"""

s = 26
n = 35
print ("La suma de los dos números es: " + str(s + n))
print ("La suma de los dos números es: " + str(s * n))

a = 2
m = 32
t = 10
print ("El resultado de la operacion de los tres números es: " + str(a + m * t))

f = 3
q = 9
print ("La division de los dos números es: " + str(f / q))

numero = 0.333333333333
roundnumero = round(numero, 2)
print(roundnumero)




# EJERCICIO 7

"""
    Saca el valor absoluto de -32
    Muestra el máximo y el mínimo de (3, -6, 4, -10, 2.6666)
"""
num = -32
absoluto = abs( num)
print(absoluto)

v = 3, -6, 4, -10, 2.6666
max_value = max(v)
min_value = min(v)
print("valor maximo:", max_value)
print("valor minimo:", min_value)

# EJERCICIO 8

"""
    Tratar de reemplazar los valores que faltan en este listado --> por un -1
    L = [10, None, 8, 5, None, 20]
    1) Hazlo de la forma más fácil posible teniendo en cuenta la posición (index) de esos valores.
    2) Crea un dataframe con esos valores (L = [10, None, 8, 5, None, 20])
"""
L = [10, None, 8, 5, None, 20]
L[1]= -1
L[4]= -1
print(L)
import pandas as pd
df = pd.DataFrame
