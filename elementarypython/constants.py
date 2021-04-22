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
import os
import locale
import gettext

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

'''We already talked about translations'''
try:
    current_locale, encoding = locale.getdefaultlocale()
    locale_path = os.path.join(
        os.path.abspath(
            os.path.dirname(__file__)
        ), 
        'locale'
    )
    translate = gettext.translation(
        "elementarypython", 
        locale_path, 
        [current_locale] 
    )
    _ = translate.gettext
except FileNotFoundError:
    _ = str

class App:
    '''Here we are defining our Application infos, so we can easily
    use in all our application files'''
    application_shortname = "elementarypython"
    application_id = "com.github.mirkobrombin.elementarypython"
    application_name = "Elementary Python"
    application_description = _('This is just a python template')
    application_version ="1.1"
    app_years = "2017-2018"
    main_url = "https://git.mirko.pm/brombinmirko/ElementaryPython"
    bug_url = "https://git.mirko.pm/brombinmirko/ElementaryPython/issues/labels/bug"
    help_url = "https://git.mirko.pm/brombinmirko/ElementaryPython/issues"
    translate_url = "https://git.mirko.pm/brombinmirko/ElementaryPython/blob/master/CONTRIBUTING.md"
    about_comments = application_description
    about_license_type = Gtk.License.GPL_3_0

class Colors:
    primary_color = "rgba(100, 85, 82, 1)"
    primary_text_color = "#EEEDEC"
    primary_text_shadow_color = "#53433F"
