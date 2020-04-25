=======================================
 Notes on debian system administration
=======================================

Notes taken over 10 years ago, when I used to work with Debian
systems.

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

Debian sources.list for apt
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The `sources list page`_ [#fn3]_ on the debian wiki explains what one has
to add to the apt/sources.list file to use contrib non-free

.. _`sources list page`: https://wiki.debian.org/SourcesList


Notes about debian packaging
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Per Abrahamsen, `"Distribute a single executable as a .deb file"`_.
  Per Abrahamsen's blog. March 2016.  Notes from packaging an
  executable in a debian package. [#fn1]_

* Lucas Nussbaum, `"Debian packaging tutorial"`_ (pdf). debian.org
  site. 89 slides.  Aug 2017. [#fn2]_

Slide 7 explains that a .deb archive is an "ar" (archive, as processed
by the library tool ar)::
  
  $ ar tv wget_1 .12 -2.1 _i386.deb
  
The command above wil extract the components, a binary, a control and
a data component.

* `Building tutorial`_. Debian Wiki. [#fn1]_

.. _`"Distribute a single executable as a .deb file"`: http://per-abrahamsen.blogspot.co.uk/2016/03/distribute-single-executable-as-deb-file.html

.. _`"Debian packaging tutorial"`: https://www.debian.org/doc/manuals/packaging-tutorial/packaging-tutorial.en.pdf

.. _`Building tutorial`: https://wiki.debian.org/BuildingTutorial

* Building packages

  Following the guide above (debian packaging tutorial) I just installed
  build-essential on my system.

  Now the devscripts fails to install though.

  The error looks so::

    ronaldo@debian:~$ sudo apt-get install devscripts
    Reading package lists... Done
    Building dependency tree
    Reading state information... Done
    The following additional packages will be installed:
      at autoconf automake autopoint autotools-dev dctrl-tools debhelper debian-keyring
      dh-autoreconf dh-strip-nondeterminism diffstat dput dwz equivs gettext intltool-debian
      libapt-pkg-perl libarchive-cpio-perl libarchive-zip-perl libasync-mergepoint-perl
      libb-hooks-endofscope-perl libb-hooks-op-check-perl libcapture-tiny-perl libcgi-fast-perl
      libcgi-pm-perl libclass-accessor-perl libclass-inspector-perl
      libclass-method-modifiers-perl libclass-xsaccessor-perl libclone-perl libcommon-sense-perl
      libconst-fast-perl libcontextual-return-perl libconvert-binhex-perl libdata-optlist-perl
      libdevel-callchecker-perl libdevel-globaldestruction-perl libdigest-bubblebabble-perl
      libdigest-hmac-perl libdistro-info-perl libdynaloader-functions-perl libemail-valid-perl
      libexporter-tiny-perl libfcgi-perl libfile-chdir-perl libfile-homedir-perl
      libfile-stripnondeterminism-perl libfile-which-perl libfl2 libfuture-perl
      libgetopt-long-descriptive-perl libgit-wrapper-perl libgitlab-api-v4-perl
      libhttp-tiny-multipart-perl libimport-into-perl libio-async-perl libio-prompter-perl
      libio-pty-perl libio-sessiondata-perl libio-string-perl libipc-run-perl libjson-perl
      libjson-xs-perl liblist-compare-perl liblist-moreutils-perl liblog-any-adapter-screen-perl
      liblog-any-perl libltdl-dev libmail-sendmail-perl libmime-tools-perl
      libmodule-implementation-perl libmodule-runtime-perl libmoo-perl libnamespace-clean-perl
      libnet-dns-perl libnet-dns-sec-perl libnet-domain-tld-perl libnet-ip-perl
      libnet-libidn-perl libnumber-compare-perl libnumber-range-perl libossp-uuid-perl
      libossp-uuid16 libpackage-stash-perl libpackage-stash-xs-perl libparams-classify-perl
      libparams-util-perl libparams-validate-perl libparse-debianchangelog-perl
      libpath-iterator-rule-perl libpath-tiny-perl libperlio-gzip-perl libpod-constants-perl
      libreadonly-perl libref-util-perl libref-util-xs-perl libregexp-pattern-license-perl
      librole-tiny-perl libsereal-decoder-perl libsereal-encoder-perl libsereal-perl libsigsegv2
      libsoap-lite-perl libsort-key-perl libsort-versions-perl libstrictures-perl
      libstring-copyright-perl libstring-escape-perl libstring-shellquote-perl
      libstruct-dumb-perl libsub-exporter-perl libsub-exporter-progressive-perl
      libsub-identify-perl libsub-install-perl libsub-name-perl libsub-quote-perl
      libsys-hostname-long-perl libtask-weaken-perl libterm-readkey-perl libtest-fatal-perl
      libtest-refcount-perl libtext-glob-perl libtext-levenshtein-perl libtool libtype-tiny-perl
      libtype-tiny-xs-perl libtypes-serialiser-perl libunicode-utf8-perl libvariable-magic-perl
      libwant-perl libxml-libxml-perl libxml-namespacesupport-perl libxml-sax-base-perl
      libxml-sax-expat-perl libxml-sax-perl libxml-simple-perl libxmlrpc-lite-perl
      libyaml-libyaml-perl licensecheck lintian m4 patchutils po-debconf python3-gpg
      python3-magic python3-unidiff strace t1utils wdiff
    Suggested packages:
      autoconf-archive gnu-standards autoconf-doc debtags dh-make adequate autopkgtest
      bls-standalone check-all-the-things cvs-buildpackage devscripts-el diffoscope disorderfs
      dose-extra duck faketime gnuplot how-can-i-help libdbd-pg-perl libnet-smtps-perl
      libterm-size-perl libyaml-syck-perl mozilla-devscripts mutt piuparts postgresql-client
      quilt ratt reprotest svn-buildpackage w3m mini-dinstall rsync gettext-doc libasprintf-dev
      libgettextpo-dev libtool-doc uuid libscalar-number-perl libhtml-template-perl
      libapache2-mod-perl2 libmime-lite-perl libnet-jabber-perl libbareword-filehandles-perl
      libindirect-perl libmultidimensional-perl gfortran | fortran95-compiler gcj-jdk
      libdevel-lexalias-perl libdevel-stacktrace-perl libxml-sax-expatxs-perl binutils-multiarch
      libtext-template-perl m4-doc libmail-box-perl wdiff-doc
    The following NEW packages will be installed:
      at autoconf automake autopoint autotools-dev dctrl-tools debhelper debian-keyring
      devscripts dh-autoreconf dh-strip-nondeterminism diffstat dput dwz equivs gettext
      intltool-debian libapt-pkg-perl libarchive-cpio-perl libarchive-zip-perl
      libasync-mergepoint-perl libb-hooks-endofscope-perl libb-hooks-op-check-perl
      libcapture-tiny-perl libcgi-fast-perl libcgi-pm-perl libclass-accessor-perl
      libclass-inspector-perl libclass-method-modifiers-perl libclass-xsaccessor-perl
      libclone-perl libcommon-sense-perl libconst-fast-perl libcontextual-return-perl
      libconvert-binhex-perl libdata-optlist-perl libdevel-callchecker-perl
      libdevel-globaldestruction-perl libdigest-bubblebabble-perl libdigest-hmac-perl
      libdistro-info-perl libdynaloader-functions-perl libemail-valid-perl libexporter-tiny-perl
      libfcgi-perl libfile-chdir-perl libfile-homedir-perl libfile-stripnondeterminism-perl
      libfile-which-perl libfl2 libfuture-perl libgetopt-long-descriptive-perl
      libgit-wrapper-perl libgitlab-api-v4-perl libhttp-tiny-multipart-perl libimport-into-perl
      libio-async-perl libio-prompter-perl libio-pty-perl libio-sessiondata-perl
      libio-string-perl libipc-run-perl libjson-perl libjson-xs-perl liblist-compare-perl
      liblist-moreutils-perl liblog-any-adapter-screen-perl liblog-any-perl libltdl-dev
      libmail-sendmail-perl libmime-tools-perl libmodule-implementation-perl
      libmodule-runtime-perl libmoo-perl libnamespace-clean-perl libnet-dns-perl
      libnet-dns-sec-perl libnet-domain-tld-perl libnet-ip-perl libnet-libidn-perl
      libnumber-compare-perl libnumber-range-perl libossp-uuid-perl libossp-uuid16
      libpackage-stash-perl libpackage-stash-xs-perl libparams-classify-perl libparams-util-perl
      libparams-validate-perl libparse-debianchangelog-perl libpath-iterator-rule-perl
      libpath-tiny-perl libperlio-gzip-perl libpod-constants-perl libreadonly-perl
      libref-util-perl libref-util-xs-perl libregexp-pattern-license-perl librole-tiny-perl
      libsereal-decoder-perl libsereal-encoder-perl libsereal-perl libsigsegv2 libsoap-lite-perl
      libsort-key-perl libsort-versions-perl libstrictures-perl libstring-copyright-perl
      libstring-escape-perl libstring-shellquote-perl libstruct-dumb-perl libsub-exporter-perl
      libsub-exporter-progressive-perl libsub-identify-perl libsub-install-perl libsub-name-perl
      libsub-quote-perl libsys-hostname-long-perl libtask-weaken-perl libterm-readkey-perl
      libtest-fatal-perl libtest-refcount-perl libtext-glob-perl libtext-levenshtein-perl libtool
      libtype-tiny-perl libtype-tiny-xs-perl libtypes-serialiser-perl libunicode-utf8-perl
      libvariable-magic-perl libwant-perl libxml-libxml-perl libxml-namespacesupport-perl
      libxml-sax-base-perl libxml-sax-expat-perl libxml-sax-perl libxml-simple-perl
      libxmlrpc-lite-perl libyaml-libyaml-perl licensecheck lintian m4 patchutils po-debconf
      python3-gpg python3-magic python3-unidiff strace t1utils wdiff
    0 upgraded, 150 newly installed, 0 to remove and 4 not upgraded.
    Need to get 1,046 kB/46.9 MB of archives.
    After this operation, 77.9 MB of additional disk space will be used.
    Do you want to continue? [Y/n] y
    Err:1 http://deb.debian.org/debian buster/main amd64 devscripts amd64 2.19.5
      404  Not Found [IP: 151.101.60.204 80]
    E: Failed to fetch http://deb.debian.org/debian/pool/main/d/devscripts/devscripts_2.19.5_amd64.deb  404  Not Found [IP: 151.101.60.204 80]
    E: Unable to fetch some archives, maybe run apt-get update or try with --fix-missing?

  The solution for me was to follow the `steps`_  suggested by ognjen::

    apt-get clean
    rm -rf /var/lib/apt/lists/*
    apt-get clean
    apt-get update
    apt-get upgrade

.. _`steps`: https://askubuntu.com/questions/711794/apt-get-update-always-failed-to-fetch


.. rubric:: Footnotes

.. [#fn1] Accessed Aug 2019
	     
.. [#fn2] Accessed March 2018


.. [#fn3] Accessed Apr 2020
          
