import requests 
from bs4 import BeautifulSoup 
import csv 

URL = "https://thesustainablelivingguide.com/fast-fashion-brands/" 
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

badBrands = []

table = soup.find('div', attrs = {'id':'primary'})

for name in table.findAll('div', attrs = {'class':'lwptoc_item'}):
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