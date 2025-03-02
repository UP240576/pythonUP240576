## 💻 Exercises: Day 6

### Exercises: Level 1

##1. Create an empty tuple

empty_tuple = tuple()

##2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)

brotherstpl = ('Erick', 'Alejandro', 'Pedro', 'Daniel', 'Rene', 'Sergio' )
sisterstpl = ('Cinthya', 'Karen', 'Pilar')

##3. Join brothers and sisters tuples and assign it to siblings

siblingstpl = brotherstpl + sisterstpl
print(siblingstpl)

##4. How many siblings do you have?

print('Tengo ', len(siblingstpl), ' hermanos y hermanas en total')

##5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members

parentstpl = ('Hector', 'Candy')
family_memberstpl = siblingstpl + parentstpl
print(family_memberstpl)

### Exercises: Level 2

#1. Unpack siblings and parents from family_members
#1. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
#1. Change the about food_stuff_tp  tuple to a food_stuff_lt list
#1. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
#1. Slice out the first three items and the last three items from food_staff_lt list
#1. Delete the food_staff_tp tuple completely
#1. Check if an item exists in  tuple:

del family_memberstpl

fruitptl = ('Strawberry', 'Banana', 'Mango', 'Pineapple', 'Apple', 'Orange')
vegetablestpl = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
animalProductstpl = ('Jam', 'Sausage', 'Milk', 'Chesse', 'Cream', 'Meat')

foodStuffTpl = fruitptl + vegetablestpl + animalProductstpl

print(foodStuffTpl[0:8] + foodStuffTpl[9:])
print(foodStuffTpl[3:-3])

del foodStuffTpl
print ('La fruta banana esta en el tuple (Fruits)? ','Banana' in fruitptl)

#- Check if 'Estonia' is a nordic country
#- Check if 'Iceland' is a nordic country

#  ```py
#  nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
#  ```

nordicCountries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estonia es un pais Nordico? ', 'Estonia' in nordicCountries)
print('Iceland es un pais Nordico? ', 'Iceland' in nordicCountries)
