### Exercises: Level 3

##1. Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
#   - Sort countries by name, by capital, by population
#   - Sort out the ten most spoken languages by location.
#   - Sort out the ten most populated countries.

import datosPais  as paises 

def name(pais):
    return pais['name']

def capital (pais):
    return pais['capital']

def population(pais):
    return pais ['population']

def sortnames (paises):
    return sorted(paises, key=name)

def sortcapital (paises):
    return sorted(paises, key=capital)

def srtpopulation(paises,reverse=False):
    return sorted(paises, key=population,reverse=reverse)

listapaises=paises.paises
ordenated_name= (sortnames(listapaises))
print(ordenated_name)#por orden alfabetico
for pais in ordenated_name:
    print(pais['name'])
ordenate_capital=(sortcapital(listapaises))
print(ordenate_capital)
for capital in ordenate_capital:
    print(capital['capital'])

ordenate_poblation=(srtpopulation(listapaises))
print(ordenate_poblation)
for population in ordenate_poblation:
    print(population['name'],population['population'] )

from collections import Counter
def toptenidioms():
    idioms=[]
    for pais in paises.paises:
        if 'languages' in pais:
            idioms.extend(pais['languages'])
    toptenidiom=Counter(idioms).most_common(10)
    return toptenidiom
def show_top_ten():
    topten=toptenidioms()
    print('los 10 idiomas mas hablados son: ')
    for idiom, count in topten:
        print(f'{idiom}:{count}')
(show_top_ten())

def paises_mas_poblados():
    sortpaises=sorted(paises.paises, key= lambda pais: pais['population'], reverse=True)
    return sortpaises[:10]
def show_ten_most_poblated():
    top10paises=paises_mas_poblados()
    print('the most poblated countries are: ')
    for pais in top10paises:
        print(f'{pais['name']}:{pais['population']}')
show_ten_most_poblated()