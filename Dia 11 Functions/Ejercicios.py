##1. Declare a function _add_two_numbers_. 
# It takes two parameters and it returns a sum.

print('''Ejercicio 1 nivel 1:
      Declara una funcion que se entreguen dos numeros y que devuela una suma
''')

def addTwoNumbers():
    frstNum = float(input('Ingresa un primer numero: '))
    scndNum = float(input('Ingresa un segundo numero: '))
    sum = frstNum + scndNum
    return 'La suma es', sum

##2. Area of a circle is calculated as follows: area = π x r x r. 
# Write a function that calculates _area_of_circle_.

print('''Ejercicio 2 nivel 1:
    Escribe una funcion que calcule el area de un circulo
''')

def areaDeUnCirculo():
    r = float(input('Ingresa el Radio de tu circulo: '))
    pi = 3.1416
    area = pi * r * r
    return 'El area de un circulo es: ', area

##3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. 
# Check if all the list items are number types. If not do give a reasonable feedback.

print('''Ejercicio 3 nivel 1:
      Escriba una función llamada add_all_nums que tome un número arbitrario de argumentos y los sume todos.
      Compruebe si todos los elementos de la lista son de tipo numérico. De no ser así, proporcione una respuesta razonable.
''')

def add_all_nums():
    randomNum = input('Introduce un numero del tipo que tu quieras: ')
    if "." in randomNum:
        randomNum = float(randomNum)
        print (f"El tipo de numero '{randomNum}' que ingresaste es: '{type(randomNum)}'")
    elif "." in randomNum == False:
        randomNum = int(randomNum)
        print (f"El tipo de numero '{randomNum}' que ingresaste es: '{type(randomNum)}'")
    else:
        print(f"Error el numero '{randomNum}' no es valido.")
    return ""

##4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. 
# Write a function which converts °C to °F, _convert_celsius_to-fahrenheit_.

print('''Ejercicio 4 nivel 1:
      La temperatura en °C se puede convertir a °F usando esta fórmula: °F = (°C x 9/5) + 32. 
      Escriba una función que convierta °C a °F, _convert_celsius_to-fahrenheit_.
''')

def conv_C_to_F():
    C = float(input('Ingresa la temperatura que quieres convertir de Celsius a Fahrenheint: '))
    F = (C*9/5) + 32
    return 'En Fahrenheint son', F

##5. Write a function called check-season, it takes a month parameter and returns the season:
#  Autumn, Winter, Spring or Summer.

print('''Ejercicio 5 nivel 1:
      Escriba una función llamada check-season, toma un parámetro de mes y devuelve la temporada: Otoño, Invierno, Primavera o Verano.
''')

def check_season():
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
        return""

##6. Write a function called calculate_slope which return the slope of a linear equation

print('''Ejercicio 6 nivel 1:
      Escriba una función llamada calculate_slope que devuelva la pendiente de una ecuación lineal.
''')

def calculate_slope():
    x1 = float(input('Ingresa el dato x1 de la pendiente que deseas calcular: '))
    y1 = float(input('Ingresa el dato y1 de la pendiente que deseas calcular: '))
    x2 = float(input('Ingresa el dato x2 de la pendiente que deseas calcular: '))
    y2 = float(input('Ingresa el dato y2 de la pendiente que deseas calcular: '))
    M = (y2 - y1)/(x2 - x1)
    return 'La pendiente es de: ', M

##7. Quadratic equation is calculated as follows: ax² + bx + c = 0. 
# Write a function which calculates solution set of a quadratic equation, _solve_quadratic_eqn_.

print('''Ejercicio 7 nivel 1:
      La ecuación cuadrática se calcula de la siguiente manera: ax² + bx + c = 0. 
      Escriba una función que calcule el conjunto solución de una ecuación cuadrática, _solve_quadratic_eqn_.
''')

def solve_quadratic_eqn():

    A = float(input('Ingresa el numero A de tu ecuación cuadratica: '))
    B = float(input('Ingresa el numero B de tu ecuación cuadratica: '))
    C = float(input('Ingresa el numero C de tu ecuación cuadratica: '))
    x1 = (-B/2*A) 
    x2 = ((B**2 - 4*A*C)**.5)/(2*A)
    return f"El valor de x es igual a {x1} +- {x2}"

