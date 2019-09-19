.. _ref-emacs:

Emacs
=====

Here is a link to some `emacs tips
<https://sites.google.com/site/roneau2010/computer-software/emacs>`_.

* `Emacs-devel mailing list archive
  <https://lists.gnu.org/archive/html/emacs-devel/>`_.
* `help-gnu-emacs mailing list archive
  <https://lists.gnu.org/archive/html/help-gnu-emacs/>`_.

Emacs tips
^^^^^^^^^^

Remove empty lines::

  M-x flush-lines RET ^$ RET

  (flush-lines REGEXP &optional RSTART REND INTERACTIVE)

Delete lines containing matches for REGEXP.  When called from Lisp
(and usually when called interactively as well, see below), applies to
the part of the buffer after point.  The line point is in is deleted
if and only if it contains a match for regexp starting after point.

Keep lines::

    M-x keep-lines

Does the opposite of `flush-lines`, removes lines that don't contain
matches.

To change the tab-width of emacs, use::

    M-x eval-expression
    (setq tab-width 8)


dired-x and .dired file
^^^^^^^^^^^^^^^^^^^^^^^

To ignore dot files in the output, set this into a ".dired" file::

  Local Variables:
  dired-omit-mode: t
  dired-actual-switches: "-l"
  End:

Spelling
^^^^^^^^

Add in customization the entry for ``ispell-program-name``::

  ispell-program-name "/usr/bin/hunspell"

or add this line in ``~/.emacs``::

  (setq ispell-program-name "/usr/bin/hunspell")

Convert line endings
^^^^^^^^^^^^^^^^^^^^

To convert to DOS or to Unix line endings [#fn1]_:

* Method 1: click on the indicator in the status line. Possible
  options are ":" for default encoding, (DOS) or (unix). Then save the
  file.

* Method 2: Run the command::

    C-x RET f (set-buffer-file-coding-system)
    
  and type unix/dos for unix encoding. This will change the encoding
  of newlines without changing the encoding of other characters.

  You can also change the encoding of other characters by typing
  something like utf-8-unix.

Navigate C sources
^^^^^^^^^^^^^^^^^^
Use the commands [#fn2]_::
  
  c-backward-conditional

  c-forward-conditional

  c-up-conditional

.. rubric:: Footnotes
.. [#fn1] Source: Emacs Stack Exchange `question <https://emacs.stackexchange.com/questions/5779/>`_ from 2014 by user Charo	    
.. [#fn2] Peter Lee, `"Matching #ifdefs..." <https://lists.gnu.org/archive/html/help-gnu-emacs/2003-01/msg01000.html>`_ in help-gnu-emacs mailing list. 31 Jan 2003.
  
Tramp on remote server
^^^^^^^^^^^^^^^^^^^^^^

Use the command::

  M-x find-file RET /scp:username@servername:/path/to/file

Chinese chars when UTF-16 file read
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This happens to me with the xml files from a program that erroneously
advertises the xml as UTF-16.

The solution, to show the xml normally (utf-8) is.

.. code:: 
	  
  M-x revert-buffer-with-coding-system

and choose ``binary`` encoding.
