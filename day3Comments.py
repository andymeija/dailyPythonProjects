"" " Boolean Data Types;" \
"The use of these data types will be clear once we start using the comparison operator;" \
"let's compare my progress wiht myself, not anyone else" \
"print(True) this means print true y" \
"Diff Arithmetic Operators fr" \
"addition(+): a + b" \
"subtraction(-): a - b" \
"multiplication(*): a * b" \
"division(/): a / b" \
"We also use Comparison operatrs to compare two values" \
"python uses:" \
"in: means if its true if it contains it" \
"Day 3 done, yay!"""
# Arithmetic Operations in Python
# integers
add_int = 1 + 2
print(f'Addition: {add_int}')
print('Subtraction: ', 2 - 1)
print('Multiplication: ', 2 * 3)
print('Division: ', 4 / 2)
print('Division: ', 6 / 2)
print('Division: ', 7 / 2)
print('Division without the remainder: ', 7 / 2)  # 3, gives without the floating number
print('Modulus: ', 3 % 2)
print('Exponentiation: ', 2 ** 3)
print('Floating Point Number, PI', 3.14)
print('Complex  number: ', 1 + 1j)
# Declaring the variable at the top first
a = 3
b = 2

# Arithmetic Operations and assigned the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

print(total)
print(diff)
print(product)
print(division)
print(remainder)
print(floor_division)
print(exponential)
print('== Addition, Subtraction, Multiplication, Division, Modulus ==')

num_one = 3
num_two = 4

# Calculating area of a circle
radius = 10
area_of_circle = 3.14 * radius ** 2
print('Area of a circle: ', area_of_circle)
# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle: ', area_of_rectangle)
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')

print(len('mango') == len('avocado'))
print(3 != 2)
print(2 <= 3)
print(3 >= 2)
print('True == True', True == True)
print('True == False: ', True == False)
print('A in Andy', 'A' in 'Andy')

# Logical Operators (and &&, or ||  not ~)
print(2 < 3 < 4)
print('True and True: ', True and True)
print(not not True)

Andy_age = 19
height = 5.10
jess_complex = 4 + 2j
# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle
base = int(input('Enter base: '))
height_triangle = int(input('Enter height: '))
area_of_triangle = int((base * height_triangle) * 1 / 2)
print(f'The area of this  triangle is {area_of_triangle}')
# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter
# of the triangle
side_a = int(input('Enter side a: '))
side_b = int(input('Enter side b: '))
side_c = int(input('Enter side c: '))
perimeter = side_c + side_b + side_a
print(f'The perimeter of the triangle is {perimeter}')

# Get length and width of a rectangle using prompt
length_rectangle = int(input('Enter length: '))
width_rectangle = int(input('Enter width: '))
perimeter_rectangle = int(2 * (width_rectangle + length_rectangle))
print(f'The perimeter of the rectangle is {perimeter_rectangle}')

# Get radius of a circle using prompt
radius_circle = int(input("Enter radius: "))
pi = 3.14
circ_circle = int(2 * radius_circle * pi)
area_circle = int(pi * radius_circle ** 2)
print(f'The area of the circle is {area_circle}\nThe circumference is {circ_circle}')
print(len('python') == len('dragon'))
print('on' in 'python' and 'on' in 'dragon')
print('jargon' in 'I hope this course is not full of jargon.')
print(not ('on' in 'dragon ' and 'on' in 'python'))
print(str(float(len('python'))))


def is_even(num):
    return num % 2 == 0


print(is_even(6))
print((7 // 3) == int(2.7))
print(type('10') == type(10))
print(int('9') == 10)
hours = int(input(('Enter hours: ')))
rate_ph = int(input(('Enter rate per hour: ')))
weekly_earning = hours * rate_ph
print(weekly_earning)
num_years = int(input("Enter number of years you have lived: ")) * 60 * 60 * 24 * 365
print(f'You have lived for {num_years}')
print('1 1 1 1\n2 1 2 4 8\n3 1 3 9 27\n4 1 4 16 64\n5 1 5 25 125')
