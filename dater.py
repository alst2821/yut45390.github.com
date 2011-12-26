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

def getFirstDate(l):
    s = sorted(l, key=dateKey)
    return dateKey(s[0])

def createDoc(allTags):
    head = """<meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><title>Bookmarks</title><h1>Bookmarks Menu Organized by Date </h1><dl><p></p>"""    
    tail = """</dl><p></p>"""
    yearH = """<dt><h3>%(Year)s %(Month)s</h3><dl><p></p>"""
    yearT = """</dl>"""
    datedata = sorted(allTags, key=dateKey)
    links = getHrefDictionary(datedata)
    linksByDate= {}
    processed = {}
    for a in datedata:
        ym = getYM(a)
        href = a['href']
        if not href in processed.keys():
            if ym in linksByDate.keys():
                linksByDate[ym][href] = links[href]
            else:
                linksByDate[ym] = {href: links[href]}
            processed[href] = 1
            if ym == getFirstDate(links[href]):
                ff = getFirstDate(links[href])
                print "error: ym is %s/%s - first reg is %s/%s" % (
                      ym[0], ym[1], ff[0], ff[1])
    strOut = head
    for ym in sorted(linksByDate.keys()):
        (year, month) = ym
        strOut = strOut + yearH % { 'Year' : year, 'Month' : month }
        for hrefGroupKey in linksByDate[ym].keys():
            hrefGroup = linksByDate[ym][hrefGroupKey]
            strOut = strOut + '<dt>'+str(hrefGroup[0])
            n = len(hrefGroup)
            if n > 1:
                otherDatesOut = " Also registered on "
                for i in range(1,n):
                    aa = hrefGroup[i]
                    otherDatesOut = otherDatesOut + "%s/%s " % getYM(aa)
                    if n > 2:
                        if i == n-2:
                            otherDatesOut = otherDatesOut + "and "
                        else:
                            otherDatesOut = otherDatesOut + ", "
                strOut = strOut + otherDatesOut
            strOut = strOut + '</dt>'
        strOut = strOut + yearT
    strOut = strOut + tail
    return strOut

def getHrefDictionary(tags):
    # links : dictionary using hrefs as keys
    #         members is a list of 'a' tags
    links = {}
    for t in tags:
        l=t['href']
        if l in links.keys():
            links[l].append(t)
        else:
            links[l] = [t]
    # upon printing a tag, the links dictionary is searched to 
    # find more dates. A marker 1 (type integer) marks that a
    # link href has been processed
    return links

def main():
    allTags = []
    fileList = filter( lambda x: x != "by-date.html", getFiles())
    for filename in fileList:
        f = open (filename,"r")
        soup = BeautifulSoup(f.read())
        f.close()
    
        atags = soup.findAll('a')
        allTags.extend(atags)
    
    strOut = createDoc(allTags)
    f = open("by-date.html","w")
    f.write(strOut)
    f.close()

if __name__ == "__main__":
    main()

