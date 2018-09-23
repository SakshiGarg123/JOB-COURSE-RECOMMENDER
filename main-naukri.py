from urllib2 import Request, urlopen
from bs4 import BeautifulSoup
no_of_pages=18000
start=1
end=100
import logging

logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

url="https://www.naukri.com/jobs-in-delhi"
final_ans=[]
for i in range(start,end,1):
    index=str(i);
    url=url+"-"+index
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    web_byte = urlopen(req).read()
    webpage = web_byte.decode('utf-8')
    soup = BeautifulSoup(webpage, features = "html.parser")
    list_links = soup.find_all("a")
    document = []
    for link in list_links:
        intermediate = []
        list_per_job = []
        if (link.get("count") != None):
            #print(link.get("count"))
            job_per_page_url = str(link.get("href"))
            req = Request(job_per_page_url, headers={'User-Agent': 'Mozilla/5.0'})
            web_byte = urlopen(req).read()
            webpage = web_byte.decode('utf-8')
            soup = BeautifulSoup(webpage,features = "html.parser")
            keywords = soup.find_all("a", {"class": "tag"})
            if (keywords != []):
                for keyword in keywords:
                    for span in keyword.find_all('span', recursive=False):
                        # print(span.text)
                        intermediate.append(span.text)
            div_object = soup.find("div", {"class": "ksTags"})
            if (div_object != None):
                keywords2 = div_object.find_all("a")
                if (keywords2 != []):
                    for keyword in keywords2:
                        for span in keyword.find_all('font', recursive=False):
                            # print(span.text)
                            intermediate.append(span.text)

            final_ans.append(intermediate)
            logger.info(intermediate)

# logger.info("Final_ans")
# logger.info(final_ans)