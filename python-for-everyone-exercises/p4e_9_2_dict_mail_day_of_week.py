"""
Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done. To do this look for lines that start with “From”, then look for the third word and keep a running count of each of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).

Sample Line:
From stephen.marquard@uct.ac.za Sat Jan

Sample Execution:
python dow.py
Enter a file name: mbox-short.txt
{'Fri': 20, 'Thu': 6, 'Sat': 1}
"""

d = {}
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.strip()
    words = line.split()
    if line.startswith('From:'): continue
    if line.startswith('From'):
        d[words[2]] = d.get(words[2], 0) + 1
#       if words[2] not in d:
#           d[words[2]] = 1
#       else:
#           d[words[2]] += 1
print(d)
