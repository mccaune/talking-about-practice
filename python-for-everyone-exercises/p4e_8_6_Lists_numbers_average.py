"""
Exercise 6: Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers at the end when the user enters “done”. Write the program to store the numbers the user enters in a list and use the max() and min() functions to compute the maximum and minimum numbers after the loop completes.
"""


num_list = list()

while True:
    number = input('Enter a number: ')
    if number == 'done':
        break
    try:
        value = float(number)
    except:
        print('Invalid input')
        continue

    num_list.append(value)

print(len(num_list))
print(max(num_list))
print(min(num_list))
print(sum(num_list))
print(sum(num_list) / len(num_list))
