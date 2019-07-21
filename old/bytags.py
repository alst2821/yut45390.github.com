
from BeautifulSoup import BeautifulSoup
import dater

f = open("extra2.html","r")
soup = BeautifulSoup(f.read())
f.close()

taggedLinks = soup.findAll('a',attrs={'tags':True})

tagSets = {}
for link in taggedLinks:
    for tag in link['tags'].split(","):
        if tag in tagSets.keys():
            tagSets[tag].append(link)
        else:
            tagSets[tag] = [ link ]

if __name__ == "__main__":
    main()

