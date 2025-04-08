### Exercises: Level 3

##1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list

print('''Ejercicio 1 nivel 3:
      Llama a tu función shuffle_list, toma una lista como parámetro y devuelve una lista aleatoria
''')

import random

def shuffle_list(lst):
    shuffled = lst[:]
    random.shuffle(shuffled)
    return (shuffled)

print('lista normal',[1, 2, 3, 4, 5, 6, 7, 8, 9])
print(shuffle_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))

##2. Write a function which returns an array of seven random numbers in a range of 0-9.
# All the numbers must be unique.

print('''Ejercicio 2 nivel 3:
      Escriba una función que devuelva una matriz de siete números aleatorios en un rango de 0 a 9. 
      Todos los números deben ser únicos.
''')

def unique_random_numbers():
    import random
    return random.sample(range(0, 10), 7)

print("Numeros aleatorios randoms:", unique_random_numbers())
print("revisado")