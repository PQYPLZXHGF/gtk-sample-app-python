# gtk-sample-app-python
Sample application for Gtk with Python, Glade, GIntrospaction, and cx_freeze

<i>Tutorial for Windows</i>

Install Python 3 from https://www.python.org/downloads/windows/

For example, under  C:\PythonXX where XX is the version number

#Gtk binding with PyGobject

Install PyGobject (aka PyGI) from https://wiki.gnome.org/Projects/PyGObject

You must install Gtk with the installer (check Gtk).
Gtk will be installed under your previously Python path, in the subdirectory Script

<pre>
C:\PythonXX\Scripts\
</pre>

You may now test gtk_simple.py or gtk_builder.py with the python command line

##Create a standalone executable with CX freeze

# Setup Script GTK

A cx freeze setup script is a python file that list source files and
dependancies for the final stanalone, sortof like a CMake or Makefile script. 

There is a setup script on the gnome wiki, but it does not works as-is 
https://wiki.gnome.org/Projects/PyGObject?action=AttachFile&do=view&target=setup.py


To constructe the exetutable, ether gtk_simple or gtk_build, do

<pre> 
python setup_gtk_simple.py build
</pre>

or

<pre> 
python setup_gtk_builder.py build
</pre>

## source 
site     http://cx-freeze.sourceforge.net/
doc      http://cx-freeze.readthedocs.org/en/latest/index.html
see also http://cx-freeze.readthedocs.org/en/latest/distutils.html
