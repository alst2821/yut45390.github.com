=======================================
 Notes on debian system administration
=======================================

Notes taken last decade when I used to work with debian systems.

How to get the list of packages installed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
::
   
   dpkg --list

To remove subversion::

  apt-get remove subversion
  apt-get remove libsvn0

How to know which packages may be upgraded
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

   apt-show-versions -u

