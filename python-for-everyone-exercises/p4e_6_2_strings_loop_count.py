"""
word = 'banana'
count = 0
for letter in word:
if letter == 'a':
count = count + 1
print(count)

This program demonstrates another pattern of computation called a counter. The variable count is initialized to 0 and then incremented each time an “a” is found. When the loop exits, count contains the result: the total number of a’s. Exercise 3: Encapsulate this code in a function named count, and gen- eralize it so that it accepts the string and the letter as arguments.
"""


def count (word, letter):
    count = 0
    for check in word:
        if check == letter:
                count = count + 1
    print('Letter - ',  letter, ' is mentioned ', count, ' times in word - ', word)


word = input('Please enter a word: ')
letter = input('Please enter a letter: ')

count(word, letter)
