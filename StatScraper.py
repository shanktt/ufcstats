import json
import urllib.request as urllib2
from bs4 import BeautifulSoup

def getWebPage(name):
    try: 
        from googlesearch import search 
    except ImportError:  
        print("No module named 'google' found") 

    query = "site:ufcstats.com " + name

    for j in search(query, tld="co.in", num=10, stop=1, pause=2): 
        url = j

    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    return soup

def getStats(soup):
    stats = []

    name = str(soup.h2.span.string).strip()
    stats.append(["Name", name])
    nick = str(soup.p.string).strip()
    stats.append(["Nick", nick])

    ulList = soup.find_all('ul')

    for ul in ulList: #accessing each individual ul tag in ulList
        for li in ul.find_all('li'): #iterating through each li tag in each ul tag
            if li.i and (str(li.i.string).strip() != ""): #Since and short circuits wont run into error of prevLi.i not existing and trying to get a string from it. 
                statName = str(li.i.string).strip() 
                statNum = str(li.contents[2]).strip() #If there is a statName inside the i tag there is always an associated statNum outside the i tag but in the li tag
                stats.append([statName,statNum])

    statDictionary = {stat[0]: stat[1] for stat in stats} #creating python dictionary from list of data
    jsonStats = json.dumps(statDictionary, indent=4) #create json object from python dictionary
    return jsonStats


soup = getWebPage("Jon Jones")
stats = getStats(soup)
print(stats)