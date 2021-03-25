"""
Exercise 2: Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.

Enter a number: 4
Enter a number: 5
Enter a number: bad data
Invalid input
Enter a number: 7
Enter a number: done
16 3 5.333333333333333
"""

count = 0
total = 0
largest = None
smallest = None

while True:
    number = input('Enter a number: ')
    try:
        total = float(total) + float(number)
        count = count + 1
        if largest is None or number > largest:
            largest = number
        if smallest is None or number < smallest:
            smallest = number
    except:
        if number == 'done':
            break
        else:
            print('Invalid input')

print('count: ', count)
print('total: ', total)
print('average: ', float(total) / float(count))
print('largest: ', largest)
print('smallest: ', smallest)
