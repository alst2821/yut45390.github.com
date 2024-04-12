.. _ref-docutils:

==========
 Docutils
==========
:Info: See <https://docutils.sourceforge.io/rst.html> for introductory docs.

.. NOTE:: If you are reading this as HTML, please read
   `cheatsheet (txt)`_ instead to see the input syntax examples!

.. _`cheatsheet (txt)`: http://docutils.sourceforge.net/docs/user/rst/cheatsheet.txt

Docutils is independent of `Sphinx <http://www.sphinx-doc.org/>`_.

.. _Sphinx: http://www.sphinx-doc.org/

Sphinx is used to create documentation for Python. It builds from the
reStructuredText format used by docutils and is used to create many
important bodies of documentation.

For my application, I only want to create a static website with
entries and links. I had been using google sites, but I am now not
pleased with the management of content there. The site has a lot of
content that depends on the stability of google. What would happen to
the data if google discontinues 'sites'?

The docutils documentation is at the project's `web page`_. at
http://docutils.sourceforge.net/

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
time. However for Sphinx_ the advice is to use references with
the :ref: keyword. This is documented as part of Sphinx here_.

.. _`generate links and tables`:
   http://docutils.sourceforge.net/docs/user/rst/cheatsheet.txt
   
.. _here: http://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#ref-role

How to make a table
-------------------

Use the `list-table directive`_.

.. _`list-table directive`: https://docutils.sourceforge.io/docs/ref/rst/directives.html#list-table

The way to generate link is to use the "``_``" character next to the
relevant text.  For example ``reference_``. Then a section below
preceded by "``..``", then "``_``" and the same reference, in this
case ``_reference``, a colon "``:``" and the url.


* Link to a `cheatsheet <http://docutils.sourceforge.net/docs/user/rst/cheatsheet.txt>`_ at sourceforge.io
  and its associated `html output <https://docutils.sourceforge.io/docs/user/rst/cheatsheet.html>`_.
