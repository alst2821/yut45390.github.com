.. _ref-fedora:

 Fedora Documentation
======================

Reference material
------------------

I am keeping here a link to `"Beyond Linux From Scratch"`_ which seems to
be an interesting read.  i stumbled upon the page while asking about
initramfs. Accessed okay on 20 Oct 2018.

.. _`"Beyond Linux From Scratch"`: http://www.linuxfromscratch.org/blfs/view/8.1/index.html

How to generate a password
--------------------------

I copied examples from `how to geek` on password generation:

    openssl rand -base64 32
    date +%s | sha256sum | base64 | head -c 32 ; echo
    < /dev/urandom tr -dc _A-Z-a-z-0-9 | head -c${1:-32};echo;

.. _`how to geek`:
   https://www.howtogeek.com/howto/30184/10-ways-to-generate-a-random-password-from-the-command-line/

How to find the source rpm of an installed package
--------------------------------------------------

This command outputs a source rpm for a package:

    rpm -qa --queryformat='%{NAME} %{SOURCERPM}\n' <package>

For example

    $ rpm -qa --queryformat='%{NAME} %{SOURCERPM}\n' python3-docutils
    python3-docutils python-docutils-0.14-6.fc30.src.rpm

the list of elements that can go in the query formats comes from

    rpm --querytags




