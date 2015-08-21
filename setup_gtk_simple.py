from cx_Freeze import setup, Executable
import site
import sys
import os

if sys.platform == "win32":
    base = "Win32GUI"

site_dir = site.getsitepackages()[1]
gnome_dir = os.path.join(site_dir, "gnome")
include_files = []
includes = ['gi']
excludes = []
packages = ['gi']

#list of dll to copy
dll_list = ['libatk-1.0-0.dll',
            'libffi-6.dll',
            'libfontconfig-1.dll',
            'libfreetype-6.dll',
            'libgio-2.0-0.dll',
            'libgirepository-1.0-1.dll',
            'libglib-2.0-0.dll',
            'libgmodule-2.0-0.dll',
            'libintl-8.dll',
            'libgobject-2.0-0.dll',
            'libgtk-3-0.dll',
            'libharfbuzz-gobject-0.dll',
            'libjasper-1.dll',
            'libpng16-16.dll',
            'librsvg-2-2.dll',
            'libwebp-5.dll',
            'libwinpthread-1.dll',
            'libxmlxpat.dll',
            'libcairo-gobject-2.dll',
            'libgdk-3-0.dll',
            'libgdk_pixbuf-2.0-0.dll',
            'libgnutls-26.dll',
            'libjpeg-8.dll',
            'libpango-1.0-0.dll',
            'libpangocairo-1.0-0.dll',
            'libpangoft2-1.0-0.dll',
            'libpangowin32-1.0-0.dll',
            'libzzz.dll']
for dll in dll_list:
    include_files.append((os.path.join(gnome_dir, dll), dll))  

	
#copy the girepository typelibs
include_files.append((os.path.join(gnome_dir, 'lib/girepository-1.0'), 'lib/girepository-1.0')) 

#copy subdirectories
gnome_subdirs = [
    'etc', 
    #'lib', 
    #'share'
]
for gnome_subdir in gnome_subdirs:
    include_files.append((os.path.join(gnome_dir, gnome_subdir), gnome_subdir))

for gnome_subdir in gnome_subdirs:
    include_files.append((os.path.join(gnome_dir, gnome_subdir), gnome_subdir))
    
executables = [Executable('gtk_simple.py', base=base)]

options_build_exe = {
    'include_msvcr': True,
    'includes': includes,
    'excludes': excludes,
    'packages': packages,
    'include_files':include_files,
}

setup(name='GTK SIMPLE',
      version = '1.0',
      description = '',
      options = {"build_exe":options_build_exe},
      executables = executables)
