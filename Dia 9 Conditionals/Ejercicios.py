### Exercises: Level 1

##1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: 
# You are old enough to drive. If below 18 give feedback to wait for the missing amount of years.
# Output:
#    ```sh
#    Enter your age: 30
#    You are old enough to learn to drive.
#    Output:
#    Enter your age: 15
#    You need 3 more years to learn to drive.
#    ```

print('Exercise 1 Level 1')

yearsold = int(input("Enter your age: "))
if yearsold >= 18:
    print('You are old enough to learn to drive.')
else:
    print('You need 3 more years to learn to drive.')

##2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”)
# to get the age as input. You can use a nested condition to print 'year' for 1 year difference 
# in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
#    ```sh
#    Enter your age: 30
#    You are 5 years older than me.
#    ```

print('Ejercicio 2 nivel 1:')

print('Mi edad es de ', yearsold)
yourage = int(input("Ingresa tu edad: "))

print('Quien es mayor')
if yearsold == yourage:
    print('Somos de la misma edad'), ('Los dos tenemos: ', yearsold, 'años')
elif yearsold > yourage:
    print('Yo soy mayor que tu por',yearsold - yourage, 'años')
else:
    print('Eres mayor que yo por', yourage - yearsold, 'años')

#3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b,
#  if a is less b return a is smaller than b, else a is equal to b. Output:

#```sh
#Enter number one: 4
#Enter number two: 3
#4 is greater than 3
#```

print('Ejercicio 3 nivel 1:')

a = int(input('Ingresa un numero: '))
b = int(input('Ingresa otro numero: '))

print('Que numero es mayor')
if a == b:
    print('Ambos numeros son iguales'),('Los dos son de un valor de', a)
elif a > b:
    print('El primer numero es mayor que el segundo por ', a - b)
else:
    print('El segundo numero es mayor que el primero por ', b - a)

### Exercises: Level 2

##1. Write a code which gives grade to students according to theirs scores:

#        ```sh
#        80-100, A
#        70-89, B
#        60-69, C
#        50-59, D
#        0-49, F
#        ```

print('Ejercicio 1 nivel 2')

calAlumno = int(input('Ingresa tu calificación: '))

if calAlumno > 80 and calAlumno <= 100:
    print('Felicidades tu calificacion es A')
elif calAlumno < 80 and calAlumno >= 70:
    print('Tu calificacion es B')
elif calAlumno < 70 and calAlumno >= 60:
    print('Tu calificacion es C')
elif calAlumno < 60 and calAlumno >= 50:
    print('Tu calificacion es D')
elif calAlumno < 50:
    print('Tu calificacion es F suerte para la proxima vez')
else:
    print('Error tu calificacion no es valida') 


#   1. Check if the season is Autumn, Winter, Spring or Summer. If the user input is:
#    September, October or November, the season is Autumn.
#    December, January or February, the season is Winter.
#    March, April or May, the season is Spring
#    June, July or August, the season is Summer

Autumn = {'September', 'Septiembre', 'October', 'Octubre', 'November', 'Noviembre'}
Winter = {'Dicember', 'Diciembre', 'January', 'Enero', 'February', 'Febrero'}
Spring = {'March', 'Marzo', 'April', 'Abril', 'May', 'Mayo'}
Summer = {'June', 'Junio', 'July', 'Julio', 'Agust', 'Agosto'}

month = input('Ingresa un mes para decirte la estacion del año: ')

if month in Autumn:
    print('La estacion del año es Otoño')
elif month in Winter:
    print('La estacion del año es Invierno')
elif month in Spring:
    print('La estacion del año es Primavera')
elif month in Summer:
    print('La estacion del año es Verano')
else:
    print('Error: el mes que ingreso no es valido por favor ingrese uno empezando con mayuscula y lo demas en minusculas')

#   2. The following list contains some fruits:

#    ```sh
#    fruits = ['banana', 'orange', 'mango', 'lemon']
#    ```

#   If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
# If the fruit exists print('That fruit already exist in the list')

print('Ejercicio 2 lvl 2')

fruit = input('Ingresa el nombre de una fruta (todo en minusculas): ')

fruits = ['banana', 'orange', 'mango', 'lemon']

print('La lista actual de frutas es: ', fruits)

if fruit in fruits:
    print('Esta fruta ya esta en la lista')
else:
    fruits.append(fruit)
    print('La lista se a actualizado a: ', fruits)

### Exercises: Level 3

#   1. Here we have a person dictionary. Feel free to modify it!

#```py
#        person={
#    'first_name': 'Asabeneh',
#    'last_name': 'Yetayeh',
#    'age': 250,
#    'country': 'Finland',
#    'is_marred': True,
#    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#    'address': {
#        'street': 'Space street',
#        'zipcode': '02210'
#    }
#    }
#```

#   * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
#   * Check if the person dictionary has skills key, if so check if the person has 
#     'Python' skill and print out the result.
#   * If a person skills has only JavaScript and React, print('He is a front end developer'), 
#     if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
#     if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
#     else print('unknown title') - for more accurate results more conditions can be nested!
#   * If the person is married and if he lives in Finland, print the information in the following format:

#```py
#    Asabeneh Yetayeh lives in Finland. He is married.
#```

print('Ejercicio 1 nivel 3')

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

print(person)

print('problematica 1: Conseguir las keys de enmedio de skills')

midskillskeys = len(person.get('skills'))//2

print('Las habilidades de enmedio son ', person['skills'][midskillskeys])

print('problematica 2: Checar si la persona tiene de habilidad el uso de python')

if 'Python' in person['skills']:
    print('Si la persona tiene la habilidad de Python en: habilidades: ', person['skills'])
else:
    print('La persona no tiene la habilidad de Python en sus habilidades')

print('''Problematica 3: revisar si la persona tiene solo las habilidades de JavaScript y React devolver
      que la persona es un front end developer, si la persona tiene la hablidad de Node, Python, MongoDB
      devolver que la persona es un backend developer, 
      si la persona tiene las habilidades Node and MongoDB devolver es un fullstack developer, 
      si no devolver unknown title.
      ''')

frontDev = 'JavaScript' in person['skills'] and 'React' in person['skills']
backendDev = 'Node,' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']
fullstackDev = 'React' in person['skills'] and 'Node' in person['skills']  and 'MongoDB' in person['skills']

if frontDev == True and len(person['skills']) == 2 :
    print("El programador es un (Front end developer)")
elif backendDev == True and len(person['skills']) == 3:
    print('El programador es un (Backend developer)')
elif fullstackDev == True:
    print('El programador es un (Fullstack developer)')
else:
    print('unknown title')

print('''Problematica 4 y ultima:
Si la persona esta casada y vive en findlandia deolver la informacion en el siguiente orden 
(Nombre, Apellido, donde vive, y si esta casado)      
''')

if person['is_marred'] == True and 'Finland' in person['country']:
    print('''
     Asabeneh Yetayeh vive en Finland, el es casado
    ''')
else:
    print('Una de las condiciones no coinciden')
