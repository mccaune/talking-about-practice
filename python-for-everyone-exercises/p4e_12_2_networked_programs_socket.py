'''
Exercise 2: Change your socket program so that it counts the number of characters it has received and stops displaying any text after it has shown 3000 characters. The program should retrieve the entire docu- ment and count the total number of characters and display the count of the number of characters at the end of the document.
'''

import socket

while True:
    webpage = input('Enter a web page: ')
    try:
        webpage_lst = webpage.split('/')
        host = webpage_lst[2]
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect((host, 80))
        cmd = 'GET '+webpage+' HTTP/1.0\r\n\r\n'
        mysock.send(cmd.encode())
    except:
        print('Please enter a valid web address')
        continue
    count = 0
    full_data = ''
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        count = count + len(data)
        data_decoded = data.decode()
        full_data = data_decoded + full_data
    break
print(len(data), count)
print(data_decoded)
mysock.close()
