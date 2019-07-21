======================
 Fedora Documentation
======================

How to find the source rpm of an installed package
--------------------------------------------------

This was originally in `other linux`_ page.

This command outputs a source rpm for a package:

    rpm -qa --queryformat='%{NAME} %{SOURCERPM}\n' <package>

For example

    $ rpm -qa --queryformat='%{NAME} %{SOURCERPM}\n' python3-docutils
    python3-docutils python-docutils-0.14-6.fc30.src.rpm

the list of elements that can go in the query formats comes from

    rpm --querytags


.. _`other linux`: https://sites.google.com/site/thelinux2017/fedora/find

