
all: index1.html docutils.html magit.html

%.html: %.txt
	rst2html5 $< > $@


