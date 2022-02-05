from urllib import request
import json

#url = "https://type.fit/api/quotes"
url = "http://joke3.p.rapidapi.com/v1/joke"

r = request.urlopen(url)
print(r.getcode())
data = r.read()
#print(data)
jData = json.loads(data)
print(jData)
