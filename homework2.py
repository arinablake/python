# Set a variable called total to 0.
# Ask the user to enter five numbers and after each input ask them if they want that number included.
# If they do, then add the number to the total. If they do not want it included, don’t add it to the total.
# After they have entered all five numbers, display the total.

total = 0
count = 0
while count < 5:
    num = int(input('Enter a number '))
    add = input('Do you want to add the number to the total ')
    if add == 'yes':
        total += num
    count += 1
print(f'The total is {total}')


# Ask which direction the user wants to count (up or down).
# If they select up, then ask them for the top number and then count from 1 to that number.
# If they select down, ask them to enter a number below 20 and then count down from 20 to that number.
# If they entered something other than up or down, display the message “I don’t understand”.

direction = input('In which direction do you want to count (up or down)? ')
if direction == 'up':
    up = int(input('What is a top number? '))
    range_up = range(1, up + 1)
    for i in range_up:
        print(i)
elif direction == 'down':
    down = int(input('Enter a number below 20 '))
    range_down = range(20, down - 1, -1)
    for i in range_down:
        print(i)
else:
    print('I don’t understand')
#
# Ask how many people the user wants to invite to a party.
# If they enter a number below 10, ask for the names and after each name display “[name] has been invited”.
# If they enter a number which is 10 or higher, display the message “Too many people”.

party_ppl = int(input('How many people do you want to invite to a party? '))
count = 0
if party_ppl < 10:
    while count < party_ppl:
        name = input('Enter the name of the guest ')
        print(f'{name} has been invited')
        count += 1
else:
    print(f'Too many people')


# Set the total to 0 to start with.
# While the total is 50 or less, ask the user to input a number.
# Add that number to the total and print the message “The total is… [total]”.
# Stop the loop when the total is over 50.

total = 0
while total <= 50:
    num = int(input('Enter a number '))
    total += num
    print(f'The total is {total}')


# Ask the user to enter a number.
# Keep asking until they enter a value over 5
# and then display the message “The last number you entered was a [number]” and stop the program.


num = int(input('Enter a number '))
while num <= 5:
    num = int(input('Enter a number '))
print(f'The last number you entered was {num}')


# Ask the user to enter a number and then enter another number.
# Add these two numbers together and then ask if they want to add another number.
# If they enter “y", ask them to enter another number and keep adding numbers until they do not answer “y”.
# Once the loop has stopped, display the total.

num1 = int(input('Enter a number '))
num2 = int(input('Enter a number '))
sum = num1 + num2
add = input('Do you want to add another number? ')
while add == 'y':
    num = int(input('Enter a number '))
    add = input('Do you want to add another number? ')
    sum += num
print(f'Total is {sum}')


# Ask for the name of somebody the user wants to invite to a party.
# After this, display the message “[name] has now been invited” and add 1 to the count.
# Then ask if they want to invite somebody else.
# Keep repeating this until they no longer want to invite anyone else to the party
# and then display how many people they have coming to the party.

count = 0
name = input('Enter the name of the guest you want to invite to the party ')
print(f'{name} has now been invited')
count += 1
add = input('Do you want to invite somebody else? ')
while add == 'yes':
    name = input('Enter the name of the guest you want to invite to the party ')
    print(f'{name} has now been invited')
    add = input('Do you want to invite somebody else? ')
    count += 1
print(f'{count} people are coming to the party')


# Ask the user to enter a number between 10 and 20.
# If they enter a value under 10, display the message “Too low” and ask them to try again.
# If they enter a value above 20, display the message “Too high” and ask them to try again.
# Keep repeating this until they enter a value that is between 10 and 20 and then display the message “Thank you”.

num = int(input('Enter a number between 10 and 20 '))
while num < 10:
    print(f'Too low. Try again.')
    num = int(input('Enter a number between 10 and 20 '))
while num > 20:
    print(f'Too high. Try again.')
    num = int(input('Enter a number between 10 and 20 '))
else:
    print(f'Thank you')

# Write a Python program to sum all the items in a list.

list = [1, 2, 3, 4, 5, 6]
sum = 0
for item in list:
    sum += item
print(sum)

# Write a Python program to multiplies all the items in a list.

list = [1, 2, 3, 4, 5, 6]
mult = 1
for item in list:
    mult *= item
print(mult)

# Write a Python program to get the largest number from a list.

list = [11, 42, 3, -4, 15, 6]
max = list[0]
for item in list:
    if item > max:
        max = item
print(max)

# Write a Python program to get the smallest number from a list

list = [11, 42, 3, -4, 15, -60]
min = list[0]
for item in list:
    if item < min:
        min = item
print(min)

# Write a Python program to remove duplicates from a list.

list = [11, 42, 3, 11, -4, 15, -60, 3]
new_list = []
for item in list:
    if item not in new_list:
        new_list.append(item)
print(new_list)

# Write a Python program to check a list is empty or not.

list = []
if len(list) == 0:
    print(f'The list is empty')
else:
    print(f'The list is not empty')

# Write a Python function that takes two lists and returns True if they have at least one common member.

def common(list1, list2):
    for item in list1:
        if item in list2:
            return True
    else:
        return False
print(common([2, 3, 7, 11, 8], [1, 4, 5, 9, 7]))

# Write a Python program to get unique values from a list.

list = [1, 4, 5, 9, 7, 5, 3, 4, 5]
new_list = []
for item in list:
    if item not in new_list:
        new_list.append(item)
print(new_list)


list = [1, 4, 5, 9, 7, 5, 3, 4, 5]
new_list = []
for item in list:
    if list.count(item) == 1:
        new_list.append(item)
print(new_list)

# Write a Python program to select the odd items of a list.

list = [1, 4, 5, 9, 7, 5, 3, 4, 5]
new_list = []
for item in list:
    if item % 2 != 0:
        new_list.append(item)
print(new_list)

# Write a Python program to concatenate elements of a list

list = [1, 4, 5, 9, 7, 5, 3, 4, 5]
concat = ''
for item in list:
    concat += str(item)
print(concat)
