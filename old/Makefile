
PAGES := index bookmarks 
PAGES := $(PAGES)  insurance

all: $(patsubst %,%.html, $(PAGES))

%.html: %.txt
	rst2html5 $< > $@


