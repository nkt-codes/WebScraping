import requests
from bs4 import BeautifulSoup
import re
#import os

test = requests.get("https://www.youtube.com/c/KalleHallden/videos")
if test.status_code ==200:
    print("Website exists")
elif test.status_code == 404:
    print("No website found")

soup = BeautifulSoup(test.content, 'html5lib')
scrapped_web = soup.prettify()

'''
with open("KalleHalldenNewVideo/webdetails.txt","w") as wd:
    wd.write(scrapped_web)
    wd.close()
#file = open("webdetails.txt","r")
#k = file.read()
'''

r = re.findall(r'\"title\":.*?,\"webPageType\":',soup.prettify())

print(r[1])



