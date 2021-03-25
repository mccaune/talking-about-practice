"""Exercise 2: This program counts the distribution of the hour of the day for each of the messages. You can pull the hour from the “From” line by finding the time string and then splitting that string into parts using the colon character. Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.

python timeofday.py
Enter a file name: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
"""

d = {}
#space = ' '
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.strip()
    words = line.split()
    if line.startswith('From '):
        timestamp = words[5]
        hour = timestamp.split(':')[0]
#        apos = line.find('@')
#        zpos = len(words[0] + words[1] + space)
#        domain = line[apos + 1:zpos]
        #print(hour)
        d[hour] = d.get(hour, 0) + 1
#       if domain not in d:
#           d[domain] = 1
#       else:
#           d[domain] += 1
#print(d)

lst = list()
for key, val in list(d.items()):
    lst.append((key, val))
lst.sort()
for key, val in lst:
    print(key, val)