##8. Declare a function named print_list. 
# It takes a list as a parameter and it prints out each element of the list.

print('''Ejercicio 8 nivel 1:
      Declare una función llamada print_list. 
      Esta función toma una lista como parámetro e imprime cada elemento de la lista.
''')

def print_list():
    it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']   
    return ""

print(print_list())

##9. Declare a function named reverse_list. 
# It takes an array as a parameter and it returns the reverse of the array (use loops).

#```py
#print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
#print(reverse_list1(["A", "B", "C"]))
# ["C", "B", "A"]
#```

print('''Ejercicio 9 nivel 1:
      Declare una función llamada reverse_list. 
      Esta función toma una matriz como parámetro y devuelve su valor inverso (usando bucles).
''')

def reverse_list(*elemento):
    list_whatever = []
    for n in elemento[::-1]:
        list_whatever.append(n)
    return list_whatever

##10. Declare a function named capitalize_list_items. 
# It takes a list as a parameter and it returns a capitalized list of items

print('''Ejercicio 10 nivel 1:
      Declare una función llamada capitalize_list_items. 
      Esta toma una lista como parámetro y devuelve una lista de elementos en mayúsculas.
''')

def capitalize_list_items():
    phrase = input('Ingresa una frase que quieras que pase sus letras a mayusculas: ')
    phrase = str(phrase)
    print(phrase.upper())
    return""

##11. Declare a function named add_item. It takes a list and an item parameters. 
# It returns a list with the item added at the end.

#```py
#food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
#print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
#numbers = [2, 3, 7, 9]
#print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
#```

print('''Ejercicio 11 nivel 1:
      Declara una función llamada add_item. Esta toma como parámetros una lista y un elemento.
      Devuelve una lista con el elemento añadido al final.
''')

def add_item():
    item_list = []
    itemToAdd = str(input("Ingresa un elemento para agregar a la lista: "))
    item_list.append(itemToAdd)
    print(item_list)
    return""

##12. Declare a function named remove_item. It takes a list and an item parameters. 
# It returns a list with the item removed from it.

#```py
#food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
#print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
#numbers = [2, 3, 7, 9]
#print(remove_item(numbers, 3))  # [2, 7, 9]
#```

print('''Ejercicio 12 nivel 1:
      Declara una función llamada remove_item. 
      Esta toma como parámetros una lista y un elemento. Devuelve una lista con el elemento eliminado.
''')

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']

def removeItem(itemToRemove):
    food_staff.remove(itemToRemove)
    return""

##13. Declare a function named sum_of_numbers. 
# It takes a number parameter and it adds all the numbers in that range.

#```py
#print(sum_of_numbers(5))  # 15
#print(sum_of_numbers(10)) # 55
#print(sum_of_numbers(100)) # 5050
#```

print('''Ejercicio 13 nivel 1:
      Declara una función llamada suma_de_números. 
      Esta función toma un parámetro numérico y suma todos los números en ese rango.
''')

def sumOfNumbers():
    rang = int(input("Introduce un numero para hacer la suma de sus numeros en su rango: "))
    num = 0
    for i in range(rang+1):
        num += i 
    print(f"El numero que usted introdujo fue ({rang}) y su forma factorial es: {num}")
    return ""

print(sumOfNumbers())

##14. Declare a function named sum_of_odds. 
# It takes a number parameter and it adds all the odd numbers in that range.

print('''Ejercicio 14 nivel 1:
      Declare una función llamada suma_de_impares. 
      Esta función toma un parámetro numérico y suma todos los números impares en ese rango.
''')

def sumOfOdds(rang):
    parnum = []
    impnum = []
    for i in range(rang):
        if i % 2 == 0:
            parnum.append(i)
        else:
            impnum.append(i)
    
    return f"La suma de los numeros impares del 1 al {rang} es igual a ", sum(impnum)



