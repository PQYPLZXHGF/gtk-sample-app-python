from gi.repository import Gtk
import requests

class Handler:
    def gtk_main_quit(self, *args):
        Gtk.main_quit(*args)

    def on_imagemenuitem_about_activate(self, menuitem):
        aboutdialog = builder.get_object("aboutdialog")
        aboutdialog.run()
        aboutdialog.hide()

    def on_button_load_clicked(self, button):
        entry_address = builder.get_object("entry_address")
        address = entry_address.get_text()

        #get the page content
        page = requests.get(address)      

        #display the html
        textbuffer_html = builder.get_object("textbuffer_html")
        textbuffer_html.set_text(page.text, len(page.text))

builder = Gtk.Builder()
builder.add_from_file("share/sampleapp_net/sampleapp.glade")
builder.connect_signals(Handler())

window = builder.get_object("window")
window.set_default_size(400, 200)
window.show_all()

Gtk.main()
