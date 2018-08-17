from urllib.request import Request, urlopen
url="https://www.naukri.com/web-developer-jobs"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

web_byte = urlopen(req).read()

webpage = web_byte.decode('utf-8')
from bs4 import BeautifulSoup
#import BeautifulSoup
soup = BeautifulSoup(webpage)
print(soup.find_all("a"))
list_links=soup.find_all("a")
for link in list_links:
    if(link.get("count")!=None):
        print(link.get("count"))
        print(link.get("href"))
print(len(list_links))