from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import re

driver = webdriver.Chrome('D://chromedriver_win32//chromedriver.exe')

#main edX page of all English courses -- this scraper excludes edX courses in other languages
driver.get('https://www.edx.org/course?language=English')

#open a new blank csv
csv_file = open('courses_whole.csv', 'w')

writer = csv.writer(csv_file)

#write column headers for each of the variables to scrape
writer.writerow(['course_link','price', 'title', 
                 'subject', 'level', 'institution', 'length', 
                 'prerequisites', 'short_description', 'effort'])

num_classes_str = driver.find_element_by_xpath('//h2[@class="js-result-msg hide-phone"]').text

