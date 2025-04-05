### Exercises: Level 2

##1. Use map to create a new list by changing each country to uppercase in the countries list

print('''Ejercicio 1 nivel 2
      Utilice el mapa para crear una nueva lista cambiando cada país a mayúscula en la lista de países.
''')

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def uppercase (country):
    return country.upper()
result=map(uppercase, countries)

print(list(result))

##2. Use map to create a new list by changing each number to its square in the numbers list

print('''Ejercicio 2 nivel 2
      Utilice el mapa para crear una nueva lista cambiando cada número por su cuadrado en la lista de números
''')

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def square_num (num):
    return num**2

result=map(square_num, numbers)
print(list(result))

##3. Use map to change each name to uppercase in the names list

print('''Ejercicio 3 nivel 2
      Utilice el mapa para cambiar cada nombre a mayúsculas en la lista de nombres
''')

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']

def uppercase_name(name):
    return name.upper()

resul=map(uppercase_name, names)
print(list(resul))

##4. Use filter to filter out countries containing 'land'.

print('''Ejercicio 4 nivel 2
      Utilice el filtro para filtrar los países que contienen la palabra "tierra".
''')

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def lan_country (country):
    if 'land' in country:
        return True
    return False

result= filter(lan_country, countries)
print(list(result))

##5. Use filter to filter out countries having exactly six characters.

print('''Ejercicio 5 nivel 2
      Utilice el filtro para filtrar países que tengan exactamente seis caracteres.
''')

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def six_ch_country(ch):
    if len(ch)==6:
        return True
    return False

result=filter(six_ch_country,countries )
print(list(result))

##6. Use filter to filter out countries containing six letters and more in the country list.

print('''Ejercicio 6 nivel 2
      Utilice el filtro para filtrar los países que contengan seis letras o más en la lista de países.
''')

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def six_ch_or_more_country(pais):
    if len(pais)>=6:
        return True
    return False

result=filter(six_ch_or_more_country, countries)
print(list(result))

##7. Use filter to filter out countries starting with an 'E'

print('''Ejercicio 7 nivel 2
      Utilice el filtro para filtrar los países que comienzan con 'E'
''')

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def countries_w_e(pais):
    return pais.startswith('E')

result=(filter(countries_w_e,countries ))
print(list(result))

##8. Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))

print('''Ejercicio 8 nivel 2
      Encadenar dos o más iteradores de lista (por ejemplo, arr.map(callback).filter(callback).reduce(callback))
''')

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

from functools import reduce
resultado=( lambda x, y: x + y,map(lambda x: x * 2, filter(lambda x: x % 2 == 0, numbers)))
print(resultado)

##9. Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.

print('''Ejercicio 9 nivel 2
      Declare una función llamada get_string_lists que toma una lista como parámetro y luego devuelve una lista que contiene solo elementos de cadena.
''')

lista = [1,2,3,'LETRAS','Paulo','palabras']

def get_string_list(list):
    return[cosa for cosa in lista if isinstance(cosa, str)]

resultado=get_string_list(lista)
print(resultado)

##10. Use reduce to sum all the numbers in the numbers list.

print('''Ejercicio 10 nivel 2
      Utilice reducir para sumar todos los números en la lista de números
''')

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def add_num (x,y):
    return int(x) + int(y)

suma=reduce(add_num, numbers)
print(suma)

##11. Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries

print('''Ejercicio 11 nivel 2
      Utilice reduce para concatenar todos los países y producir esta oración: Estonia, Finlandia, Suecia, Dinamarca, Noruega e Islandia son países del norte de Europa.
''')

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def pais_sentence(x,y):
    return x + ', ' + y 

oracion=reduce(pais_sentence,countries )
oracion1= oracion+'los paises son de Europa '
print(oracion1)

##12. Declare a function called categorize_countries that returns a list of countries with some common pattern
#  (you can find the [countries list](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py)
#  in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).

print('''Ejercicio 12 nivel 2
      Declare una función llamada categorize_countries que devuelva una lista de países con algún patrón común (puede encontrar la 
      [lista de países](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py)
      en este repositorio como Countries.js (por ejemplo, 'land', 'ia', 'island', 'stan')).
''')

from countries import countries 

def categorize_countries(countries , pattern):
    return list(filter(lambda pais: pattern in pais.lower(),countries))

print(categorize_countries(countries,'land'))

##13. Create a function returning a dictionary, where keys stand for starting letters of 
# countries and values are the number of country names starting with that letter.

print('''Ejercicio 13 nivel 2
      Crea una función que devuelva un diccionario, donde las claves representan las letras 
      iniciales de los países y los valores son la cantidad de nombres de países que comienzan con esa letra.
''')

def count_countries_initial(countries ):
    return dict(map(lambda letter: (letter, sum(1 for country in countries if country.startswith(letter))), sorted(set(map(lambda x: x[0], countries)))))

print(count_countries_initial(countries))

##14. Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.

print('''Ejercicio 14 nivel 2
      Declare una función get_first_ten_countries: 
      devuelve una lista de los primeros diez países de la lista Countries.js en la carpeta de datos.
''')

def get_first_ten():
    ten= [p for p in countries[:10]]
    return ten

print(get_first_ten())


##15. Declare a get_last_ten_countries function that returns the last ten countries in the countries list.

print('''Ejercicio 15 nivel 2
      Declare una función get_last_ten_countries que devuelva los últimos diez países de la lista de países.
''')

def get_last_ten():
    ten= [p for p in countries[-10:]]
    return ten

print(get_last_ten())
