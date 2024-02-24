import requests 
URL = "https://www.ravelry.com/" 
r = requests.get(URL) 
print(r.content) 