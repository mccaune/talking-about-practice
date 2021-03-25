"""
Exercise 2: Write a program to prompt for a file name, and then read through the file and look for lines of the form:
X-DSPAM-Confidence: 0.8475
When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the floating-point number on the line. Count these lines and then compute the total of the spam confidence values from these lines. When you reach the end of the file, print out the average spam confidence.

Enter the file name: mbox.txt
Average spam confidence: 0.894128046745

Enter the file name: mbox-short.txt
Average spam confidence: 0.750718518519

"""

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    if fname == 'pokemon':
        print('gotta catch them all')
    else:
        print('File cannot be opened:', fname)
    exit()

count = 0
total = 0
for line in fhand:
    line = line.strip()
    if line.find('X-DSPAM-Confidence:') == -1: continue
    #print(line)
    count = count +1
    apos = line.find(':')
    zpos = len(line)
    number = line[apos + 1:zpos]
    float_number = float(number)
    #print(float_number)
    #print(type(float_number))
    total = total + float_number
print('count: ', count)
print('total: ', total)
print('average: ', total / count)
