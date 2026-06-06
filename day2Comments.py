" Built in Functions:" \
"print()" \
"len()" \
"type() " \
"Variables store data in computer memory" \
"Mnemonic variables: recommended" \
"   a name that is memorable: ex. Anduzzle" \
"variable: a memory address which data is stored" \
"a more descriptive language is preferred" \
"Python usually does: snake case (andy_mejia)" \
"Assigned a data type to a variable is called variable declaration"""
# Variables in Python
first_name = 'Asabeneh'

print('First name:', first_name)
print('First name length:', len(first_name))

last_name, country, age, is_married = 'Yetayeh', 'Helsink', 250, True
print('Last Name:', last_name)
print('Country', country)
print('Age', age)
print('Married: ', is_married)

age= input('How old are you? ')
print(age)

num_int=10
print('num_int', num_int)
num_float=float(num_int)
print('num_float: ', num_float)

gravity = 9.81
print(int(gravity))

num_str = '10.6'
num_float = float(num_str)
num_int = int(num_float)
print('num_int', int(num_str))
print('num_float', float(num_str))
num_int = int(num_float)
print('num_int', int(num_int))