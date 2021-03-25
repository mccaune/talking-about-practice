"""Exercise 1: Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line. Count the num- ber of messages from each person using a dictionary.

After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.

Sample Line:
From stephen.marquard@uct.ac.za Sat Jan
5 09:14:16 2008

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195
"""

d = {}
space = ' '
fhand = open('mbox.txt')
for line in fhand:
    line = line.strip()
    words = line.split()
    if line.startswith('From '):
        email = words[1]
        #domain = email.split('@')[1]
#        apos = line.find('@')
#        zpos = len(words[0] + words[1] + space)
#        domain = line[apos + 1:zpos]
        #print(email)
        d[email] = d.get(email, 0) + 1
#       if domain not in d:
#           d[domain] = 1
#       else:
#           d[domain] += 1
#print(d)

lst = list()
for key, val in list(d.items()):
    lst.append((val, key))
lst.sort(reverse=True)
for key, val in lst[:1]:
    print(key, val)
