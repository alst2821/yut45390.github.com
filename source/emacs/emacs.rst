.. _ref-emacs:

Emacs
=====

Here is a link to some `emacs tips <https://sites.google.com/site/roneau2010/computer-software/emacs>`_.



Remove empty lines
^^^^^^^^^^^^^^^^^^

    M-x flush-lines RET ^$ RET

    (flush-lines REGEXP &optional RSTART REND INTERACTIVE)
    
Delete lines containing matches for REGEXP.  When called from Lisp
(and usually when called interactively as well, see below), applies to
the part of the buffer after point.  The line point is in is deleted
if and only if it contains a match for regexp starting after point.

    M-x keep-lines

Does the opposite, removes lines that don't contain matches

Tab width
^^^^^^^^^

To change the tab-width of emacs, use:

    M-x eval-expression
    (setq tab-width 8)

    
