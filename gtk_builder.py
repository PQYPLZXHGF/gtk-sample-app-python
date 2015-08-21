from gi.repository import Gtk, Gio

class Handler:
    schema_id = "sampleapp"
    
    def __init__(self):
        self.settings = Gio.Settings.new(self.schema_id)
    
    def gtk_main_quit(self, *args):
        Gtk.main_quit(*args)

    def on_imagemenuitem_about_activate(self, menuitem):
        aboutdialog = builder.get_object("aboutdialog")
        aboutdialog.run()
        aboutdialog.hide()

    def on_button_load_clicked(self, button):
        message = self.settings.get_string("message");
        entry_message = builder.get_object("entry_message")
        entry_message.set_text(message)
            
    def on_button_save_clicked(self, button):
        entry_message = builder.get_object("entry_message")
        message = entry_message.get_text()
        self.settings.set_string("message", message)

builder = Gtk.Builder()
builder.add_from_file("share/sampleapp/sampleapp.glade")
builder.connect_signals(Handler())

window = builder.get_object("window")
window.show_all()

Gtk.main()
