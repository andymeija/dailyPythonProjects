# Day 2: 30 Days of python programming
import math

first_name = 'Andy'
last_name = 'Mejia'
full_name = 'Andy Mejia'
country = 'Ecuador'
city = 'NYC'
age = 19
year = 2026
is_married = False
is_true = True
is_light_on = False
didi, loves, me = 'beautiful', False, 'Liam'
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(len(first_name))
print(len(first_name) == len(last_name))
num_one = 5
num_two = 4
total = num_two + num_one
diff = num_one - num_two
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two
# The radius of a circle is 30 meters
circum_of_circle = (60 * math.pi)
radius = input('Radius: ')
area_of_circle = (math.pi * (int(radius) ** 2))
print(area_of_circle)
input(f'{first_name}+{last_name}+{area_of_circle}')
