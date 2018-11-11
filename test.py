import socket

s1 = 'https://docs.python.org/dev/library/urllib.parse.html?highlight=s'
a1 = 15
if(isinstance(a1,str)):
    print(a1)
if(isinstance(s1,str)):
    print(s1)
li = s1.split(' ')
if(len(li) >= 3):
    if li[3] != socket.gethostbyname( li[3] ):
        print(li)