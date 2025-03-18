 ## 💻 Exercises: Day 8

##1. Create  an empty dictionary called dog

print('Ejercicio 1')

dogdct = {}     #Dictionary called dog
print(dogdct)

##2. Add name, color, breed, legs, age to the dog dictionary

print('Ejercicio 2')

dogdct ['Name'] = 'Jake'
dogdct ['Color'] = 'Yellow'
dogdct ['Breed'] = 'Bulldog England'
dogdct ['Legs'] = '4'
dogdct ['Age'] = '34'
print(dogdct)

##3. Create a student dictionary and add first_name, last_name, gender, age,
# marital status, skills, country, city and address as keys for the dictionary

print('Ejercicio 3')

studentdct = {
    'First name': 'Leonardo',
    'Last name': 'Zamora',
    'Gender': 'male',
    'Age': '19',
    'Material Status': 'Single',
    'Skills': ['Beginer in cybersecutity', 'Beginer in python', 
    'Support and maintenance technician', 'B1 basic in english'],
    'Address': {'State':'Aguascalientes', 
                'City': 'Ags', 
                'Neighborhood': 'Mision de Santa Fe',
                'Street':'Estrella 456'}
}
print(studentdct)

##4. Get the length of the student dictionary

print('Ejercicio 4')

print(len(studentdct))

##5. Get the value of skills and check the data type, it should be a list

print('Ejercicio 5')

print(studentdct.get('Skills'))

##6. Modify the skills values by adding one or two skills

print('Ejercicio 6')

studentdct['Skills'].extend(['Autodidact', 'Smart'])
print(studentdct)

##7. Get the dictionary keys as a list

print('Ejercicio 7')

studntkeys = studentdct.keys()
print(studntkeys)

##8. Get the dictionary values as a list

print('Ejercicio 8')

studentvalues = studentdct.values()
print(studentvalues)

##9. Change the dictionary to a list of tuples using _items()_ method

print('Ejercicio 9')

studentlist = studentdct.items()
print(studentlist)

##10. Delete one of the items in the dictionary

print('Ejercicio 10')

del studentdct['Skills']
print(studentdct)

##11. Delete one of the dictionaries

print('Ejercicio 11')

del dogdct
print(dogdct)