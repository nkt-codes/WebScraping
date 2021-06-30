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
r = re.findall(r'\"title\":.*?,\"webPageType\":',soup.prettify())
link = re.findall(r'\"/watch.*?\"',r[1])
newVideoLink = link[0].replace('"','')
print('https://www.youtube.com'+newVideoLink)





