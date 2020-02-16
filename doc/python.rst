.. _ref-python:

======================
 Python related links
======================

* `Advanced python`_. Lecture on python by Thomas Wouters at Google. 21 Feb 2007 [#fn1]_
* `reddit channel for python`_
* `Numpy for Matlab users`_ (Accessed July 2019)
* `Matplotlib developers' guide`_ (Accessed July 2019)
* `Matplotlib usage guide`_ 


.. _`Advanced python`: https://www.youtube.com/watch?v=HlNTheck1Hk
.. _`reddit channel for python`: http://www.reddit.com/r/python
.. _`Numpy for Matlab users`: https://docs.scipy.org/doc/numpy/user/numpy-for-matlab-users.html
.. _`Matplotlib developers' guide`: https://matplotlib.org/devel/index.html#developers-guide-index
.. _`Matplotlib usage guide`: https://matplotlib.org/faq/usage_faq.html

.. rubric:: Footnotes

.. [#fn1] Accessed on 28 Aug 2019


Example using datetime
^^^^^^^^^^^^^^^^^^^^^^

The documentation of the `datetime module
<https://docs.python.org/3.7/library/datetime.html>`_ indicates that
there are these objects:
* datetime
* time
* timezone

.. code:: python

    import datetime
    import time
    b= 1261228562.0
    print(b)
    a = datetime.datetime.fromtimestamp(b)
    print(a)

=============
 Style guide
=============

* `Google python style guide`_ (part of the general `style guides`_).
  These guides are kept in a "styleguide" `github repo`_.

.. _`Google python style guide`: https://google.github.io/styleguide/pyguide.html
.. _`style guides`: https://google.github.io/styleguide/
.. _`github repo`: https://github.com/google/styleguide

* `Fluent python book by Luciano Ramalho (O'Reilly 2015) <http://shop.oreilly.com/product/0636920032519.do>`_.
  The `example code <https://github.com/fluentpython/example-code>`_ is in github.
  


