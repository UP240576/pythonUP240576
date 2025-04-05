## Exercises: Level 2

##1- Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array 
# (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 
# 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).

print('''Ejercicio 1 nivel 2:
      Escriba una función llamada list_of_hexa_colors que devuelva cualquier número de colores hexadecimales en un array 
      (seis números hexadecimales escritos después de . El sistema de numeración hexadecimal se compone de 16 símbolos, 
      del 0 al 9 y las primeras 6 letras del alfabeto, de la a a la f. Consulte la tarea 6 para ver ejemplos de resultados).
''')

def list_of_hexa_colors(number=6):
    import random
    hxColor=[]
    for x in range(number):  
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))  
        hxColor.append(color) 
    return hxColor

print(list_of_hexa_colors())

##2- Write a function list_of_rgb_colors which returns any number of RGB colors in an array.

print('''Ejercicio 1 nivel 2:
      Escriba una función list_of_rgb_colors que devuelva cualquier número de colores RGB en una matriz.
''')

import random

def list_of_rgb_colors(n=3):
    rgb_colors = []
    for x in range(n):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        rgb_colors.append((r, g, b))
    return rgb_colors

print(list_of_rgb_colors(5))

##3- Write a function generate_colors which can generate any number of hexa or rgb colors.
   #generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
   #generate_colors('hexa', 1) # ['#b334ef']
   #generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
   #generate_colors('rgb', 1)  # ['rgb(33,79, 176)']

print('''Ejercicio 3 nivel 2
      Escriba una función generate_colors que pueda generar cualquier cantidad de colores hexadecimales o rgb.
''')

import random

colors=[]

def generate_colors(n=5, color_type='hex'):
    if color_type == "hex":
        for i in range(n): 
            color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
            colors.append(color)
    
    elif color_type == "rgb":
        for i in range(n):  
            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)
            colors.append((red, green, blue))
    
    else:

        return "Error: color_type debe ser 'hex' o 'rgb'"
    
    return colors

hex_colors = generate_colors(5, "hex")
print("Colores Hexadecimales:", hex_colors)
rgb_colors = generate_colors(5, "rgb")
print("Colores RGB:", rgb_colors)
print(generate_colors())
