=====
magit
=====

Magit is an emacs based git package. I use magit_ and I sometimes find
it convenient.

.. _magit: https://magit.vc/manual/magit/index.html

The user manual gets installed as info pages in emacs, but there is a
version online `too <https://magit.vc/manual/magit/index.html>`_

Installation
------------

The melpa method is::

  (require 'package)
  (add-to-list 'package-archives
             '("melpa" . "http://melpa.org/packages/") t)

  M-x package-refresh-contents RET
  M-x package-install RET magit RET

