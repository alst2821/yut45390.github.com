.. _ref-docutils:

=============
rst2html blog
=============

I discovered that rst2html is part of docutils and it is independent
of Sphinx_.

.. _Sphinx: http://www.sphinx-doc.org/

Sphinx seems to be great to create documentation. It builds from the
reStructuredText format used by docutils and is used to create many
important bodies of documentation. The most notable are the help pages
for Python.

For my application, I only want to create a blog with entries and
links. I had been using google sites, but I am now not pleased with
the management of content there. The site has a lot of content that
depends on the stability of google. What would happen to the data if
google went out of business?

That may not happen soon, but a similar thing could happen if google
decided that they need to restructure the business and decide to cut
down sections of the service, like google sites.

The link to the docutils documentation is a link away from the
project's `web page`_. at http://docutils.sourceforge.net/

.. _`web page`: http://docutils.sourceforge.net/


I found among the `docutils documentation pages`_ that there is an
`emacs mode`_ for docutils. and it works by invoking 'rst-mode'.

.. _`docutils documentation pages`:
   http://docutils.sourceforge.net/docs/index.html
.. _`emacs mode`:
   http://docutils.sourceforge.net/docs/user/emacs.html

There are examples of what can be done to `generate links and
tables`_.  References and inline targets sound more esoteric.  So far
I am quite glad that I can include links. I use those most of the
time.

.. _`generate links and tables`:
   http://docutils.sourceforge.net/docs/user/rst/cheatsheet.txt

The way to generate link is to use the "``_``" character next to the
relevant text.  For example ``reference_``. Then a section below
preceded by "``..``", then "``_``" and the same reference, in this
case ``_reference``, a colon "``:``" and the url.


