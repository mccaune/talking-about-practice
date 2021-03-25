"""Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency. Your program should convert all the input to lower case and only count the letters a-z. Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. Find text samples from several different languages and see how letter frequency varies between languages. Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.
"""

import string
d = {}
#alphabet = ['a', 'b','c', 'd', 'e', 'f', 'g', 'h', 'i',
#'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u',
#'v', 'z', 'x', 'y', 'q', 'w']
#space = ' '
fhand = open('mbox.txt')
for line in fhand:
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()

    words = line.split()
    for word in words:
        for letter in word:
#            if letter not in alphabet: continue
#            else:
#            print(letter)
#    if line.startswith('From '):
#        timestamp = words[5]
#        hour = timestamp.split(':')[0]
#        apos = line.find('@')
#        zpos = len(words[0] + words[1] + space)
#        domain = line[apos + 1:zpos]
#        print(hour)
                d[letter] = d.get(letter, 0) + 1
#       if domain not in d:
#           d[domain] = 1
#       else:
#           d[domain] += 1
#print(d)
num_list = list()
for key, val in list(d.items()):
    num_list.append(val)
#print(sum(num_list))


lst = list()
for key, val in list(d.items()):
    lst.append((val/sum(num_list)*100, key))
lst.sort(reverse=True)
for key, val in lst:
    print(key, val)
