.. _ref-emacs:

Emacs
=====

Here is a link to some `emacs tips
<https://sites.google.com/site/roneau2010/computer-software/emacs>`_.

* `Emacs-devel mailing list archive
  <https://lists.gnu.org/archive/html/emacs-devel/>`_.

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


