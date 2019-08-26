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

Raid disk stuff
^^^^^^^^^^^^^^^

RAID-1 mirror reconstruction notes. These I have not used since 2008,
so ``man mdadm`` may have much better information!

Mark as failed::

  mdadm /dev/md0 -f /dev/hda1

Remove from array::

  mdadm /dev/md0 -r /dev/hda1

Add to array as spare::

  mdadm -a /dev/hda1

  
