===========================
 Colouring the bash prompt
===========================

I am entering this to document a favourite sequence for PS1::

  PS1="\[\033[1;34m\][\D{%a %d.%m.%y} \t \u@\h \w]$\[\033[0m\] "
  export PS1

The colours are shown in `section 6.1 <https://www.tldp.org/HOWTO/Bash-Prompt-HOWTO/x329.html>`_ of the `Bash Prompt HOWTO`_.

.. _`Bash Prompt HOWTO` : https://www.tldp.org/HOWTO/Bash-Prompt-HOWTO/index.html