##15. Declare a function named sum_of_even. 
#It takes a number parameter and it adds all the even numbers in that - range.

print('''Ejercicio 15 nivel 1:
      Declare una función llamada suma_de_pares. 
      Esta función toma un parámetro numérico y suma todos los números pares en ese rango.
''')

def sumOfeven(rang):
    parnum = []
    impnum = []
    for i in range(rang):
        if i % 2 == 0:
            parnum.append(i)
        else:
            impnum.append(i)
    
    return f"La suma de los numeros pares del 1 al {rang} es igual a ", sum(parnum)

print(sumOfeven(50))

### Exercises: Level 2

##1. Declare a function named evens_and_odds . 
# It takes a positive integer as parameter and it counts number of evens and odds in the number.

#```py
#    print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.
#```

print('''Ejercicio 1 nivel 2:
      Declare una función llamada evens_and_odds. 
      Esta función toma un entero positivo como parámetro y cuenta el número de pares e impares en el número.
''')

def evenAndOdds(rang):
    parnum = []
    impnum = []
    for i in range(rang):
        if i % 2 == 0:
            parnum.append(i)
        else:
            impnum.append(i)
    
    return f"La suma de los numeros pares e imppares del 1 al {rang} es igual a numeros pares {len(parnum)} y numeros impares {len(impnum)}"

print(evenAndOdds(100))

##2. Call your function factorial, 
# it takes a whole number as a parameter and it return a factorial of the number

print('''Ejercicio 2 nivel 2:
      Llama a tu función factorial, 
      toma un número entero como parámetro y devuelve un factorial del número.
''')

def factorial(f):
    
    f = int(f)
    if f <0:
        return "Es imposible debido a que el numero ingresado es 0 o es menor"
    result = 1
    for i in range(1, f + 1):
        result *= i 
    return result

numero = float(input("Ingroduce un numero que quieras convertir a factorial: "))
print(f"El factorial de {numero} es {factorial(numero)}")

##3. Call your function _is_empty_, 
# it takes a parameter and it checks if it is empty or not

print('''Ejercicio 3 nivel 2:
      Llama a tu función _is_empty_, 
      toma un parámetro y verifica si está vacío o no
''')

def is_empty(nposibleEmpty):
    if nposibleEmpty == "":
        print('La variable que usted ingreso esta vacio')
    else:
        print('Usted no ingreso ningun numero vacio')
    return

##4. Write different functions which take lists. 
# They should calculate_mean, calculate_median, calculate_mode, calculate_range, 
# calculate_variance, calculate_std (standard deviation).

print('''Ejercicio 4 nivel 2:
      Escriba diferentes funciones que acepten listas. 
      Estas funciones deben calcular la media, la mediana, 
      la moda, el rango, la varianza y la desviación estándar (desviación estándar).
''')

lst = []
for i in range(3):
    nwitem = float(input(f"Introduce un numero como item numero {i+1} para agregarlo a la lista, (se pueden repetir numeros): "))
    lst.append(nwitem)

def calculate_mean(lst):
    mean = sum(lst)/(len(lst))
    print(f"La media de la lista es {mean}")
    return""

