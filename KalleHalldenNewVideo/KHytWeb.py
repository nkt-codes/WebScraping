import requests
from bs4 import BeautifulSoup
import re
import webbrowser

creator = input("Enter the YouTube Creators Videos link: ")

ytUserLink = "https://www.youtube.com/c/"+creator+"/videos"

test = requests.get(ytUserLink)
if test.status_code ==200:
    print("Website exists")
elif test.status_code == 404:
    print("No website found")
soup = BeautifulSoup(test.content, 'html5lib')
scrapped_web = soup.prettify()
r = re.findall(r'\"title\":.*?,\"webPageType\":',soup.prettify())

ifLatest = re.findall(r'\"publishedTimeText\":{\"simpleText\":\".*?ago\"',r[1])

def openNewVideoBrowser ():
    'This function opens the new video in chrome browser'
    #listToStr = ''.join(map(str, ifLatest))
    link = re.findall(r'\"/watch.*?\"',r[1])
    newVideoLink = link[0].replace('"','')
    newestVideoLink = 'https://www.youtube.com'+newVideoLink

    webbrowser.get("google-chrome").open(newestVideoLink)

while True:
    if re.search(r'days',ifLatest[0]):
        print("No videos uploaded today")
        break

    elif re.search(r'hours',ifLatest[0]):
        hourTime = re.findall(r'\d?\d',ifLatest[0])
        print("Video was uploaded" + hourTime[0]+" Hours ago.")
        openNewVideoBrowser()
        break

    elif re.search(r'minutes',ifLatest[0]):
        minuteTime = re.findall(r'\d?\d',ifLatest[0])
        print("Video was uploaded" + minuteTime[0]+" Minutes ago")
        openNewVideoBrowser()
        break
        
