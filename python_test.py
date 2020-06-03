# Input your age.
# If you are 18 or over, print the message “You can vote”,
# if you are aged 17, print the message “You can learn to drive”,
# if you are 16, print the message “You can buy a lottery ticket”,
# if you are under 16, print the message “You can go Trick-or-Treating”

# age = int(input('Enter your age '))
# if age >= 18:
#     print('You can vote')
# elif age == 17:
#     print('You can learn to drive')
# elif age == 16:
#     print('You can buy a lottery ticket')
# else:
#     print('You can go Trick-or-Treating')


# Enter a random string, which includes only digits.
# Write a function sum_digits which will find a sum of digits in this string.

string1 = input('Enter a random string, which includes only digits ')


def sum_digits(string):
    sum = 0
    for item in string:
        sum += int(item)
    print(sum)


sum_digits(string1)

# Write a Python program to get the largest number from a list.

# list = [2, 8, -10, 66, 24, -4, 91, 54]
# max = list[0]
# for item in list:
#     if item > max:
#         max = item
# print(max)
