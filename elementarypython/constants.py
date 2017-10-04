#!/usr/bin/python3
'''
   Copyright 2017 Mirko Brombin (brombinmirko@gmail.com)

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
from gi.repository import Gtk

class App:
    application_id = "com.github.mirkobrombin.elementarypython"
    application_name = "Python Template"
    application_description = "This is just a python template"
    application_version ="1.0"
    main_url = "https://github.com/mirkobrombin/elementarypython"
    bug_url = "https://github.com/mirkobrombin/elementarypython/issues/labels/bug"
    help_url = "https://github.com/mirkobrombin/ElementaryPython/issues"
    about_authors = {"Mirko Brombin <brombinmirko@gmail.com>"}
    about_comments = application_description
    about_license_type = Gtk.License.GPL_3_0

class Colors:
    primary_color = "#ac7339"
    primary_text_color = "#f9f2ec"
    primary_text_shadow_color = "#4d3319"
