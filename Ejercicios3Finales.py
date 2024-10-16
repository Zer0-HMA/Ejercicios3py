# 1.
entero = 5
print ("Ejercicio 1")
print(entero)

# 2.
flotante = 3.14
print ("Ejercicio 2")
print(flotante)

# 3.
nombre = "Python"
print ("Ejercicio 3")
print(len(nombre))

# 4.
lista = [1, 2, 3]
print ("Ejercicio 4")
print(lista[0])

# 5.
diccionario = {'a': 1, 'b': 2}
print ("Ejercicio 5")
print(diccionario['a'])

# 6.
num = 4
print ("Ejercicio 6")
print("Par" if num % 2 == 0 else "Impar")

# 7.
cadena = "Hola Mundo"
print ("Ejercicio 7")
print("Contiene 'Mundo'" if "Mundo" in cadena else "No contiene 'Mundo'")

# 8.
print ("Ejercicio 8")
num = -1
if num > 0:
    print("Positivo")
elif num < 0:
    print("Negativo")
else:
    print("Cero")

# 9.
print ("Ejercicio 9")
year = 2020
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Bisiesto")
else:
    print("No bisiesto")

# 10.
num = 15
print ("Ejercicio 10")
print("Dentro de rango" if 1 <= num <= 10 else "Fuera de rango")

# 11.
print ("Ejercicio 11")
for i in range(1, 6):
    print(i, end=', ')

# 12.
print ("Ejercicio 12")
print(sum(range(1, 11)))

# 13.
print ("Ejercicio 13")
cuadrados = [x**2 for x in range(1, 6)]
print(cuadrados)

# 14.
cadena = "Hola"
print ("Ejercicio 14")
vocales = sum(1 for char in cadena if char in "aeiouAEIOU")
print(vocales)

# 15.
print ("Ejercicio 15")
tabla = [3 * i for i in range(1, 11)]
print(tabla)

# 16.
print ("Ejercicio 16")
lista = []
lista.append(1)
print(lista)
lista.append(2)
print(lista)

# 17.
print ("Ejercicio 17")
conjunto = {1, 2, 3}
print(2 in conjunto)

# 18.
print ("Ejercicio 18")
diccionario = {}
diccionario['a'] = 1
print(diccionario)

# 19.
print ("Ejercicio 19")
lista = [3, 1, 2]
print(sorted(lista))

# 20.
print ("Ejercicio 20")
lista = [1, 2, 3]
print(len(lista))

# 21.
print ("Ejercicio 21")
lista = [1, 2, 3, 4, 5]
print(sum(lista))

# 22.
print ("Ejercicio 22")
lista = [1, 2, 3, 4, 5]
pares = [num for num in lista if num % 2 == 0]
print(pares)

# 23.
print ("Ejercicio 23")
cadena = "Hola Mundo"
print(len(cadena.split()))

# 24.
print ("Ejercicio 24")
lista = [1, 3, 2]
print(max(lista))

# 25.
print ("Ejercicio 25")
lista = [True, True, False]
print(all(lista))

# 26.
print ("Ejercicio 26")
lista = [False, False, True]
print(any(lista))

# 27.
print ("Ejercicio 27")
claves = ['a', 'b', 'c']
valores = [1, 2, 3]
diccionario = dict(zip(claves, valores))
print(diccionario)

# 28.
print ("Ejercicio 28")
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
tuplas = list(zip(lista1, lista2))
print(tuplas)

# 29.
print ("Ejercicio 29")
lista = [1, 2, 1, 3]
print(lista.count(1))

# 30. Generar una lista de Fibonacci
n = 5
fibonacci = [0, 1]
for i in range(2, n):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
print("Ejercicio 30")
print(fibonacci[:n])

# 31. Reversar una lista
lista = [1, 2, 3]
print("Ejercicio 32")
print(lista[::-1])

# 32. Concatenar dos listas
lista1 = [1, 2]
lista2 = [3, 4]
print("Ejercicio 31")
print(lista1 + lista2)

import random

# 32. Concatenar dos listas
lista1 = [1, 2]
lista2 = [3, 4]
resultado_32 = lista1 + lista2

# 33. Crear una lista de números aleatorios
resultado_33 = [random.randint(1, 10) for _ in range(5)]

# 34. Contar la cantidad de elementos en un conjunto
conjunto = {1, 2, 3}
resultado_34 = len(conjunto)

# 35. Crear un diccionario a partir de una lista de tuplas
tuplas = [(1, 'a'), (2, 'b')]
resultado_35 = dict(tuplas)

# 36. Obtener los elementos únicos de una lista
lista = [1, 2, 2, 3]
resultado_36 = list(set(lista))

# 37. Verificar si un diccionario contiene una clave
diccionario = {'a': 1}
resultado_37 = 'a' in diccionario

# 38. Fusionar dos diccionarios
dic1 = {'a': 1}
dic2 = {'b': 2}
resultado_38 = {**dic1, **dic2}

# 39. Convertir una lista en un conjunto
lista = [1, 2, 2, 3]
resultado_39 = set(lista)

