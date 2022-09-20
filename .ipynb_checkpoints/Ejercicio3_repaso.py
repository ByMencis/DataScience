# EJERCICIO 1

"""
    Dada una lista de nombre "listado" y con valores: 10,20,30,40,50
"""
# 1) Crea un pequeño programa capaz de conseguir el orden inverso de los números de "listado"
# imprime nuevamente el listado para tenerlo "a mano"
# 10-20-30-40-50 (tengo)
# 50-40-30-20-10 (lo que busco)

listado = [10,20,30,40,50]
print(listado[::-1])


# EJERCICIO 2

"""
    Programa que coge por teclado 5 números y los almacena en una lista

    Nota:

    debería estar en la misma celda

    Hazlo como puedas, discurre cómo sería..
"""





# EJERCICIO 3

"""
    Programa que coge por teclado una frase y es capaz de decir cuántas vocales hay

    Nota: asume que son letras minúsculas sin tildes.
"""

frase =(input("Escriba una frase: "))

def contar_vocales(frase):
	contador = 0
	for letra in frase:
		if letra.lower() in "aeiou":
			contador += 1
	return contador
cantidad = contar_vocales(frase)
# 1) Entrada de texto por teclado
# 2) Hazlo si puedes de varias formas
    # forma 1: contar vocales en palabra/frase
# 3) Hazlo de otra forma si se te ocurre..
    # forma 2

# EJERCICIO 4

"""
    Tablas de multiplicar:

    Haz algo tal que:
"""

# 1) Pregunta al usuario que tabla quiere multiplicar: <1 al 10>

# 2) Muestra los resultados de esta forma:

