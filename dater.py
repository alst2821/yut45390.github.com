# find the dates of links

from BeautifulSoup import BeautifulSoup
import os
import time
from duplicates import getFiles

def dateKey(x):
    if x.has_key('add_date'):
        return x['add_date']
    else:
        return None

def getYM(atag):
    if atag.has_key('add_date'):
        tm = time.gmtime(float(atag['add_date']))
        return (tm.tm_year, tm.tm_mon)
    else:
        return (None, None)


def createDoc(atags):
    head = """
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>
 Bookmarks
</title>
<h1>
 Bookmarks Menu Organized by Date
</h1>
<dl>
 <p>
 </p>
"""    
    tail = """
</dl>
<p>
</p>
"""
    yearH = """
 <dt>
  <h3>
   %(Year)s %(Month)s
  </h3>
  <dl>
   <p>
   </p>
"""
    yearT = """
  </dl>
"""
    strOut = head
    firstYM = True   # write because it's the first time
    for a in atags:
        if firstYM:
            (year, month) = getYM(a)
            writeYM = True
            firstYM = False
        else:
            (nyear, nmonth) = getYM(a)
            if (nyear, nmonth) == (year, month):
                writeYM = False
                strOut = strOut + yearT
            else:
                writeYM = True
                (year, month) = (nyear, nmonth)
        if writeYM:
            strOut = strOut + yearH % { 'Year' : year, 'Month' : month }
        strOut = strOut + '<dt>'+str(a)+'</dt>'
    strOut = strOut + yearT
    strOut = strOut + tail
    return strOut

def removeDups(tags):
    links = {}
    for t in tags:


def main():
    allTags = []
    for filename in getFiles():
        f = open (filename,"r")
        soup = BeautifulSoup(f.read())
        f.close()
    
        atags = soup.findAll('a')
        allTags.extend(atags)
    
    datedata = sorted(allTags, key=dateKey)
    removeDups(datedata)
    strOut = createDoc(datedata)
    f = open("by-date.html","w")
    f.write(strOut)
    f.close()

if __name__ == "__main__":
    main()

