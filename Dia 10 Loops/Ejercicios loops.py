### Exercises: Level 1

##1. Iterate 0 to 10 using for loop, do the same using while loop.

print('Ejercicio 1 nivel 1: Itera del 0 al 10 usando el bucle for, haz lo mismo usando el bucle while.')

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    print(number)

##2. Iterate 10 to 0 using for loop, do the same using while loop.

print('Ejercicio 2 nivel 1: Itera del 0 al 10 usando el bucle for, haz lo mismo usando el bucle while.')

number = 10
while number > -1:
    print(number)
    number = number -1 

##3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
#   ```py
     #
     ##
     ###
     ####
     #####
     ######
     #######
#   ```

print('''Ejercicio 3 nivel 1: 
    Escriba un bucle que realice siete llamadas a print(), de modo que obtengamos en la salida el siguiente triángulo:
      ''')

triangle = '#'

for i in range(8):
    print(triangle*i)
    

##4. Use nested loops to create the following:

#   ```sh
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
#   ```

print('''Ejercicio 4 nivel 1:
    Utilice bucles anidados para crear lo siguiente:
''')

a = '# '
for i in range(8):
    print(a*8)

##5. Print the following pattern:
#   ```sh
#   0 x 0 = 0
#   1 x 1 = 1
#   2 x 2 = 4
#   3 x 3 = 9
#   4 x 4 = 16
#   5 x 5 = 25
#   6 x 6 = 36
#   7 x 7 = 49
#   8 x 8 = 64
#   9 x 9 = 81
#   10 x 10 = 100
#   ```

print('''Ejercicio 5 nivel 1:
    Imprime el siguiente patrón
''')

num = 0
while num < 11:
    print('{} x {} = {}'.format(num, num, num * num))
    num = num + 1

##6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

print('''Ejercicio 6 nivel 1:
      Itere a través de la lista, ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
       usando un bucle for e imprima los elementos.
''')
lenguages = ['Python', 'Numpy','Pandas','Django', 'Flask']

for lenguaje in lenguages:
    print(lenguaje)

##7. Use for loop to iterate from 0 to 100 and print only even numbers

print('''Ejercicio 7 nivel 1:
      Utilice el bucle for para iterar de 0 a 100 e imprimir solo números pares.
''')

num = 0
evenNumbers = num % 2
while num < 101:
    print(num)
    num = num + 2

##8. Use for loop to iterate from 0 to 100 and print only odd numbers

print('''Ejercicio 8 nivel 1:
      Utilice el bucle for para iterar de 0 a 100 e imprimir solo números impares
''')

num = 1
while num < 101:
    print(num)
    num = num + 2

   
### Exercises: Level 2
    
##1.  Use for loop to iterate from 0 to 100 and print the sum of all numbers.

##   ```sh
#   The sum of all numbers is 5050.
#   ```

print('''   Ejercicio 1 nivel 2: 
        Utilice el bucle for para iterar de 0 a 100 e imprimir la 
      suma de todos los números.
      ''')

num = 0
for i in range(101):
    num = num + i 
    print(num)

#2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

#    ```sh
#    The sum of all evens is 2550. And the sum of all odds is 2500.
#    ```

print('''Ejercicio 2 nivel 2:
      Utilice el bucle for para iterar de 0 a 100 e imprimir la suma 
      de todos los pares y la suma de todos los impares.     
''')

parnum = []
impnum = []

for i in range(101):
    if i % 2 == 0:
        parnum.append(i)
    else:
        impnum.append(i)

print(parnum)
print('La suma de los numeros pares de 0 a 100 es: ', sum(parnum))
print(impnum)
print('La suma de los numeros impares de 0 a 100 es: ', sum(impnum))

### Exercises: Level 3

#1. Go to the data folder and use the [countries.py]
# (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py) file. 
# Loop through the countries and extract all the countries containing the word _land_.

import countries as paises

print('''Ejercicio 1 nivel 3:
      Recorra los países y extraiga todos los países que contengan la palabra _land_.
''')

p = paises.countries
land = 'land'

for pais in p:
    if land in pais:
        print(pais)

#2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.

print('''Ejercicio 2 nivel 3:
      Esta es una lista de frutas, ['banana', 'naranja', 'mango', 'limón'] 
      invierte el orden usando un bucle.
''')

fruitlist = ['banana', 'orange', 'mango', 'lemon']
fruitsortedlist = fruitlist[::-1]

print('Lista de frutas: ', fruitlist)

for fruit in fruitsortedlist:
    print(fruit)

#3. Go to the data folder and use the [countries_data.py]
# (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file. 
 #3.1. What are the total number of languages in the data
 #3.2. Find the ten most spoken languages from the data
 #3.3. Find the 10 most populated countries in the world

print('''Ejercicio 3 nivel 3:
''')

print('3.1 Cual es el total de los idiomas en el archivo')

import datosPais as datac 

datos = datac.paises
countrylanguage = []
for pais in datos:
    for lenguaje in pais['languages']:
        countrylanguage.append(lenguaje)
        
print('La cantidades de lenguajes en countriesdata son: ', len(countrylanguage))

print('3.2 Encuentra el idioma mas hablado')

setlanguages = set(countrylanguage)
dictlanguages = {

}
for language in setlanguages:
    dictlanguages[language] = 0

print(dictlanguages)

for idioma in dictlanguages:
    for pais in datos:  
         if idioma in pais['languages']:
             dictlanguages[idioma] = pais['population'] + dictlanguages[idioma]

sortValuesLanguagespopulation = sorted(dictlanguages.values(), reverse= True)
sorfkeyslanguagespopulation = sorted(dictlanguages, key= dictlanguages.get, reverse=True)

print( sorfkeyslanguagespopulation[1] ,sortValuesLanguagespopulation[1])

print('''Ejercicio 3.3 nivel 3:
      Encuentra los 10 idiomas mas populares en el mundo
''')
print('Los 10 idiomas mas hablados en el mundo son (orden decendente)')
for i in range(10):
    print(sorfkeyslanguagespopulation[i] ,sortValuesLanguagespopulation[i])
