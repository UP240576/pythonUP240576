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
print(addTwoNumbers())

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
print(areaDeUnCirculo())

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
        
add_all_nums()

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
print(conv_C_to_F())

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
        return
print(check_season())

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

print(calculate_slope())

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

print(solve_quadratic_eqn())

##8. Declare a function named print_list. 
# It takes a list as a parameter and it prints out each element of the list.

print('''Ejercicio 8 nivel 1:
      Declare una función llamada print_list. 
      Esta función toma una lista como parámetro e imprime cada elemento de la lista.
''')

def print_list():
    it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
    return it_companies

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

def reverse_list():
    list_whatever = []
    for n in list_whatever:
        list_whatever.insert(0,n)
        return""

##10. Declare a function named capitalize_list_items. 
# It takes a list as a parameter and it returns a capitalized list of items

print('''Ejercicio 10 nivel 1:
      Declare una función llamada capitalize_list_items. 
      Esta toma una lista como parámetro y devuelve una lista de elementos en mayúsculas.
''')

def capitalize_list_items():
    

##11. Declare a function named add_item. It takes a list and an item parameters. 
# It returns a list with the item added at the end.

#```py
#food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
#print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
#numbers = [2, 3, 7, 9]
#print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
#```

print('''Ejercicio 11 nivel 1:
      
''')



##12. Declare a function named remove_item. It takes a list and an item parameters. 
# It returns a list with the item removed from it.

#```py
#food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
#print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
#numbers = [2, 3, 7, 9]
#print(remove_item(numbers, 3))  # [2, 7, 9]
#```

print('''Ejercicio 12 nivel 1:
      
''')



##13. Declare a function named sum_of_numbers. 
# It takes a number parameter and it adds all the numbers in that range.

#```py
#print(sum_of_numbers(5))  # 15
#print(sum_of_numbers(10)) # 55
#print(sum_of_numbers(100)) # 5050
#```

print('''Ejercicio 13 nivel 1:
      
''')



##14. Declare a function named sum_of_odds. 
# It takes a number parameter and it adds all the odd numbers in that range.

print('''Ejercicio 14 nivel 1:
      
''')

##15. Declare a function named sum_of_even. 
#It takes a number parameter and it adds all the even numbers in that - range.

print('''Ejercicio 15 nivel 1:
      
''')

### Exercises: Level 2

##1. Declare a function named evens_and_odds . 
# It takes a positive integer as parameter and it counts number of evens and odds in the number.

#```py
#    print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.
#```

print('''Ejercicio 1 nivel 2:
      
''')



##2. Call your function factorial, 
# it takes a whole number as a parameter and it return a factorial of the number

print('''Ejercicio 2 nivel 2:
      
''')



##3. Call your function _is_empty_, 
# it takes a parameter and it checks if it is empty or not

print('''Ejercicio 3 nivel 2:
      
''')



##4. Write different functions which take lists. 
# They should calculate_mean, calculate_median, calculate_mode, calculate_range, 
# calculate_variance, calculate_std (standard deviation).

print('''Ejercicio 4 nivel 2:
      
''')



### Exercises: Level 3

##1. Write a function called is_prime, which checks if a number is prime.

print('''Ejercicio 1 nivel 3:
      
''')



##2. Write a functions which checks if all items are unique in the list.

print('''Ejercicio 2 nivel 3:
      
''')



##3. Write a function which checks if all the items of the list are of the same data type.

print('''Ejercicio 3 nivel 3:
      
''')



##4. Write a function which check if provided variable is a valid python variable

print('''Ejercicio 4 nivel 3:
      
''')



##5. Go to the data folder and access the countries-data.py file.

#- Create a function called the most_spoken_languages in the world. 
# It should return 10 or 20 most spoken languages in the world in descending order
#- Create a function called the most_populated_countries. 
# It should return 10 or 20 most populated countries in descending order.

print('''Ejercicio 5 nivel 3:
      
''')


