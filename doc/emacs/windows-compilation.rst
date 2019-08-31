=======================================================
Using emacs ``M-x compile`` to generate windows targets
=======================================================

Use a script similar to the one below. It was obtained from an
environment as populated by ``vcvars.bat`` (visual studio command line
compiler invocation batch file).  Name it "emacs-env.bat".  Then one
can use the emacs M-x compile command to invoke visual studio so::

  M-x compile RET
  X:/path/to/script/emacs-env.bat make RET

.. code:: batch
	  
 @set CommandPromptType=Native
 @set Framework35Version=v3.5
 @set FrameworkDir=C:\Windows\Microsoft.NET\Framework64
 @set FrameworkDIR64=C:\Windows\Microsoft.NET\Framework64
 @set FrameworkVersion=v4.0.30319
 @set FrameworkVersion64=v4.0.30319
 @set FSHARPINSTALLDIR=c:\Program Files (x86)\Microsoft F#\v4.0\
 @set INCLUDE=c:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\INCLUDE
 @set INCLUDE=%INCLUDE%;c:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\ATLMFC\INCLUDE
 @set INCLUDE=%INCLUDE%;C:\Program Files (x86)\Microsoft SDKs\Windows\v7.0A\include
 @set LIB=c:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\LIB\amd64
 @set LIB=%LIB%;c:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\ATLMFC\LIB\amd64
 @set LIB=%LIB%;C:\Program Files (x86)\Microsoft SDKs\Windows\v7.0A\lib\x64
 @set LIBPATH=C:\Windows\Microsoft.NET\Framework64\v4.0.30319
 @set LIBPATH=%LIBPATH%;C:\Windows\Microsoft.NET\Framework64\v3.5
 @set LIBPATH=%LIBPATH%;c:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\LIB\amd64
 @set LIBPATH=%LIBPATH%;c:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\ATLMFC\LIB\amd64
 @set path=
 @set path=%path%;c:\python27\
 @set path=%path%;c:\perl64\site\bin
 @set path=%path%;c:\perl64\bin
 @set path=%path%;c:\windows\system32
 @set path=%path%;c:\windows
 @set path=%path%;c:\windows\system32\wbem
 @set path=%path%;c:\windows\system32\windowspowershell\v1.0\
 @set path=%path%;c:\program files (x86)\microsoft sql server\100\tools\binn\
 @set path=%path%;c:\program files\microsoft sql server\100\tools\binn\
 @set path=%path%;c:\program files\microsoft sql server\100\dts\binn\
 @set path=%path%;c:\program files (x86)\subversion\bin
 @set path=%path%;c:\windows\system32
 @set path=%path%;c:\program files\tortoisesvn\bin
 @set path=%path%;c:\matlab2011b\bin
 @set path=%path%;c:\program files\matlab\r2011b\bin
 @set path=%path%;c:\program files\dell\sysmgt\oma\bin
 @set path=%path%;c:\program files\dell\sysmgt\shared\bin
 @set path=%path%;c:\program files\dell\sysmgt\idrac
 @set path=%path%;c:\anaconda
 @set path=%path%;c:\anaconda\scripts
 @set path=%path%;c:\program files (x86)\git\cmd
 @set path=%path%;c:\program files (x86)\microsoft visual studio 10.0\vc\bin\amd64
 @set path=%path%;c:\windows\microsoft.net\framework64\v4.0.30319
 @set path=%path%;c:\windows\microsoft.net\framework64\v3.5
 @set path=%path%;c:\program files (x86)\microsoft visual studio 10.0\vc\vcpackages
 @set path=%path%;c:\program files (x86)\microsoft visual studio 10.0\common7\ide
 @set path=%path%;c:\program files (x86)\microsoft visual studio 10.0\common7\tools
 @set path=%path%;c:\program files (x86)\html help workshop
 @set path=%path%;c:\program files (x86)\microsoft sdks\windows\v7.0a\bin\netfx 4.0 tools\x64
 @set path=%path%;c:\program files (x86)\microsoft sdks\windows\v7.0a\bin\x64
 @set path=%path%;c:\program files (x86)\microsoft sdks\windows\v7.0a\bin
 @set path=%path%;c:\python27\
 @set path=%path%;c:\windows\system32
 @set path=%path%;c:\windows
 @set path=%path%;c:\windows\system32\wbem
 @set path=%path%;c:\windows\system32\windowspowershell\v1.0\
 @set path=%path%;c:\program files (x86)\microsoft sql server\100\tools\binn\
 @set path=%path%;c:\program files\microsoft sql server\100\tools\binn\
 @set path=%path%;c:\program files\microsoft sql server\100\dts\binn\
 @set path=%path%;c:\program files (x86)\subversion\bin
 @set path=%path%;c:\windows\system32
 @set path=%path%;c:\program files\tortoisesvn\bin
 @set path=%path%;c:\matlab2011b\bin
 @set path=%path%;c:\program files\matlab\r2011b\bin
 @set path=%path%;c:\program files\dell\sysmgt\oma\bin
 @set path=%path%;c:\program files\dell\sysmgt\shared\bin
 @set path=%path%;c:\program files\dell\sysmgt\idrac
 @set path=%path%;c:\anaconda
 @set path=%path%;c:\anaconda\scripts
 @set path=%path%;c:\program files (x86)\gnuwin32\bin
 @set path=%path%;c:\program files (x86)\vim\vim73
 @set path=%path%;c:\program files (x86)\re2c
 @set Platform=X64
 @set VCINSTALLDIR=c:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\
 @set VS100COMNTOOLS=C:\Program Files (x86)\Microsoft Visual Studio 10.0\Common7\Tools\
 @set VSINSTALLDIR=c:\Program Files (x86)\Microsoft Visual Studio 10.0\
 @set WindowsSdkDir=C:\Program Files (x86)\Microsoft SDKs\Windows\v7.0A\
 %*
 
