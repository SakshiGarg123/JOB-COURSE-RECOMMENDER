from urllib2 import Request, urlopen
from bs4 import BeautifulSoup
no_of_pages=18000
start=22
end=100
import logging

print("Creating skills log file...")

logging.basicConfig(filename="example3.log",
                    format='%(asctime)s %(message)s',level=logging.INFO)
print("Scraping started...")
url="https://www.naukri.com/jobs-in-delhi"
final_ans=[]
for i in range(start,end,1):
    try:
        print("Page {}".format(i))
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
            if (link.get("id") == "jdUrl"):
                job_per_page_url = str(link.get("href"))
                job_per_page_name = str(link.text)
                intermediate.append(job_per_page_url)
                intermediate.append(job_per_page_name)
                req = Request(job_per_page_url, headers={'User-Agent': 'Mozilla/5.0'})
                web_byte = urlopen(req).read()
                webpage = web_byte.decode('utf-8')
                soup = BeautifulSoup(webpage,features = "html.parser")
                keywords = soup.find_all("a", {"class": "tag"})
                if (keywords != []):
                    for keyword in keywords:
                        for span in keyword.find_all('span', recursive=False):
                            intermediate.append(span.text)
                div_object = soup.find("div", {"class": "ksTags"})
                if (div_object != None):
                    keywords2 = div_object.find_all("a")
                    if (keywords2 != []):
                        for keyword in keywords2:
                            for span in keyword.find_all('font', recursive=False):
                                intermediate.append(span.text)

                final_ans.append(intermediate)
                logging.info(intermediate)

    except:
        print "skipped"