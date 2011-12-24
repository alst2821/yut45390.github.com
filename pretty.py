from BeautifulSoup import BeautifulSoup
import os
import sys

def getFiles():
    list = filter(lambda x: x.endswith(".html"), os.listdir("."))
    list.sort()
    return list

def save(soup, filename, overwrite=False):
    if overwrite:
        output = filename
    else:
        output = filename + ".pretty"
    f = open(output, "w")
    f.write(soup.prettify())
    f.close()

def main():
    if sys.argv[1] == "-o":
        overwrite = True
    else:
        overwrite = False
    for filename in getFiles():
        print "*** %s *** " % filename
        f = open(filename, "r")
        soup = BeautifulSoup(f.read())
        f.close()
        save(soup, filename, overwrite)

if __name__ == "__main__":
    main()