# 40. Obtener los elementos de un diccionario en forma de lista
diccionario = {'a': 1, 'b': 2}
resultado_40_claves = list(diccionario.keys())
resultado_40_valores = list(diccionario.values())

# 41. Calcular la suma de los valores en un diccionario
diccionario = {'a': 1, 'b': 2}
resultado_41 = sum(diccionario.values())

# 42. Filtrar un diccionario por un valor mínimo
diccionario = {'a': 1, 'b': 2, 'c': 3}
resultado_42 = {k: v for k, v in diccionario.items() if v >= 2}

# 43. Crear un contador de palabras
cadena = "Hola mundo hola"
palabras = cadena.split()
resultado_43 = {palabra: palabras.count(palabra) for palabra in set(palabras)}

# 44. Obtener los elementos comunes entre dos listas
lista1 = [1, 2, 3]
lista2 = [2, 3, 4]
resultado_44 = list(set(lista1) & set(lista2))

# 45. Comprobar si una lista es un subconjunto de otra
lista1 = [1, 2]
lista2 = [1, 2, 3]
resultado_45 = set(lista1).issubset(lista2)

# 46. Generar una lista de números pares del 1 al 20
resultado_46 = [x for x in range(1, 21) if x % 2 == 0]

# 47. Crear un diccionario de frecuencias de una lista
lista = [1, 2, 2, 3]
resultado_47 = {x: lista.count(x) for x in set(lista)}

# 48. Unir dos listas alternando sus elementos
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
resultado_48 = [val for pair in zip(lista1, lista2) for val in pair]

# 49. Encontrar el índice de un elemento en una lista
lista = [1, 2, 3]
resultado_49 = lista.index(2)

# 50. Crear un diccionario a partir de una lista de claves y valores
claves = ['a', 'b']
valores = [1, 2]
resultado_50 = dict(zip(claves, valores))

# 51. Filtrar palabras largas de una lista
palabras = ["uno", "dos", "tres", "cuatro"]
resultado_51 = [palabra for palabra in palabras if len(palabra) > 4]

# 52. Crear una lista de los índices de los elementos en una lista
lista = [10, 20, 30]
resultado_52 = list(range(len(lista)))

# 53. Ordenar un diccionario por sus valores
diccionario = {'a': 3, 'b': 1, 'c': 2}
resultado_53 = dict(sorted(diccionario.items(), key=lambda item: item[1]))

# 54. Verificar si dos listas son iguales
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
resultado_54 = lista1 == lista2

# 55. Crear un conjunto a partir de una lista con duplicados
lista = [1, 1, 2, 3]
resultado_55 = set(lista)

# 56. Calcular el promedio de una lista
lista = [1, 2, 3, 4, 5]
resultado_56 = sum(lista) / len(lista)

# 57. Comprobar si una lista está vacía
lista = []
resultado_57 = not bool(lista)

# 58. Obtener los elementos únicos de una lista manteniendo el orden
lista = [1, 2, 2, 3]
unicos = []
for elem in lista:
    if elem not in unicos:
        unicos.append(elem)
resultado_58 = unicos

# 59. Contar las letras en una cadena
cadena = "Hola"
resultado_59 = {letra: cadena.count(letra) for letra in set(cadena)}

# 60. Cambiar el valor de un elemento en un diccionario
diccionario = {'a': 1}
diccionario['a'] = 2
resultado_60 = diccionario

# 61. Eliminar un elemento de una lista
lista = [1, 2, 3]
lista.remove(2)
resultado_61 = lista

# 62. Repetir una cadena varias veces
cadena = "Hola"
resultado_62 = cadena * 3

# 63. Crear una lista de números aleatorios y ordenarla
resultado_63 = sorted([random.randint(1, 100) for _ in range(10)])

# 64. Crear una lista de listas
resultado_64 = [[1, 2], [3, 4]]

# Resultados
print("32:", resultado_32)
print("33:", resultado_33)
print("34:", resultado_34)
print("35:", resultado_35)
print("36:", resultado_36)
print("37:", resultado_37)
print("38:", resultado_38)
print("39:", resultado_39)
print("40:", resultado_40_claves, resultado_40_valores)
print("41:", resultado_41)
print("42:", resultado_42)
print("43:", resultado_43)
print("44:", resultado_44)
print("45:", resultado_45)
print("46:", resultado_46)
print("47:", resultado_47)
print("48:", resultado_48)
print("49:", resultado_49)
print("50:", resultado_50)
print("51:", resultado_51)
print("52:", resultado_52)
print("53:", resultado_53)
print("54:", resultado_54)
print("55:", resultado_55)
print("56:", resultado_56)
print("57:", resultado_57)
print("58:", resultado_58)
print("59:", resultado_59)
print("60:", resultado_60)
print("61:", resultado_61)
print("62:", resultado_62)
print("63:", resultado_63)
print("64:", resultado_64)
print("#################################################")
print(" Integrantes del equipo \n")
print(" Serrano Eduardo Cristobal \n Humberto Martinez Aragon \n Miguel Angel Jardon Espinoza \n")
print("#################################################")