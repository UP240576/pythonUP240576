#### 💻 Exercises: Day 7

#   ```py
#   sets
#   it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
#   A = {19, 22, 24, 20, 25, 26}
#   B = {19, 22, 20, 25, 26, 24, 28, 27}
#   age = [22, 19, 24, 25, 26, 24, 25, 24]
#   ```

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

### Exercises: Level 1

##1. Find the length of the set it_companies

print('Las cantidad de compañias en it_commpanies es de: ', len(it_companies))

##2. Add 'Twitter' to it_companies

it_companies.add('Twitter')
print(it_companies)

##3. Insert multiple IT companies at once to the set it_companies

it_companies.update(['Intel', 'Nvidia', 'Amd', 'Radeon'])
print(it_companies)

##4. Remove one of the companies from the set it_companies

it_companies.remove('Apple')
print(it_companies)

##5. What is the difference between remove and discard

it_companies.remove('Amd')
it_companies.add('Qualcomm')
it_companies.remove('Qualcomm')
it_companies.discard('Samsung')
print(it_companies)

'''
this should give us an error and thats because we don´t have Qualcomm in the list
And here we don´t have any problem because discar is like an if
if we have samsung in the list discard discard it but in another
way it don´t give us an error
'''

### Exercises: Level 2

#1. Join A and B

A.update(B)
print(A)

#1. Find A intersection B

print(B.intersection(A))

#1. Is A subset of B

print(A.issubset(B))

#1. Are A and B disjoint sets

print(A.isdisjoint(B))

#1. Join A with B and B with A

A.update(B)
B.update(A)

#1. What is the symmetric difference between A and B

print('La diferencia entre A y B es: ', A.difference(B))
print('La diferencia entre B y A es: ', B.difference(A))

#1. Delete the sets completely

del A
del B

### Exercises: Level 3

#1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?

print('La cantidad de edades es de: ', len(age))
print('La edad maxima es de: ', max(age))
print('La edad minima es de: ', min(age))

#1. Explain the difference between the following data types: string, list, tuple and set

'''
Una string o cadena solo puede contener una palabra y que esta no se puede cambiar 
Una lista ya puede contener mas cadenas por asi decirlo y a su vez a esta se le puede quitar y agregar
contenido
Y En tuple no podemos modificarla y esta como las 2
y los set pueden estar ordenados como desordenados y se pueden acoplar a otros sin necesidad de que se
repitan strings
'''

#2. _I am a teacher and I love to inspire and teach people._ How many unique words have been used in the sentence? 
# Use the split methods and set to get the unique words.

phrace = ['Use', 'the', 'split', 'methods', 'and', 'set', 'to', 'get', 'the', 'unique', 'words']
print(phrace.symmetric_difference(phrace))

#🎉 CONGRATULATIONS ! 🎉
