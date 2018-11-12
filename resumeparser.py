import csv
import six
import re
import spacy
import sys
import importlib
reload(sys)
# importlib.reload(sys)
import pandas as pd
sys.setdefaultencoding('utf8')
# import io
from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os
import sys, getopt
import numpy as np
from bs4 import BeautifulSoup
import urllib2
from urllib2 import urlopen
# import urllib.request
# from urllib.request import urlopen

#Function converting pdf to string
def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    # output=io.StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = open(fname, 'rb')#changed open
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text

#Function to extract Phone Numbers from string using regular expressions
def extract_phone_numbers(string):
    r = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
    phone_numbers = r.findall(string)
    return [re.sub(r'\D', '', number) for number in phone_numbers]
#Function to extract Email address from a string using regular expressions
def extract_email_addresses(string):
    r = re.compile(r'[\w\.-]+@[\w\.-]+')
    return r.findall(string)

def init():
    #Converting pdf to string
    resume_string = convert("resume.pdf")
    resume_string1 = resume_string
    #Removing commas in the resume for an effecient check
    resume_string = resume_string.replace(',',' ')
    #Converting all the charachters in lower case
    resume_string = resume_string.lower()
    return resume_string

#Information Extraction Function
def extract_information(string):
    string.replace (" ", "+")
    query = string
    soup = BeautifulSoup(urlopen("https://en.wikipedia.org/wiki/" + query), "html.parser")
    #creates soup and opens URL for Google. Begins search with site:wikipedia.com so only wikipedia
    #links show up. Uses html parser.
    for item in soup.find_all('div', attrs={'id' : "mw-content-text"}):
        print(item.find('p').get_text())
        print('\n')
def parse_resume():
    resume_string=init()
    with open('techatt.csv', 'rt') as f:
        reader = csv.reader(f)
        tech_listatt = list(reader)
    with open('techskill.csv', 'rt') as f:
        reader = csv.reader(f)
        tech_list = list(reader)
    with open('nontechnicalskills.csv', 'rt') as f:
        reader = csv.reader(f)
        nontech_list = list(reader)
    #Sets are used as it has a a constant time for lookup hence the overall the time for the total code will not exceed O(n)
    s = set(tech_list[0])
    skillindex = []
    skills = []
    skillsatt = []
    # print('\n')
    # print('\n')
    # print('Phone Number is')
    # numbers = extract_phone_numbers(resume_string)
    # number_list = []
    # for i in range(len(numbers)):
    #     if(len(numbers[i])>9):
    #         number_list.append(numbers[i])
    # print(number_list)
    # print('\n')
    # print('Email id is')
    # print(extract_email_addresses(resume_string))
    for word in resume_string.split(" "):
        if word in s:
            skills.append(word)
    print('\n')
    print("Following are his/her Technical Skills")
    print('\n')
    np_a1 = np.array(tech_list)
    for i in range(len(skills)):
        item_index = np.where(np_a1==skills[i])
        skillindex.append(item_index[1][0])

    nlen = len(skillindex)
    for i in range(nlen):
        print(skills[i])
        print(tech_listatt[0][skillindex[i]])
        print('\n')

    # #Sets are used as it has a a constant time for lookup hence the overall the time for the total code will not exceed O(n)
    # s1 = set(nontech_list[0])
    # nontechskills = []
    # for word in resume_string.split(" "):
    #     if word in s1:
    #         nontechskills.append(word)
    # print('\n')

    # print("Following are his/her Non Technical Skills")
    # print('\n')
    # for i in range(len(nontechskills)):
    #     print(nontechskills[i])
    # print('\n \n')
    return skills
