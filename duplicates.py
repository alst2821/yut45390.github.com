from BeautifulSoup import BeautifulSoup
import os

def getFiles():
    list = filter(lambda x: x.endswith(".html"), os.listdir("."))
    list.sort()
    return list

def getHrefs(filename):
    f = open(filename, "r")
    soup = BeautifulSoup(f.read())
    f.close()
    atags = soup.findAll('a')
    return map( lambda x: x['href'], atags)

def report(filename, link):
    print link
    #print "Found duplicate link in %s: %s" % (filename, link)

def main():
    links = {}
    duplicateCount = 0
    for filename in getFiles():
        print "*** %s *** " % filename
        hrefs =  getHrefs(filename)
        for x in hrefs:
            if x in links.keys():
                report(filename, x)
                duplicateCount = duplicateCount + 1
            else:
                links[x] = 1
        #print "File %s has %d links duplicates %d" % ( 
        #        filename, len(hrefs) , duplicateCount)
    print "duplicates: %d" % duplicateCount
    print "total links: %d" % len(links)

if __name__ == "__main__":
    main()

