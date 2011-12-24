from BeautifulSoup import BeautifulSoup
import os

def getFiles():
    list = filter(lambda x: x.endswith(".html"), os.listdir("."))
    list.sort()
    return list

def save(soup, filename):
    f = open(filename + ".pretty", "w")
    f.write(soup.prettify())
    f.close()

def main():
    for filename in getFiles():
        print "*** %s *** " % filename
        f = open(filename, "r")
        soup = BeautifulSoup(f.read())
        f.close()
        save(soup, filename)

if __name__ == "__main__":
    main()


