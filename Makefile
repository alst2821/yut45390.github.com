
PAGES := index bookmarks index1 docutils magit epics
PAGES := $(PAGES) python chinese-links

all: $(patsubst %,%.html, $(PAGES))

%.html: %.txt
	rst2html5 $< > $@


