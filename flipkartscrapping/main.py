import requests
from bs4 import BeautifulSoup
import csv

# Get Flipkart source code
url = "https://www.flipkart.com/search?q=laptop&page=1"
header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 Edg/89.0.774.77'}
MyRequests = requests.get(url, header)
print(MyRequests)

# Send requested code to soup
MySoup = BeautifulSoup(MyRequests.content, 'html.parser')

# Get Laptop description
LaptopLists = MySoup.find_all('div', class_='_4rR01T')
LaptopList = []
for each in LaptopLists:
    # print(each.text)
    LaptopList.append(each.text)

# Get Laptop Price
PriceLists = MySoup.find_all('div', class_='_30jeq3 _1_WHN1')
PriceList = []
for each in PriceLists:
    # print(each.text)
    PriceList.append(each.text)

with open('output.csv', 'w+', newline='', encoding='utf_8') as MyFile:
    a = csv.writer(MyFile, delimiter=',')
    a.writerow(["Product", "Price"])
    # print([LaptopList, PriceList])
    for index in range(len(PriceList)):
        a.writerow([LaptopList[index], PriceList[index][1:]])

