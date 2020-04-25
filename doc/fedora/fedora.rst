.. _ref-fedora:

Fedora Documentation and References
===================================

Reference material
------------------

* `Fedora start page <https://start.fedoraproject.org/>`_.

* `Fedora Code of Conduct <https://getfedora.org/code-of-conduct>`_.

* `Fedora Magazine <http://fedoramagazine.org/>`_.

* `Fedora Developer <https://developer.fedoraproject.org/>`_.

I am keeping here a link to `"Beyond Linux From Scratch"`_ which seems to
be an interesting read.  i stumbled upon the page while asking about
initramfs. Accessed okay on 20 Oct 2018.

.. _`"Beyond Linux From Scratch"`: http://www.linuxfromscratch.org/blfs/view/8.1/index.html

How to generate a password
--------------------------

I copied examples from `how to geek`_ on password generation::

    openssl rand -base64 32
    
    date +%s | sha256sum | base64 | head -c 32 ; echo
    
    < /dev/urandom tr -dc _A-Z-a-z-0-9 | head -c${1:-32};echo;

.. _`how to geek`:
   https://www.howtogeek.com/howto/30184/10-ways-to-generate-a-random-password-from-the-command-line/

How to find the source rpm of an installed package
--------------------------------------------------

This command outputs a source rpm for a package::

    rpm -qa --queryformat='%{NAME} %{SOURCERPM}\n' <package>

For example::

    $ rpm -qa --queryformat='%{NAME} %{SOURCERPM}\n' python3-docutils
    python3-docutils python-docutils-0.14-6.fc30.src.rpm

the list of elements that can go in the query formats comes from::

    rpm --querytags


Setting up a second monitor
---------------------------

For an all-in-one pc with a broken main display running Fedora.

The configuration below allows the pc to operate on a second monitor
ignoring the first monitor.

The configuration file is "monitors.xml" in the folder ~/.config

For gdm to operate the same way, I had to copy it to
/var/lib/gdm/.config::

  <monitors version="2">
    <configuration>
      <logicalmonitor>
        <x>0</x>
        <y>0</y>
        <scale>1</scale>
        <primary>yes</primary>
        <monitor>
          <monitorspec>
            <connector>HDMI-2</connector>
            <vendor>MED</vendor>
            <product>MD 20119</product>
            <serial>0x01010101</serial>
          </monitorspec>
          <mode>
            <width>1280</width>
            <height>1024</height>
            <rate>75.025177001953125</rate>
          </mode>
        </monitor>
      </logicalmonitor>
      <disabled>
        <monitorspec>
          <connector>HDMI-1</connector>
          <vendor>LEN</vendor>
          <product>Lenovo AIO PC</product>
          <serial>000001</serial>
        </monitorspec>
      </disabled>
    </configuration>
  </monitors>


And this is for a newer Lenovo ThinkPad laptop::

  <monitors version="2">
    <configuration>
      <logicalmonitor>
        <x>0</x>
        <y>0</y>
        <scale>1</scale>
        <primary>yes</primary>
        <monitor>
          <monitorspec>
            <connector>eDP-1</connector>
            <vendor>CMN</vendor>
            <product>0x15e5</product>
            <serial>0x00000000</serial>
          </monitorspec>
          <mode>
            <width>1680</width>
            <height>1050</height>
            <rate>59.954250335693359</rate>
          </mode>
        </monitor>
        <monitor>
          <monitorspec>
            <connector>HDMI-2</connector>
            <vendor>DEL</vendor>
            <product>DELL 2407WFP</product>
            <serial>UY5456BE10WS </serial>
          </monitorspec>
          <mode>
            <width>1680</width>
            <height>1050</height>
            <rate>59.883251190185547</rate>
          </mode>
        </monitor>
      </logicalmonitor>
    </configuration>
  </monitors>

  
