import urllib.request

response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.01)
print(response.read())
