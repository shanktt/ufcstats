import json
import urllib.request as urllib2
from bs4 import BeautifulSoup

try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
  
#query = "site:ufcstats.com jon jones"
query = "site:ufcstats.com conor mcgregor"

for j in search(query, tld="co.in", num=10, stop=1, pause=2): 
    url = j

page = urllib2.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

allStatsNamesAndNums = []

name = str(soup.h2.span.string).strip()
allStatsNamesAndNums.append(["Name", name])
nick = str(soup.p.string).strip()
allStatsNamesAndNums.append(["Nick", nick])

ul = soup.find_all('ul')

i = 0
for j in ul: 
    prevLi = ul[i].li 
    name = None #rename variable
    if prevLi.i and prevLi.i.string:
        name = str(prevLi.i.string).strip()

    data = str(prevLi.contents[2]).strip()
    if name and data: 
        allStatsNamesAndNums.append([name,data])

    for m in j:
        nextLi = prevLi.find_next_sibling('li')
        if nextLi is None or nextLi.i is None: #nextLi.i is accounting for the last li.i group that has unwanted information like "Fighters". Also if there is name for a stat then there must be a number for it so just need to ensure the name exists
            break
        name = str(nextLi.i.string).strip()
        data = str(nextLi.contents[2]).strip()
        #print(name + "," + data)
        if not name and data: 
            continue

        allStatsNamesAndNums.append([name,data]) 

        prevLi = nextLi
    i = i+1

#print(allStatsNamesAndNums)

statDictionary = {stat[0]: stat[1] for stat in allStatsNamesAndNums}
#print(statDictionary)

jsonStats = json.dumps(statDictionary)
print(jsonStats)
    


