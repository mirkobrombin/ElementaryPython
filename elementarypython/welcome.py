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
import subprocess
import os
import locale
import gettext
import webbrowser

gi.require_version('Gtk', '3.0')
gi.require_version('Granite', '1.0')

from gi.repository import Gtk, Granite

import constants as cn

class Welcome(Gtk.Box):

    '''Getting system default settings'''
    settings = Gtk.Settings.get_default()

    def __init__(self):
        '''Our class will be a Gtk.Box and will contain our 
        new Welcome Widget.'''
        Gtk.Box.__init__(self, False, 0)

        '''Your app needs translations, right?
        Here we are trying to set the locale_path to the system one, assuming 
        the app is installed.'''
        try:
            current_locale, encoding = locale.getdefaultlocale()
            locale_path = os.path.join(
                os.path.abspath(
                    os.path.dirname(__file__)
                ), 
                'locale'
            )
            translate = gettext.translation(
                cn.App.application_shortname, 
                locale_path, 
                [current_locale] 
            )
            _ = translate.gettext
        except FileNotFoundError:
            _ = str
        ''''The self._ can be used for defining a new translation string.
        Note: that if the translation is not loaded (the check above), 
              self._ will be the same as str, so you won't get any errors.'''
        self._ = _

        '''Here we are creating a new Welcome Widget from the Granite library'''
        welcome = Granite.WidgetsWelcome()
        welcome = welcome.new(
            _("Welcome"), 
            cn.App.application_description
        )

        '''Let's populate the Welcome menu actions.'''
        welcome.append(
            "weather-clear-night", # the action icon (a valid icon name)
            _('Dark Mode'), # the action name
            _('Switch to the dark side') # the action description
        )
        welcome.append(
            "utilities-terminal",
            _('Open Terminal'), 
            _('Just an example of action')
        )
        welcome.append(
            "help-contents", 
            _('Info'), 
            _('Learn more about this application')
        )
        welcome.append(
            "help-browser", 
            _('Doc'), 
            _('Valadoc for Granite')
        )

        '''Here we are connecting the on_welcome_activated method to the 
        activated signal of the Welcome Widget, so this will be triggered 
        when an action is activated'''
        welcome.connect("activated", self.on_welcome_activated)

        '''Do you remember the Box we were talking about at the beginning?
        Here, we add the Welcome Widget to this.'''
        self.add(welcome)

    def on_welcome_activated(self, widget, index):
        '''The activated signal return an index with the activated item, we
        will use this to perform different actions'''

        if index == 0:
            '''Pssst.. Array starts from 0. So this is our first action.
            We are toggling the Dark theme based on the system settings.'''
            theme = self.settings.get_property(
                "gtk-application-prefer-dark-theme"
            )
            self.settings.set_property(
                "gtk-application-prefer-dark-theme", 
                not theme # theme is a bool, we are reversing it
            )
        elif index == 1:
            try:
                subprocess.check_output("io.elementary.terminal")
            except:
                print(self._('Terminal Not Found!'))
        elif index == 2:
            webbrowser.open_new_tab(
                "https://github.com/mirkobrombin/ElementaryPython"
            )
        else:
            webbrowser.open_new_tab(
                "https://valadoc.org/granite/Granite.html"
            )

        '''Printing the Index just for Debug purposes.'''
        print(f"Index: {str(index)}")
