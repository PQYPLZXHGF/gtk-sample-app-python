# gtk-sample-app-python
Sample application for Gtk with Python, Glade, GIntrospaction, and cx_freeze

<i>Tutorial for Windows</i>

Install Python 3 from https://www.python.org/downloads/windows/

For example, under  C:\PythonXX where XX is the version number

#Gtk binding with PyGobject

<pre>
Install PyGobject pygi-aio-3.14.0_rev19-setup.exe (aka PyGI)
from http://sourceforge.net/projects/pygobjectwin32/files/
</pre>
You must install Gtk with the installer (checkbox Gtk-...).
Gtk will be installed under your Python path, in the Script subdirectory


    C:\PythonXX\Scripts\


You may now test gtk_simple.py or gtk_builder.py with the python command line

##Create a standalone executable with CX freeze

#install it

from http://cx-freeze.sourceforge.net/

# Setup Script GTK

A cx freeze setup script is a python file that list source files and
dependancies for the final stanalone, sort-of like a CMake or Makefile script. 

There is a setup script on the gnome wiki, but it does not works as-is

https://wiki.gnome.org/Projects/PyGObject?action=AttachFile&do=view&target=setup.py

To constructe an exe, gtk_simple.exe or gtk_build.exe, do

<pre> 
python setup_gtk_simple.py build
</pre>

or

<pre> 
python setup_gtk_builder.py build
</pre>

## sources
<pre>
site http://cx-freeze.sourceforge.net/
doc  http://cx-freeze.readthedocs.org/en/latest/index.html
and  https://wiki.gnome.org/Projects/PyGObject
</pre>