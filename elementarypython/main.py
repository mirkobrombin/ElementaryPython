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

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gio, Gdk

import window as wn
import constants as cn

class Application(Gtk.Application):

    def do_activate(self):
        '''Here we are creating a new instante of the Windows, setting its 
        size and connecting the delete-event signal to correctly handle 
        the application exit.'''
        self.win = wn.Window()
        self.win.set_default_size(600, 600)
        self.win.connect("delete-event", Gtk.main_quit)

        self.win.show_all()

        Gtk.main()


app = Application()

'''Here we are defining the application colors, using the parameters 
defined in the constants file.'''
stylesheet = f"""
    @define-color colorPrimary {cn.Colors.primary_color};
    @define-color textColorPrimary {cn.Colors.primary_text_color};
    @define-color textColorPrimaryShadow {cn.Colors.primary_text_shadow_color};
"""

'''And here we are injecting the style CSS in the application'''
style_provider = Gtk.CssProvider()
style_provider.load_from_data(bytes(stylesheet.encode()))
Gtk.StyleContext.add_provider_for_screen(
    Gdk.Screen.get_default(), style_provider,
    Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
)

'''Defining our application infos'''
app.application_id = cn.App.application_id
app.flags = Gio.ApplicationFlags.FLAGS_NONE
app.program_name = cn.App.application_name
app.build_version = cn.App.application_version
app.about_comments = cn.App.about_comments
app.app_years = cn.App.app_years
app.build_version = cn.App.application_version
app.app_icon = cn.App.application_id
app.main_url = cn.App.main_url
app.bug_url = cn.App.bug_url
app.help_url = cn.App.help_url
app.translate_url = cn.App.translate_url

'''Let's make our app roar!'''
app.run("")
