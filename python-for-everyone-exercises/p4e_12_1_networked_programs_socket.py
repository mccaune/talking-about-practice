'''
Exercise 1: Change the socket program socket1.py to prompt the user for the URL so it can read any web page. You can use split('/') to break the URL into its component parts so you can extract the host name for the socket connect call. Add error checking using try and except to handle the condition where the user enters an improperly formatted or non-existent URL.
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
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(),end='')
    break
mysock.close()
