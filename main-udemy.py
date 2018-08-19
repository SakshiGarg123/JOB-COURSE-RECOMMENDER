import pandas as pd
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

data = pd.read_csv("Udemy Courses Data - IT & Software .csv")
data.columns = data.iloc[1]
data.drop(data.index[[0,1]],inplace=True)
data.reset_index(drop=True,inplace=True)
list_url=data["Product URL"]
print(data.dtypes)
for link in list_url:
    url=str(link)
    print("new",url)
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    web_byte = urlopen(req).read()
    webpage = web_byte.decode('utf-8')
    soup = BeautifulSoup(webpage)
    list_links = soup.find_all('div', {"class": "requirements__content"})
    for link in list_links:
            print(link)
# print(list(data))