def calculate_median(lst):
    lst.sort
    midlst = (len(lst)//2)
    print(lst[midlst])
    return""

def calculate_mode(lst):
    frequency = {}
    for num in lst:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    max_frequency = max(frequency.values())
    modes = [num for num, count in frequency.items() if count == max_frequency]
    
    if len(modes) == 1:
        print(f"La moda de la lista es {modes[0]} que se repite {max_frequency} veces")
    else:
        print(f"Hay múltiples modas: {', '.join(map(str, modes))} que se repiten {max_frequency} veces")
    
    return""

calculate_mode(lst)

def calculate_range():
    srtdlst = sorted(lst)
    gtrange = srtdlst[-1] - srtdlst[0]
    print(f"El rango de la lista es de {gtrange} empezando de {srtdlst[0]} llegando hasta {srtdlst[-1]}")
    return""

print(calculate_mean(lst))
print(calculate_median(lst))
print(calculate_mode(lst))
print(calculate_range())

### Exercises: Level 3

##1. Write a function called is_prime, which checks if a number is prime.

print('''Ejercicio 1 nivel 3:
      Escriba una función llamada is_prime, que verifique si un número es primo.
''')

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True

n = float(input('Ingresa un numero y te digo si es primo o no: '))
print(is_prime(n))

##2. Write a functions which checks if all items are unique in the list.

print('''Ejercicio 2 nivel 3:
      Escriba una función que verifique si todos los elementos son únicos en la lista.
''')

def allItemsUniqueinlst(lst):
    """Verifica si todos los elementos en una lista son únicos"""
    stlst = set(lst)
    allunique = len(lst) == len(stlst)
    
    if allunique:
        print("Todos los elementos de la lista son únicos")
    else:
        print("La lista contiene elementos repetidos")
    
    return allunique 


lst = []
for i in range(5):  
    nwitem = input(f"Introduce un nuevo item número {i+1}: ")
    lst.append(nwitem)  

resultado = allItemsUniqueinlst(lst)
print(f"Resultado booleano: {resultado}")

##3. Write a function which checks if all the items of the list are of the same data type.

print('''Ejercicio 3 nivel 3:
      Escriba una función que verifique si todos los elementos de la lista son del mismo tipo de datos
''')

def todos_mismo_tipo(lista):
    if not lista:  
        return True, "La lista está vacía"
    
    primer_tipo = type(lista[0])
    
    for elemento in lista[1:]:
        if type(elemento) != primer_tipo:
            return False, f"Tipos mezclados encontrados. Primer tipo: {primer_tipo}, tipo diferente: {type(elemento)}"
    
    return True, f"Todos los elementos son de tipo: {primer_tipo.__name__}"

lsttest = [True, False, 4]
print(todos_mismo_tipo(lsttest))

##4. Write a function which check if provided variable is a valid python variable

print('''Ejercicio 4 nivel 3:
      Escriba una función que verifique si la variable proporcionada es una variable de Python válida.
''')

posiblevariablepy = input('Ingresa una posible variable para python: ')
def valid_variablepy_simple(posiblevariablepy):
    if not posiblevariablepy or " " in posiblevariablepy:
        return False
    if not (posiblevariablepy[0].isalpha() or posiblevariablepy[0] == '_'):
        return False
    return True

print(valid_variablepy_simple(posiblevariablepy))

##5. Go to the data folder and access the countries-data.py file.

#- Create a function called the most_spoken_languages in the world. 
# It should return 10 or 20 most spoken languages in the world in descending order
#- Create a function called the most_populated_countries. 
# It should return 10 or 20 most populated countries in descending order.

print('''Ejercicio 5 nivel 3:
      Vaya a la carpeta de datos y acceda al archivo Countries-data.py.
- Cree una función llamada "most_spoken_languages ​​in the world".
- Debería devolver los 10 o 20 idiomas más hablados del mundo en orden descendente.
- Cree una función llamada "most_populated_countries".
- Debería devolver los 10 o 20 países más poblados en orden descendente.
''')

import datosPais as datac 

datos = datac.paises

def most_spoken_languages():
    countrylanguage = []
    for pais in datos:
        for lenguaje in pais['languages']:
            countrylanguage.append(lenguaje)
    setlanguages = set(countrylanguage)
    dictlanguages = {}
    for language in setlanguages:
        dictlanguages[language] = 0

    for idioma in dictlanguages:
        for pais in datos:  
            if idioma in pais['languages']:
                dictlanguages[idioma] = pais['population'] + dictlanguages[idioma]
    
    sortValuesLanguagespopulation = sorted(dictlanguages.values(), reverse= True)
    sorfkeyslanguagespopulation = sorted(dictlanguages, key= dictlanguages.get, reverse=True)
    
    print('Los 10 idiomas mas hablados en el mundo son (orden decendente)')
    for i in range(20):
        print(i+1, "-",sorfkeyslanguagespopulation[i] ,sortValuesLanguagespopulation[i])
    return""

print(most_spoken_languages())

