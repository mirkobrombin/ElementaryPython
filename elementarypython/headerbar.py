#!/usr/bin/python3
'''
   Copyright 2017 Mirko Brombin <send@mirko.pm>

   This file is part of ElementaryPython.

    ElementaryPython is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    ElementaryPython is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with ElementaryPython.  If not, see <http://www.gnu.org/licenses/>.
'''

import constants as cn
import gi
import webbrowser
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


class Headerbar(Gtk.HeaderBar):

    def __init__(self):

        Gtk.HeaderBar.__init__(self)

        self.set_show_close_button(True)
        self.props.title = cn.App.application_name

        # help button
        self.hbar_help = Gtk.ToolButton()
        self.hbar_help.set_icon_name("help-contents")
        self.hbar_help.connect("clicked", self.on_hbar_help_clicked)
        self.pack_end(self.hbar_help)
        
        # color button
        self.hbar_color = Gtk.ColorButton.new_with_rgba(Gdk.RGBA(222, 222, 222, 255))
        self.hbar_color.connect("color_set", self.on_hbar_color_color_set)
        self.pack_end(self.hbar_color)

    def on_hbar_help_clicked(self, widget):
        webbrowser.open_new_tab("https://github.com/mirkobrombin/ElementaryPython")

    def on_hbar_color_color_set(self, widget):
        cn.Colors.primary_color = widget.get_rgba().to_string()

        # There are better methods to define CSS variables, but this is an example.
        stylesheet = """
            @define-color colorPrimary """+cn.Colors.primary_color+""";
            @define-color textColorPrimary """+cn.Colors.primary_text_color+""";
            @define-color textColorPrimaryShadow """+cn.Colors.primary_text_shadow_color+""";
        """

        style_provider = Gtk.CssProvider()
        style_provider.load_from_data(bytes(stylesheet.encode()))
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(), style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
