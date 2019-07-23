# remove duplicates in bookmark files
# uses the alphabetical ordering of file names to choose duplicates to remove
import bs4
import os
import sys

def getFiles():
    flist = filter(lambda x: x.endswith(".html"), os.listdir("."))
    statlist = list(map(lambda x: (x, os.stat(x) ) , flist))
    statlist.sort(key=lambda x: x[1].st_mtime)
    return map(lambda x: x[0], statlist)

def removeDups(soup, dups):
    for duplicate in dups:
        t = soup.findAll(True)
        count = len(t)
        atags = soup.findAll('a',href=duplicate,limit=1)
        if len(atags) < 1:
            print("Mysterious dissapearance of link to %s" % duplicate)
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
        print("%s count = %d new count %d" %  (duplicate, count, ncount))

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
    soup = bs4.BeautifulSoup(f.read())
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
        print("*** %s *** " % filename)
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
    print("duplicates: %d" % duplicateCount)
    print("total links: %d" % len(links))

if __name__ == "__main__":
    main()

