#Top
""""
This should probably be written in c for GObject, but many BL3 tools are
already written in Python so f it

Written By Cole4King
"""

#-Import
import gi
import subprocess
import jinja2
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, Gio

#-Main
class main:
    def __init__(self):
        def build_from_xml():
            #-Style
            css = Gtk.CssProvider()
            css.load_from_path("main.css")
            screen = Gdk.Screen.get_default()
            style_context = Gtk.StyleContext()
            style_context.add_provider_for_screen(screen, css, 1)

            #-Template
            jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(""))
            jinja_template = jinja_environment.get_template("main.xml")
            jinja_render = jinja_template.render()

            #-build
            build = Gtk.Builder()
            build.add_from_string(jinja_render)
            return build
        self.build = build_from_xml()
        self.window = self.build.get_object("window")
        self.view_box = self.build.get_object("view")
        self.window.show_all()
        self.window.present()
        self.connect_signals()
        self.save_file = None
    def file_status(self):
        if self.save_file is None:
            return False
        else:
            return True

    #-Functions
    def switch_view(self, callback,view_str):
        print(view_str)
        view_box = self.view_box
        build = self.build
        if not self.file_status():
            return
        if type(view_str) is not str:
            return
        else:
            pass
        for child in view_box:
            view_box.remove(child)
            pass
        match view_str:
            case "general_view":
                view_box.add(build.get_object("general_view"))
            case "character_view":
                view_box.add(build.get_object("character_view"))
            case "fast_t_view":
                view_box.add(build.get_object("fast_t_view"))
            case "inv_view":
                view_box.add(build.get_object("inv_view"))
                print("gg")
            case "raw_view":
                view_box.add(build.get_object("raw_view"))
            case "profile_view":
                view_box.add(build.get_object("profile_view"))
            case "about_view":
                view_box.add(build.get_object("about_view"))
            case "test_view":
                view_box.add(build.get_object("test"))
        self.window.show_all()

    def connect_signals(self):
        view_buttons = [
            "general_",
            "character_",
            "fast_t_",
            "inv_",
            "raw_",
            "profile_",
            "about_",
        ]
        for view_button in view_buttons:
            print(view_button + " " + str(self.build.get_object(view_button + "button")))
            self.build.get_object(view_button + "button").connect("clicked", self.switch_view, str(view_button + "view"))
        self.build.get_object("open").connect("activate", self.open_file)
        self.build.get_object("window").connect("destroy", quit)
    def open_file(self, *callback):
        self.save_file = subprocess.run(["kdialog", "--getopenfilename"], capture_output=True, text=True).stdout.strip()
        save_file = open(self.save_file, "rb").read()
#

Main = main()
Gtk.main()
print("GotToEnd")

#Bottom