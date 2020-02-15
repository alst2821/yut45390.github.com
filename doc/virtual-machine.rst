==================================
 Lost password on virtual machine
==================================

I recently lost the password of 'root' on a debian virtual machine.
I found some `pointers <https://coderwall.com/p/vibura/reset-a-lost-password-on-an-ubuntu-vm>`_ to recover and I am grateful.

The things that I had to do were:
* Go into a root shell on startup.
  This needed to modify the grub line to add ::
    
    init=/bin/bash
* Remount the root folder as read-write. This is because it was
  read-only when the machine booted::
    mount -rw -o remount /

* I was then able to reset the password::
    passwd


    
