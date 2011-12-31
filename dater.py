# find the dates of links, generate output
# by-date.html
from BeautifulSoup import BeautifulSoup
import os
import time
from duplicates import getFiles

def dateKey(x):
    if x[0].has_key('add_date'):
        return x[0]['add_date']
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

def createContents(linksByDate):
    contentsHead="""<h2><a name="contents">Contents (Total links: %d)</a></h2>
<ul>"""
    contentsEntry="""<li><a href="#%(AnchorName)s">%(Name)s</a> %(Elements)s</li>"""
    contentsTail="</ul>"
    total = 0
    strOut = ""
    for ym in sorted(linksByDate.keys()):
        no_elements = len(linksByDate[ym].keys())
        total = total + no_elements
        if no_elements > 1:
            elements = "%d elements" % no_elements
        else:
            elements = "1 element"
        YM = {'Year': ym[0], 'Month': ym[1]}
        strOut = strOut + contentsEntry % { 
            'AnchorName': "%(Year)s_%(Month)s" % YM,
            'Name' : "%(Year)s %(Month)s" % YM,
            'Elements' : elements} 
    strOut = (contentsHead % total) + strOut + contentsTail
    return strOut

def createDoc(allPairs, hrefDictionary):
    documentHead = """<meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><title>Bookmarks</title><h1>Bookmarks Menu Organized by Date </h1>"""
    head = """<dl><p></p>"""
    tail = """</dl><p></p>"""
    yearH = """<dt><h3><a name="%(Year)s_%(Month)s">%(Year)s %(Month)s</a></h3><dl><p></p>"""
    yearT = """</dl>"""
    pairs_by_date = sorted(allPairs, key=dateKey)
    linksByDate= {}
    processed = {}
    for (a,dd) in pairs_by_date:
        ym = getYM(a)
        href = a['href']
        if not href in processed.keys():
            if ym in linksByDate.keys():
                linksByDate[ym][href] = hrefDictionary[href]
            else:
                linksByDate[ym] = {href: hrefDictionary[href]}
            processed[href] = 1
            if ym == getFirstDate(hrefDictionary[href]):
                ff = getFirstDate(hrefDictionary[href])
                print "error: ym is %s/%s - first reg is %s/%s" % (
                      ym[0], ym[1], ff[0], ff[1])
    strOut = documentHead
    strOut = strOut + createContents(linksByDate)
    for ym in sorted(linksByDate.keys()):
        (year, month) = ym
        strOut = strOut + yearH % { 'Year' : year, 'Month' : month }
        for hrefGroupKey in linksByDate[ym].keys():
            hrefGroup = linksByDate[ym][hrefGroupKey]
            (aa, dd) = hrefGroup[0]
            strOut = strOut + '<dt>'+str(aa)
            n = len(hrefGroup)
            otherDates = []
            if n > 1:
                for i in range(1,n):
                    (aa,dd1) = hrefGroup[i]
                    if dd == None:
                        dd = dd1
                    otherYM = getYM(aa)
                    if ym == otherYM:
                        continue
                    else:
                        otherDates.append(otherYM)
                nOtherDates = len(otherDates)
                for dindex in range(nOtherDates):
                    otherDatesOut = "%s/%s " % otherDates[dindex]
                    if nOtherDates > 2:
                        if dindex == nOtherDates-2:
                            otherDatesOut = otherDatesOut + "and "
                        else:
                            otherDatesOut = otherDatesOut + ", "
                if nOtherDates > 1:
                    strOut = strOut + otherDatesOut
            strOut = strOut + '</dt>'
            if dd != None:
                strOut = strOut + str(dd)
        strOut = strOut + yearT
    strOut = strOut + tail
    return strOut

def gatherTags(exceptions=["by-date.html"]):
    allPairs = [] # tuples of a link and associated dd field
    fileList = filter(lambda x: x not in exceptions, getFiles())
    hrefDictionary = {}
    for filename in fileList:
        f = open(filename,"r")
        soup = BeautifulSoup(f.read())
        f.close()
        atags = soup.findAll('a')
        hasDD = False
        for a in atags:
            dt = a.findParent()
            assert dt.name == "dt"
            ddList=dt.findAllNext(['dt','dd'],limit=1)
            if ddList and ddList[0].name == "dd":
                dd = ddList[0]
            else:
                dd = None
            pair = (a, dd)
            l = a['href']
            if l in hrefDictionary.keys():
                hrefDictionary[l].append(pair)
                if hasDD:
                    print "Warning: duplicate description for link."
                    print "URL: %s" % l
            else:
                hrefDictionary[l] = [pair]
                hasDD = pair[1] != None
            allPairs.append(pair)
    return (allPairs, hrefDictionary)

def main():
    (allPairs,hrefDictionary) = gatherTags()
    strOut = createDoc(allPairs,hrefDictionary)
    soup = BeautifulSoup(strOut)
    fg = open("by-date.html","w")
    fg.write(soup.prettify())
    fg.close()

if __name__ == "__main__":
    main()

