import json
import urllib.request as urllib2
from bs4 import BeautifulSoup

try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
  
query = "site:ufcstats.com jon jones"

for j in search(query, tld="co.in", num=10, stop=1, pause=2): 
    url = j

page = urllib2.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')



ul = soup.find_all('ul') #this might not be a list, probably not. But has a length of four

#prevLi = ul[0].li # or: liOne = ul[0].find_next('li'). Height
#data = str(prevLi.contents[2]).strip()
#print(data)

i = 0
allStatsNums = [] 

for j in ul: #Weight, Reach, Stance, DOB. Not iterating through all indexes in ul, just ul[0]. J is individual ul groups. This actually goes to one extra ul group but fails all if statements so nothing extra gets added
    stats = []
    prevLi = ul[i].li #I think this is the first li group in each ul[] index
    data = str(prevLi.contents[2]).strip()
    if data: #only add to list is string is not empty. This avoids adding empty string that was occuring before
        stats.append(data)
    for m in j: #This should be the right structure but need to add stuff in between nested loops so it works. M allows us to acccess individual li groups
        nextLi = prevLi.find_next_sibling('li')
        if nextLi is None:
            break
        data = str(nextLi.contents[2]).strip()
        if not data: #prevents empty string from being added to the list
            continue
        stats.append(data)
        prevLi = nextLi
    i = i+1
    if stats: #prevents a empty list from being added to the list of allStatsNums
        allStatsNums.append(stats)

print(allStatsNums) #Holy shit everything is working!

i = 0
allStatsNames = []

for j in ul: 
    names = []
    prevLi = ul[i].li 
    name = None
    if prevLi.i and prevLi.i.string:
        name = str(prevLi.i.string).strip()
        names.append(name)
    for m in j: 
        nextLi = prevLi.find_next_sibling('li')
        if nextLi is None or nextLi.i is None: #nextLi.i is accounting for the last li.i group that has unwanted information like "Fighters"
            break
        name = str(nextLi.i.string).strip()
        if not name: 
            continue
        names.append(name)
        prevLi = nextLi
    i = i+1
    if names:
        allStatsNames.append(names)

print(allStatsNames)  

#inside each ul index we want all of the li's
#then we move onto the next ul index


