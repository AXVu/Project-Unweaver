import requests 
from bs4 import BeautifulSoup 

URL = "https://thesustainablelivingguide.com/fast-fashion-brands/" 
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

badBrands = []

table = soup.find('div', attrs = {'id':'primary'})

for name in table.find_all('div', attrs = {'class':'lwptoc_item'}):
    x = name.a['href']
    x = x.replace('_', ' ')
    x = x.replace('#', '')
    y = x.replace(' ', '')
    if y.isalpha() == False:
        badBrands.append(x)
       
badBrands = badBrands[1:42]

for i in range(len(badBrands)): 
    brand = badBrands[i]

    brand = brand.lstrip(brand[:2])
    brand = brand.lstrip()
    badBrands[i] = brand

print(badBrands)



URL2 = "https://www.panaprium.com/blogs/i/list-of-fast-fashion-brands-to-avoid" 
r2 = requests.get(URL2)

soup2 = BeautifulSoup(r2.content, 'html5lib')

badBrands2 = []

table2 = soup2.find('div', attrs = {'id':'blog-post'})

for name in table2.select('li'):
    badBrands2.append(name.text)


badBrands2 = badBrands2[5:94]
print(len(badBrands2))
print(badBrands2)