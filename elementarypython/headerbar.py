#!/usr/bin/python3
'''
   Copyright 2017 Mirko Brombin (brombinmirko@gmail.com)

   This file is part of Football.

    Football is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Football is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Football.  If not, see <http://www.gnu.org/licenses/>.
'''

import gi
import webbrowser
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
import constants as cn

class Headerbar(Gtk.HeaderBar):

    def __init__(self):

        Gtk.HeaderBar.__init__(self)

        self.set_show_close_button(True)
        self.props.title = cn.App.application_name

        # settings button
        self.hbar_help = Gtk.ToolButton()
        self.hbar_help.set_icon_name("help-contents")
        self.hbar_help.connect("clicked", self.on_hbar_help_clicked)
        self.pack_end(self.hbar_help)
    
    def on_hbar_help_clicked(self, widget):
        webbrowser.open_new_tab("https://github.com/mirkobrombin/ElementaryPython")
