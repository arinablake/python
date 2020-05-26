# Ask for the total price of the bill, then ask how many diners there are.
# Divide the total bill by the number of diners and show how much each person must pay.

bill_total = float(input('What is a bill total?'))
diners = int(input('How many diners are?'))
each_person_pays = bill_total / diners
print(f'Each person has to pay {round(each_person_pays, 2)}')

# Write a program that will ask for a number of days and
# then will show how many hours, minutes and seconds are in that number of days.

num_days = int(input('Enter the number of days '))
hours = num_days * 24
minutes = hours * 60
seconds = minutes * 60
print(f'In {num_days} days: {hours} hours, {minutes} minutes, {seconds} seconds')

# Task the user to enter a number over 100 and then enter a number under 10
# and tell them how many times the smaller number goes into the larger number in a user-friendly format.

num1 = int(input('Enter the number over 100 '))
num2 = int(input('Enter the number under 10 '))
times_bigger = num1 // num2
print(f'{num2} goes into {num1} {times_bigger} times ')

# Ask the integer number and return the second power of this number.

num = int(input('Enter an integer number '))
second_power = num ** 2
print(f'Second power of {num} is {second_power}')

# Ask the integer number and power what you would like to get. Return result

num = int(input('Enter an integer number '))
power = int(input('Enter the power '))
num_power = num ** power
print(f'{power} power of {num} is {num_power}')

# Ask the user to enter their first name and then display the length of their name.

name = input('Enter your first name ')
print(len(name))

# Ask the user to enter their first name and then ask them to enter their surname.
# Join them together with a space between and display the name and the length of the whole name.

first_name = input('Enter your first name ')
last_name = input('Enter your last name ')
name = f'{first_name} {last_name}'
print(f'{name} {len(name)}')

# Ask the user to enter their first name and surname in lower case.
# Change the case to title case and join them together. Display the finished result.

first_name = input('Enter your first name in lower case ')
last_name = input('Enter your last name in lower case ')
name = f'{first_name} {last_name}'
print(name.title())

# Enter a random string, which includes only digits.
# Write a function sum_digits which will find a sum of digits in this string

digits_string = input('Enter a random string, which includes only digits ')

result = 0
for i in digits_string:
    result += int(i)
print(result)

# Ask the user to enter their favorite color.
# If they enter “red”, “RED” or “Red” display the message “I like red too”,
# otherwise display the message “I don’t like [color], I prefer red”.

fav_color = input('Enter your favorite color ')
if fav_color == 'red' or fav_color == 'RED' or fav_color == 'Red':
    print('I like red too')
else:
    print(f'I don’t like {fav_color}, I prefer red')

# Ask the user’s age.
# If they are 18 or over, display the message “You can vote”,
# if they are aged 17, display the message “You can learn to drive”,
# if they are 16, display the message “You can buy a lottery ticket”,
# if they are under 16, display the message “You can go Trickor-Treating”.

age = int(input('What is your age? '))
if age >= 18:
    print('You can vote')
elif age == 17:
    print('You can learn to drive')
elif age == 16:
    print('You can buy a lottery ticket')
else:
    print('You can go Trickor-Treating')


# Ask the user to enter a number.
# If it is under 10, display the message “Too low”,
# if their number is between 10 and 20, display “Correct”, otherwise display “Too high”.

num = int(input('Enter a number '))
if num < 10:
    print('Too low')
elif num < 20:
    print('Correct')
else:
    print('Too high')

# Ask the user to enter 1, 2, or 3.
# If they enter a 1, display the message “Thank you”,
# if they enter a 2, display “Well done”,
# if they enter a 3, display “Correct”. If they enter anything else, display “Error message”.

num = int(input('Enter a number 1, 2, or 3 '))
if num == 1:
    print('Thank you')
elif num == 2:
    print('Well done')
elif num == 3:
    print('Correct')
else:
    print('Error message')
