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
gi.require_version('Granite', '1.0')

from gi.repository import Gtk

import constants as cn
import headerbar as hb
import welcome as wl

class Window(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(
            self, 
            title=cn.App.application_name
        )

        '''Here we are creating a new instance of Headerbar 
        and setting as the titlebar'''
        hbar = hb.Headerbar()
        self.set_titlebar(hbar)

        '''This is a new instance of Welcome, we are 
        simply adding it to the window
        Note: Not all applications need a Welcome Page, make 
        your choice well.'''
        self.welcome = wl.Welcome()
        self.add(self.welcome)
