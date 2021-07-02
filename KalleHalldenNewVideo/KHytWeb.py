import requests
from bs4 import BeautifulSoup
import re
import webbrowser

def creatorSelect():
    with open("/home/nkt/Scripting/Projects/WebScraping/KalleHalldenNewVideo/creators.txt") as f:
        creator = f.read().splitlines()
        print("List of creator who you can check if uploaded today: \n------------------------\n")
        for j in range(len(creator)):
            print(str(j+1) + ". " + creator[j])
        selectedCreator = input("\nEnter Number or q to quit: ")
        if selectedCreator == "q":
            print("You can check later... :)")
            exit()
        else:
            return creator[int(selectedCreator)-1]
            
#watchCreator = input("Enter the YouTube Creators Videos link: ")
ytUserLink = "https://www.youtube.com/c/"+creatorSelect()+"/videos"

print(ytUserLink)

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

    webbrowser.get("google-chrome").open(newestVideoLink,new=2)

while True:
    if re.search(r'days',ifLatest[0]):
        print("No videos uploaded today")
        break

    elif re.search(r'hours',ifLatest[0]):
        hourTime = re.findall(r'\d?\d',ifLatest[0])
        print("Video was uploaded " + hourTime[0]+" Hours ago.")
        openNewVideoBrowser()
        break

    elif re.search(r'minutes',ifLatest[0]):
        minuteTime = re.findall(r'\d?\d',ifLatest[0])
        print("Video was uploaded " + minuteTime[0]+" Minutes ago")
        openNewVideoBrowser()
        break
        
