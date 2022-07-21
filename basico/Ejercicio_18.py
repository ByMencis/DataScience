# EJERCICIO 1

"""
    Definir una función max()
    que tome como argumento dos números y devuelva el mayor de ellos. 
    (Es cierto que python tiene una función max() incorporada,
    pero hacerla nosotros mismos es un muy buen ejercicio).
"""


from re import A, L


def maximo(n1, n2):
    if n1 < n2:
        print("El valor máximo es {n2}")
        return n2
    elif n2 < n1:
        print("El valor máximo es {n1}")
        return n1
    else:
        return "son iguales"

print(maximo(30, 15))

# EJERCICIO 2


"""
    Definir una función max_de_tres(), 
    que tome tres números como argumentos y 
    devuelva el mayor de ellos.
"""


def max_de_tres(n1, n2, n3):
    if n1 < n2 < n3:
        print("El valor máximo es {n3}")
        return n3
    if n1 < n2 > n3:
        print("El valor máximo es {n2}")
        return n2
    elif n3 < n2 < n1:
        print("El valor máximo es {n1}")
        return n1
    else:
        return "son iguales"
print(max_de_tres(1, 3, 5))
    



# EJERCICIO 3

"""
    Definir una función que calcule la longitud de una lista 
    o una cadena dada. 
    (Es cierto que python tiene la función len() incorporada, 
    pero escribirla por nosotros mismos resulta un muy buen ejercicio.
"""
lista = ("Madrid", "Valencia", "Barcelona", "Toledo")
def longitud():

 # EJERCICIO 4
 _
def es_vocal (c):
    if c == "a" or c == "e" or c == "i" or c == "o" or c== "u":
        return True

    elif c == "A" or c == "E" or c == "I" or c == "O" or c == "U":
        return True

    return False

caracter = input("introduce una letra por favor: ")
print(es_vocal(caracter))

# EJERCICIO 5

""""
     Escribir una función suma() y una función multip() que sumen y multipliquen
    respectivamente todos los números de una lista.
    Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
"""


def  suma (n1, n2, n3):
   if n1 * n2 * n3:
        print("El valor es {}")
print(suma(5, 6, 8))


def  multip (n1, n2, n3):
    if n1 * n2 * n3:
        print("El valor es {}")
    
print(multip(5, 6, 8))
print("Enhorabuena acabaste los ejercicios")