from gi.repository import Gtk

class Handler:
    def gtk_main_quit(self, *args):
        Gtk.main_quit(*args)

    def on_imagemenuitem_about_activate(self, menuitem):
        aboutdialog = builder.get_object("aboutdialog")
        aboutdialog.run()
        aboutdialog.hide()

builder = Gtk.Builder()
builder.add_from_file("glade/ui.glade")
builder.connect_signals(Handler())

window = builder.get_object("window")
window.show_all()

Gtk.main()