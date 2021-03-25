"""
Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt Write a program that reads the words in words.txt and stores them as keys in a dictionary. It doesn’t matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.
"""

#d = dict()
d = {}
fhand = open('words.txt')
for line in fhand:
    words = line.split()
    for word in words:
        #print(word)
        d[word] = 1 #katram vardnicas key pieskir vertibu 1
print(d) #izprinte visu tekstu ka vardnicu, kur katram vardam value ir 1
print('and' in d) #parbauda vai 'and' atrodas vardnica
