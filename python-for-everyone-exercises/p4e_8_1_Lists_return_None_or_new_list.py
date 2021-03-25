"""
Exercise 1: Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None. Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.
"""

def chop(t):
    del t[0]
    del t[len(t) - 1]

def middle(t):
    return t[1:len(t)-1]

#modificē esošo listu. returns None
letters = ['a', 'b', 'c', 'd', 'e']
mod1 = chop(letters)
print(mod1)
print(letters, '\n')

#izveido jaunu listu, esošo saglabā nemainītu
letters2 = ['a', 'b', 'c', 'd', 'e']
mod2 = middle(letters2)
print(mod2)
print(letters2)
