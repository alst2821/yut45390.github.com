from BeautifulSoup import BeautifulSoup
import os
import sys

def getFiles():
    list = filter(lambda x: x.endswith(".html"), os.listdir("."))
    list.sort()
    return list

def removeDups(soup, dups):
    for duplicate in dups:
        t = soup.findAll(True)
        count = len(t)
        atags = soup.findAll('a',href=duplicate,limit=1)
        if len(atags) < 1:
            print "Misterious dissapearance of link to %s" % duplicate
            continue
        assert len(atags) == 1
        dt = atags[0].findParent()
        assert dt.name == "dt"
        nn=dt.findAllNext(['dt','dd'],limit=1)
        if nn and nn[0].name == "dd":
            nn[0].extract()
        dt.extract()
        nt = soup.findAll(True)
        ncount = len(nt)
        print "%s count = %d new count %d" %  (duplicate, count, ncount)
        #if nn[0].name == "dd":
        #    assert count == ncount + 3
        #else:
        #    assert count == ncount + 2

def saveNoDups(soup, filename, overwrite):
    if overwrite:
        output = filename
    else:
        output = filename + ".nodups"
    f = open(output , "w")
    f.write(soup.prettify())
    f.close()

def getHrefs(filename):
    f = open(filename, "r")
    soup = BeautifulSoup(f.read())
    f.close()
    atags = soup.findAll('a', attrs={'href':True})
    hrefs = map( lambda x: x['href'], atags)
    return ( hrefs, soup)

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "-o":
        overwrite = True
    else:
        overwrite = False
    links = {}
    duplicateCount = 0
    for filename in getFiles():
        print "*** %s *** " % filename
        (hrefs , soup) =  getHrefs(filename)
        dups = []
        for x in hrefs:
            if x in links.keys():
                dups.append(x)
                duplicateCount = duplicateCount + 1
            else:
                links[x] = 1
        if dups:
            removeDups(soup, dups)
            saveNoDups(soup, filename, overwrite)
    print "duplicates: %d" % duplicateCount
    print "total links: %d" % len(links)

if __name__ == "__main__":
    main()


