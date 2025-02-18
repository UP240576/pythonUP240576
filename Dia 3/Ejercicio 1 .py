##1. Declare your age as integer variable
age = int(input("Ingresa tu edad en numeros "))

##2. Declare your height as a float variable
height = float(input("Ingresa tu altura en numeros ")) 

##3. Declare a variable that store a complex number
comnum = float(input("Ingresa un numero complejo"))

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
radio = float(input("Ingresa el radio de tu circulo"))
areac = (radio**2)*pi
circumference = 2*pi*radio
print("El area de tu circulo es ", areac)
print("La circunferencia de tu circulo es ", circumference)
















