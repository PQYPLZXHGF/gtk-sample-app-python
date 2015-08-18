from gi.repository import Gtk

class Handler:
    def gtk_main_quit(self, *args):
        Gtk.main_quit(*args)

    def on_imagemenuitem_about_activate(self, menuitem):
        aboutdialog = builder.get_object("aboutdialog")
        aboutdialog.run()
        aboutdialog.hide()

    def on_button_load_clicked(self, button):
        print ('load')
            
    def on_button_save_clicked(self, button):
        print ('save')

builder = Gtk.Builder()
builder.add_from_file("share/sampleapp/sampleapp.glade")
builder.connect_signals(Handler())

window = builder.get_object("window")
window.show_all()

Gtk.main()
