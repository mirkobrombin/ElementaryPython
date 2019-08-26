#!/usr/bin/python3

import glob, os 
from distutils.core import setup

install_data = [('share/applications', ['data/com.github.mirkobrombin.elementarypython.desktop']),
                ('share/metainfo', ['data/com.github.mirkobrombin.elementarypython.appdata.xml']),
                ('share/icons/hicolor/128x128/apps',['data/com.github.mirkobrombin.elementarypython.svg']),
                ('bin/elementarypython',['elementarypython/constants.py']),
                ('bin/elementarypython',['elementarypython/headerbar.py']),
                ('bin/elementarypython',['elementarypython/main.py']),
                ('bin/elementarypython',['elementarypython/welcome.py']),
                ('bin/elementarypython',['elementarypython/window.py']),
                ('bin/elementarypython',['elementarypython/__init__.py']),
                ('bin/elementarypython/locale/it_IT/LC_MESSAGES',
                    ['elementarypython/locale/it_IT/LC_MESSAGES/elementarypython.mo']),
                ('bin/elementarypython/locale/it_IT/LC_MESSAGES',
                    ['elementarypython/locale/it_IT/LC_MESSAGES/elementarypython.po'])]

setup(  name='Elementary Python',
        version='0.0.1',
        author='Mirko Brombin',
        description='This is just a python template',
        url='https://github.com/mirkobrombin/elementarypython',
        license='GNU GPL3',
        scripts=['com.github.mirkobrombin.elementarypython'],
        packages=['elementarypython'],
        data_files=install_data)
