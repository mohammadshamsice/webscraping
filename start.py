from bs4 import BeautifulSoup as bs
import requests
page = requests.get("https://jobinja.ir/jobs?filters%5Bkeywords%5D%5B%5D=data+scientist&filters%5Blocations%5D%5B%5D=%D8%AA%D9%87%D8%B1%D8%A7%D9%86&filters%5Bjob_categories%5D%5B%5D=&b=")
print(page)
soup = bs(page.text, 'html.parser')
result = soup.find_all("li", class_="c-jobListView__metaItem")
# result = soup.find_all("span", class_="")
print(result)
for item in result:
    print(item.text)