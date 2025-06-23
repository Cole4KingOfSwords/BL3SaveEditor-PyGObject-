#Top of "C4K"

#Import
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

class value_input_box (Gtk.EventBox):
    def __init__(self):
        super().__init__()
        buttons = Gtk.Box(orientation="vertical")
        buttons.add(Gtk.Button(label="🢑", name="up_button"))
        buttons.add(Gtk.Button(label="🢓", name="down_button"))
        buttons.get_children()[0].connect("clicked", self.on_click, "+")
        buttons.get_children()[1].connect("clicked", self.on_click, "-")

        self.value = 0
        self.hovered = False

        self.entry_buffer = Gtk.EntryBuffer()
        entry_box = Gtk.Entry(max_length=2, buffer=self.entry_buffer)
        entry_box.connect("changed", self.on_input)

        widget_box = Gtk.Box()

        widget_box.add(entry_box)
        widget_box.add(buttons)

        self.add(widget_box)

        self.set_events(Gdk.EventMask.ENTER_NOTIFY_MASK |
                   Gdk.EventMask.LEAVE_NOTIFY_MASK |
                   Gdk.EventMask.SCROLL_MASK)

        self.connect("enter-notify-event", self.hover_bool, "enter")
        self.connect("leave-notify-event", self.hover_bool, "exit")
        self.connect("scroll-event", self.on_scroll)

        self.set_above_child(True)
        self.show_all()


    def on_input(self, callback):
        if self.entry_buffer.get_text().isdigit():
            self.change_value(int(self.entry_buffer.get_text()))
        elif self.entry_buffer.get_text() == "":
            self.change_value(0)
        else:
            self.entry_buffer.set_text(str(self.value), 1)
    def on_click(self, callback, click_type):
        match click_type:
            case "+":
                self.value += 1
            case "-" if self.value > 0:
                self.value -= 1
        self.entry_buffer.set_text(str(self.value), len(str(self.value)))

    def on_scroll(self, widget, event):
        if self.hovered:
            match event.get_scroll_direction().direction:
                case 0: #scroll up
                    self.value += 1
                case 1: #scroll down
                    if self.value > 0:
                        self.value -= 1
                case _: #Useless
                    print(event, ":ERR? did not catch Scroll direction")
            self.entry_buffer.set_text(str(self.value), len(str(self.value)))
    def change_value(self, value_int):
        self.value = value_int

    def hover_bool(self, callback, event, event_flag):
       match event_flag:
           case "enter":
               self.hovered = True
           case "exit":
               self.hovered = False