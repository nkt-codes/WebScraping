import requests
from bs4 import BeautifulSoup
import re
import webbrowser

test = requests.get("https://www.youtube.com/c/chrissmoove/videos")
if test.status_code ==200:
    print("Website exists")
elif test.status_code == 404:
    print("No website found")
soup = BeautifulSoup(test.content, 'html5lib')
scrapped_web = soup.prettify()
r = re.findall(r'\"title\":.*?,\"webPageType\":',soup.prettify())

ifLatest = re.findall(r'\"publishedTimeText\":{\"simpleText\":\".*?ago\"',r[1])

while True:
    if re.search(r'days',ifLatest[0]):
        print("No videos uploaded today")
        break

    elif re.search(r'hours',ifLatest[0]):
        hourTime = re.findall(r'\d?\d',ifLatest[0])
        print(hourTime[0]+" Hours")
        break

    elif re.search(r'minutes',ifLatest[0]):
        minuteTime = re.findall(r'\d?\d',ifLatest[0])
        print(minuteTime[0]+" Minutes")
        break


# using list comprehension
listToStr = ''.join(map(str, ifLatest))
#print(listToStr) 

#link = re.findall(r'\"/watch.*?\"',r[1])
#newVideoLink = link[0].replace('"','')
#newestVideoLink = 'https://www.youtube.com'+newVideoLink

#webbrowser.get("google-chrome").open(newestVideoLink)


