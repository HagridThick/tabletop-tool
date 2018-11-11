import json
import socket

class Vividict(dict):
	def __missing__(self, key):
		value = self[key] = type(self)()
		return value
	def walk(self):
		for key, value in self.items():
			if isinstance(value, Vividict):
				for tup in value.walk():
					yield (key,) + tup
			else:
				yield key, value

def is_url(str):
    li = str.split(' ')
    if len(li) >= 4:
        #print(len(li))
        if li[3] != socket.gethostbyname( li[3] ):
            return str


with open('776875059.json',encoding='utf-8') as f:

    data = json.load(f)
    """
    print(type(data))
    print(data['Grid'])
    print(type(data['Grid']))
    print(data['Grid']['Type'])
    print(type(data['Grid']['Type']))
    print(data['Grid']['Color'])
    print(type(data['Grid']['Color']))
    """
    #for i in data:
        #print(i)
    vi = Vividict(data)
    for tup in vi.walk():
        #print(tup)
        #print(type(tup)) 
        s1 = tup[1]
        #print(type(s1))

        if(isinstance(s1,str)):
              #print(type(s1))
              #print(s1)
              url = is_url(s1)
              print(url)
        """
            #li = tup.split(' ')
            #if li[3] != socket.gethostbyname( li[3] ):
               # print(tup)
            url = is_url(s1)
            print(url)
            if(url):
                print(url)
        """