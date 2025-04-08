### Exercises: Level 1

##1. Explain the difference between map, filter, and reduce.

'''
map : Transforma cada elemento de un iterable aplicando una función.
filter: Filtra elementos de un iterable según una condición
reduce: Reduce un iterable a un único valor acumulativo aplicando una función.
'''

##2. Explain the difference between higher order function, closure and decorator

'''
- Una función es código ejecutable básico.
- Un closure es una función que "recuerda" variables de un ámbito superior.
- Un decorator es un patrón que usa funciones (y a menudo closures) para modificar otras funciones.
'''

##3. Define a call function before map, filter or reduce, see examples.

'''
Significa que, en lugar de usar una función lambda directamente dentro de map, 
filter o reduce, primero defines la función con def y luego la pasas como argumento.
'''

##4. Use for loop to print each country in the countries list.

print('''Ejercicio 4 nivel 1:
      Utilice el bucle for para imprimir cada país en la lista de países.
''')

paises = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

for country in paises:
    print(country)

##5. Use for to print each name in the names list.

print('''Ejercicio 5 nivel 1:
      Utilice for para imprimir cada nombre en la lista de nombres.
''')

nombres = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway','Iceland']

for name in nombres:
    print(name)

##6. Use for to print each number in the numbers list.

print('''Ejercicio 6 nivel 1:
      Utilice for para imprimir cada número en la lista de números.
''')

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numeros:
    print(num)

print("revisado")