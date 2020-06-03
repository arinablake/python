# Create a tuple containing the names of five countries and display the whole tuple.
# Ask the user to enter one of the countries that have been shown to them and then display the index number
# (i.e. position in the list) of that item in the tuple.


tuple1 = ('Russia', 'USA', 'UK', 'France', 'Italy')
print(tuple1)
country = input('Enter one of the countries that have been shown ')
if country in tuple1:
    index = tuple1.index(country)
    print(f'The index of {country} is {index}')
else:
    print("The country wasn't shown")


# Add to the previous program to ask the user to enter a number and display the country in that position.

tuple1 = ('Russia', 'USA', 'UK', 'France', 'Italy')
print(tuple1)
num = int(input('Enter a number < 5 '))
if -6 < num < 5:
    print(tuple1[num])
else:
    print("The index number doesn't exist")


# Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

dict1 = {0: 10, 1: 20}
dict1[2] = 30
print(dict1)


dict1 = {0: 10, 1: 20}
dict1.update({2: 30})
print(dict1)


# Write a Python program to iterate over dictionaries using for loops.

kids = {'Anna': 10, 'Tom': 18, 'Harry': 14, 'Katya': 16}
for key, value in kids.items():
    print(f'{key} is {kids[key]}')


# Write a Python script to merge two Python dictionaries.

kids1 = {'Anna': 10, 'Tom': 18, 'Harry': 14, 'Katya': 16}
kids2 = {'Mark': 15, 'Alisa': 12}
kids1.update(kids2)
print(kids1)


# Write a Python program to remove duplicates from the Dictionary.

kids1 = {'Anna': 10, 'Katya': 16, 'Mark': 15, 'Tom': 18, 'Harry': 14, 'Katya': 16, 'Sam': 11, 'Anna': 10, 'Denis': 18}
kids2 = {}
for key, value in kids1.items():
    if value not in kids2.values():
        kids2[key] = value
print(kids2)

# Write a Python program to remove spaces from dictionary keys.

kids1 = {'An  na': 10, 'Kat    ya': 16, 'M  ark': 15, 'Tom': 18, 'Har    ry': 14, 'Denis': 18}
kids2 = {key.replace(' ', ''): value for key, value in kids1.items()}
print(kids2)

# Write a Python program to get the maximum and minimum value in a dictionary.

kids1 = {'Anna': 8, 'Katya': 16, 'Mark': 15, 'Tom': 20, 'Harry': 14, 'Denis': 18}
max_val = max(kids1)
print(kids1[max_val])
min_val = min(kids1)
print(kids1[min_val])

# Write a Python program to check a dictionary is empty or not.

dict1 = {}
if len(dict1) == 0:
    print('Empty dictionary')
else:
    print('Dictionary is not empty')


# Write a Python program to combine two dictionary adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

for key in d1:
    if key in d2:
        d2[key] = d1[key] + d2[key]
else:
    d2[key] = d1[key]
print(d2)


# Write a Python program to print a dictionary line by line.

kids1 = {'Anna': 8, 'Katya': 16, 'Mark': 15, 'Tom': 20, 'Harry': 14, 'Denis': 18}
for x, y in kids1.items():
    print(x, y)


###### Rewrite all exercises using functions

# Create a tuple containing the names of five countries and display the whole tuple.
# Ask the user to enter one of the countries that have been shown to them and then display the index number
# (i.e. position in the list) of that item in the tuple.


tuple1 = ('Russia', 'USA', 'UK', 'France', 'Italy')
print(tuple1)
country1 = input('Enter one of the countries that have been shown ')
def country_index(country):
    if country in tuple1:
        index = tuple1.index(country)
        print(f'The index of {country} is {index}')
    else:
        print("The country wasn't shown")
country_index(country1)


# Add to the previous program to ask the user to enter a number and display the country in that position.

tuple1 = ('Russia', 'USA', 'UK', 'France', 'Italy')
print(tuple1)
num1 = int(input('Enter a number < 5 '))
def country_num(num):
    if -6 < num < 5:
        print(tuple1[num])
    else:
        print("The index number doesn't exist")
country_num(num1)


# Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}


dict1 = {0: 10, 1: 20}
def add_to_dict(dict):
    dict[2] = 30
    return dict

print(add_to_dict(dict1))

# Write a Python program to iterate over dictionaries using for loops.

kids = {'Anna': 10, 'Tom': 18, 'Harry': 14, 'Katya': 16}

def iter_dict(dict):
    for key, value in dict.items():
        print(f'{key} is {dict[key]}')

iter_dict(kids)

# Write a Python script to merge two Python dictionaries.

kids1 = {'Anna': 10, 'Tom': 18, 'Harry': 14, 'Katya': 16}
kids2 = {'Mark': 15, 'Alisa': 12}


def merge_dict(dict1, dict2):
    dict1.update(dict2)
    return dict1

print(merge_dict(kids1, kids2))

# Write a Python program to remove duplicates from the Dictionary.

kids1 = {'Anna': 10, 'Katya': 16, 'Mark': 15, 'Tom': 18, 'Harry': 14, 'Katya': 16, 'Sam': 11, 'Anna': 10, 'Denis': 18}
kids2 = {}

def remove_dup(dict1, dict2):
    for key, value in dict1.items():
        if value not in dict2.values():
            dict2[key] = value
    return dict2
print(remove_dup(kids1, kids2))

# Write a Python program to remove spaces from dictionary keys.

kids1 = {'An  na': 10, 'Kat    ya': 16, 'M  ark': 15, 'Tom': 18, 'Har    ry': 14, 'Denis': 18}
kids2 = {}

def remove_space(dict1, dict2):
    dict2 = {key.replace(' ', ''): value for key, value in dict1.items()}
    return dict2

print(remove_space(kids1, kids2))


# Write a Python program to get the maximum and minimum value in a dictionary.

kids1 = {'Anna': 8, 'Katya': 16, 'Mark': 15, 'Tom': 20, 'Harry': 14, 'Denis': 18}

def max_val(dict):
    max_val = max(dict)
    return dict[max_val]
print(max_val(kids1))

def min_val(dict):
    min_val = min(dict)
    return dict[min_val]
print(min_val(kids1))


# Write a Python program to check a dictionary is empty or not.

dict1 = {}
def empty_dic(dict):
    if len(dict1) == 0:
        print('Empty dictionary')
    else:
        print('Dictionary is not empty')
empty_dic(dict1)


# Write a Python program to combine two dictionary adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})


d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

def comm_keys(dict1, dict2):
    for key in dict1:
        if key in dict2:
            dict2[key] = dict1[key] + dict2[key]
    else:
        dict2[key] = dict1[key]
        return dict2
print(comm_keys(d1, d2))


# Write a Python program to print a dictionary line by line.

kids1 = {'Anna': 8, 'Katya': 16, 'Mark': 15, 'Tom': 20, 'Harry': 14, 'Denis': 18}
def line_by_line(dict):
    for x, y in dict.items():
        print(x, y)
line_by_line(kids1)