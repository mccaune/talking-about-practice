"""
Exercise 4: Add code to the above program to figure out who has the most messages in the file. After all the data has been read and the dic- tionary has been created, look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has the most messages and print how many messages the person has.

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195
"""

d = {}
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.strip()
    words = line.split()
    if line.startswith('From:'): continue
    if line.startswith('From'):
        d[words[1]] = d.get(words[1], 0) + 1
#       if words[2] not in d:
#           d[words[2]] = 1
#       else:
#           d[words[2]] += 1
vals = list(d.values())
biggest_value = max (vals)
keys = list(d.keys())
print(keys[vals.index(max(vals))], ' ', biggest_value)
#print(d)
