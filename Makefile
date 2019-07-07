
PAGES := index bookmarks index1 docutils magit

all: $(patsubst %,%.html, $(PAGES))

%.html: %.txt
	rst2html5 $< > $@


