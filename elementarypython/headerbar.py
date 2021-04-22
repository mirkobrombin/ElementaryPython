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

import gi
import webbrowser

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gdk

import constants as cn

class Headerbar(Gtk.HeaderBar):

    def __init__(self):

        Gtk.HeaderBar.__init__(self)

        '''Here we are setting some parameters for the HeaderBar
        <https://developer.gnome.org/gtk3/stable/GtkHeaderBar.html>'''
        self.set_show_close_button(True)
        self.props.title = cn.App.application_name

        '''Now we want to display some buttons in our HeaderBar. We are
        using ToolButton, a gtk.ToolItem subclass that displays buttons'''
        self.hbar_help = Gtk.ToolButton() # a new instance
        self.hbar_help.set_icon_name( # setting the button icon name
            "help-contents" 
        ) 
        self.hbar_help.connect( # connecting our method to the clicked signal
            "clicked", 
            self.on_hbar_help_clicked
        )
        self.pack_end( # packing the button to the end of the HeaderBar
            self.hbar_help
        )
        
        '''Another button, this can be used for choosing Application colors'''
        self.hbar_color = Gtk.ColorButton.new_with_rgba(
            Gdk.RGBA(222, 222, 222, 255)
        )
        self.hbar_color.connect(
            "color_set", 
            self.on_hbar_color_color_set
        )
        self.pack_end(self.hbar_color)

    '''Each button should perform actions, no?
    We are creating custom methods for each button.'''
    def on_hbar_help_clicked(self, widget):
        webbrowser.open_new_tab(
            "https://github.com/mirkobrombin/ElementaryPython"
        )

    def on_hbar_color_color_set(self, widget):
        cn.Colors.primary_color = widget.get_rgba().to_string()

        stylesheet = f"""
            @define-color colorPrimary {cn.Colors.primary_color};
            @define-color textColorPrimary {cn.Colors.primary_text_color};
            @define-color textColorPrimaryShadow {cn.Colors.primary_text_shadow_color};
        """

        style_provider = Gtk.CssProvider()
        style_provider.load_from_data(bytes(stylesheet.encode()))
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(), 
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
