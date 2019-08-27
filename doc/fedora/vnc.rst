==========================
 Setting up a vnc session
==========================

On the linux workstation::

  sudo dnf install tigervnc-server
  vncserver :1 -name <my-session-name> -geometry 1200x850

To set the password::

  vncpasswd

On the Mac OS system (client)::

  open vnc://username:passwd@host-ip:5901


