# Ejercicio 1

"""
    Definir una función inversa() que calcule la inversion de una cadena. 
    Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse".
"""


def invertir_cadena(cadena):
    return cadena[::-1]
print(invertir_cadena("estoy probando"))


# Ejercicio 2

"""
    Definir una funcion es_palindromo() que reconoce palindromo 
    palabras  que tiene el mismo aspecto escritas invertidas), ejemplo: es_palindromo("radar")
    tendría que devolver True.
"""

def palindromo(cadena):
    inicio = 0
    fin = len(cadena) - 1
    while cadena[inicio] == cadena[fin]:
        if inicio >= fin:
            return True
        inicio += 1
        fin -= 1
    return False

cadena = input("introduce una letra por favor: ")
print(palindromo(cadena))


# Ejercicio 3

"""
    Definir una funcion superposicion() que tome dos listas y devuelva True si tiene al
    menos 1 elemento en común o devuelva False en caso contrario. Escribe la función usando el bucle for 
    aninado.
"""

#No funciona
def superposicion (l1, l2 ):
    for item in l1:
        for item2 in l2:
            if item == item2:
                return True
            else:
                return False
l1 = [52, 13, 0, 5]
l2 = [52, 1, 0, 5]
print(superposicion(l1, l2))

