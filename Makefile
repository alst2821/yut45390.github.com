
all: index1.html docutils.html blog_post1.html

docutils.html: docutils.txt
	rst2html5 docutils.txt > $@

%.html: %.txt
	rst2html5 $< > $@


