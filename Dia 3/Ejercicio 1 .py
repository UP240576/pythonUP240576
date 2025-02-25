##1. Declare your age as integer variable
age = int(input("Ingresa tu edad en numeros "))

##2. Declare your height as a float variable
height = float(input("Ingresa tu altura en numeros ")) 

##3. Declare a variable that store a complex number
comnum = float(input("Ingresa un numero complejo "))

##4. Ejercicio 1 (crear una vaiable que determina)
# Escribe un scrip que permita al usuario entregar una base y una altura de un 
# triangulo y calcular la area de ese triangulo (area = 0.5 x b x h)

base = float(input("Ingresa la base de tu triangulo "))
altura = float(input("Ingresa la altura de tu triangulo "))
area = 0.5 * base * altura 
print ("La area de tu triangulo es de ", area) 

##5. Write a script that prompts the user to enter side a, side b, and side c of 
# the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).

sideA = float(input("Ingresa la medida del lado A "))
sideB = float(input("Ingresa la medida de tu lado B "))
sideC = float(input("Ingresa la medida de tu lado C "))
perimetro = sideA + sideB + sideC 
print("El perimetro de tu area es de ", perimetro)

##6. Get length and width of a rectangle using prompt.
# Calculate its area (area = length x width) and perimeter 
# (perimeter = 2 x (length + width))

Length = float(input("Ingresa el largo de tu rectangulo "))
Width = float(input("Ingresa el ancho de tu rectangulo "))
arear = Length * Width 
perimeter = 2*(Length + Width)
print("El area de tu rectangulo es de ", arear)
print("El perimetro de tu rectangulo es de ", perimeter) 

##7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) 
# and circumference (c = 2 x pi x r) where pi = 3.14.
pi = 3.14159
radio = float(input("Ingresa el radio de tu circulo "))
areac = (radio**2)*pi
circumference = 2*pi*radio
print("El area de tu circulo es ", areac)
print("La circunferencia de tu circulo es ", circumference)

##8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
m = 2
b = -2 
slope = -b/m 
print("Su pendiente es de ", m)
print("Su intercepcion en x es en ", slope)
print("Su intercepcion en y es de ", b)

##9. Slope is (m = y2-y1/x2-x1). Find the slope and [Euclidean distance]
# (https://en.wikipedia.org/wiki/Euclidean_distance#:~:text=In%20mathematics%2C%20the%20Euclidean%20distance,being%20called%20the%20Pythagorean%20distance.) 
# between point (2, 2) and point (6,10) 
x1 = 2
y1 = 2
x2 = 6
y2 = 10
h = ((y1+y2)**2+(x1+x2)**2)**.5
m1 = (y2-y1)/(x2-x1)
print("Su intercepcion es en ", m1)
print("Su distacia es de ", h)

##10. Compare the slopes in tasks 8 and 9.Compare the slopes in tasks 8 and 9.
difSlopet8 = slope - m1 
difSlopet9 = m1 - slope 
print("La diferencia entre la pendiente de la tarea 8 y la tarea 9 es de ", difSlopet8)
print("La diferencia entre la pendiente de la tarea 9 y la tarea 8 es de ", difSlopet9)
 

##11. Calculate the value of y (y = x^2 + 6x + 9).
#  Try to use different x values and figure out at what x value y is going to be 0.
x = float(input("Coloca un numeor que sea X para obtener Y: "))
a = 2
b = 6
c = 9 
y = x**a + x*b + c 
print("Tu valor de Y es: ", y)

##12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.

lenPython =  len("python")
lenDragon = len("dragon")
lenngth = lenPython - lenDragon
print ("La longitud de la palabra python es de: ", lenPython)
print ("La longitud de la palabra dragon es de: ", lenDragon)
print ("La diferencia entre la palabra python y dragon es de: ", Length)

##13. Use _and_ operator to check if 'on' is found in both 'python' and 'dragon'.
onCheck = "on" in "python"
oninDragon = "on" in "dragon"
print ("La palabra on se encuentra en ", onCheck, oninDragon)

##14. I hope this course is not full of jargon_. 
# Use _in_ operator to check if _jargon_ is in the sentence.
frase = input("Inserta una oracion ")
if "jargon" in frase: 
    print ("La palabra jargon se encuentra en su oracion")
else: 
    print("La palabra jargon no se encuentra en su oracion")

##15. There is no 'on' in both dragon and python.

chonin = "dragon and python"
if "on" in chonin:
    print("La palabra on se encuentra tanto en la palabra python y dragon")
else:
    print("La palabra on no se encuentra en python o dragon")

##16. Find the length of the text _python_ and convert the value to float 
# and convert it to string

longthpy = len("python")
longthpy = float(longthpy)
print ("El tipo de la palabra python se enuentra en ", type(longthpy))
longthpy = str(longthpy)
print ("El tipo de la palabra python se enuentra en ", type(longthpy))

##17. Even numbers are divisible by 2 and the remainder is zero. 
# How do you check if a number is even or not using python?

num = float(input("Ingresa un numero "))
if ((num/2)= )





