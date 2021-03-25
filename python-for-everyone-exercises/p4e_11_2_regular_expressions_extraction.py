'''
# Exercise 11.2
Exercise 2: Write a program to look for lines of the form:
New Revision: 39772 Extract the number from each of the lines using a regular expression and the findall() method. Compute the average of the numbers and print out the average as an integer.

Enter file:mbox.txt
38549

Enter file:mbox-short.txt
39756
'''

import re
lst = list()
count = 0
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^New Revision.* ([0-9]+)', line)
    if len(x) > 0: lst.append(float(x[0]))

#print(lst)
print(len(lst))
print(sum(lst))
print(sum(lst) / len(lst))
