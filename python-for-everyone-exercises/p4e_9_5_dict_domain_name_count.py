"""
Exercise 5: This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from (i.e., the whole email address). At the end of the program, print out the contents of your dictionary.

python schoolcount.py
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}

"""

d = {}
space = ' '
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.strip()
    words = line.split()
    if line.startswith('From '):
        email = words[1]
        domain = email.split('@')[1]
#        apos = line.find('@')
#        zpos = len(words[0] + words[1] + space)
#        domain = line[apos + 1:zpos]
        print(domain)
        d[domain] = d.get(domain, 0) + 1
#       if domain not in d:
#           d[domain] = 1
#       else:
#           d[domain] += 1
print(d)
