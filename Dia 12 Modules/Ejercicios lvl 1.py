### Exercises: Level 1

##1. Writ a function which generates a six digit/character random_user_id.
#```py
#print(random_user_id());
#'1ee33d'
#```

print('''Ejercicio 1 nivel 1: 
      Escriba una función que genere un random_user_id de seis dígitos/caracteres
''')

def generate_random_user_id():
    import random
    import string
    user= ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, digit = 6))
    return user

print( generate_random_user_id())

##2. Modify the previous task. Declare a function named user_id_gen_by_user. 
# It doesn’t take any parameters but it takes two inputs using input(). 
# One of the inputs is the number of characters and the second input is the number of IDs which are 
# supposed to be generated.
#```py
#print(user_id_gen_by_user()) # user input: 5 5
#output:
#kcsy2
#SMFYb
#bWmeq
#ZXOYh
#2Rgxf

print('''Ejercicio 2 nivel 1: 
      Modifique la tarea anterior. Declare una función llamada user_id_gen_by_user. 
      No acepta parámetros, pero acepta dos entradas mediante input(). Una de las entradas 
      es el número de caracteres y la otra, el número de ID que se generarán.
''')

def user_id_by_user():
    import random
    import string
    ch=int(input('Ingrese el numero de caracteres: '))
    numID=int(input('Coloca la cantidad de numeros de User ID´s para generar: '))#cantidad de ID para generar
    userID= [''.join(random.choices(string.ascii_letters + string.digits+ string.punctuation, k=ch))for _ in range(numID)]
    return userID

print(user_id_by_user())

##3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
   
#```py
#print(rgb_color_gen())
# rgb(125,244,255) - the output should be in this form
#```

print('''Ejercicio 2 nivel 1: 
      Escriba una función llamada rgb_color_gen. 
      Esta generará colores RGB (tres valores de 0 a 255 cada uno).
''')

def rgb_color_gen():
    import random
    red=random.randint(0, 255)
    green=random.randint(0, 255)
    blue=random.randint(0, 255)
    return(red,green,blue)

print(rgb_color_gen)
