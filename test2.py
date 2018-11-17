from urllib.parse import urlparse
a = 'http://www.cwi.nl:80/%7Eguido/Python.html'
b = '/data/Python.html'
c = 532
d = u'dkakasdkjdjakdjadjfalskdjfalk'

def uri_validator(x):
    try:
        result = urlparse(x)
        return all([result.scheme, result.netloc, result.path])
    except:
        return False

print(uri_validator(a))
print(uri_validator(b))
print(uri_validator(c))
print(uri_validator(d))

print(uri_validator("http://www.runoob.com/python3/python3-comment.html"))