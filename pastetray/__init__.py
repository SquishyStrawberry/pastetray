# Copyright (c) 2016 Akuli

# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""Set up things and provide information about PasteTray."""

import gettext
import locale
import signal

import gi
from gi.repository import GObject
from pkg_resources import resource_stream


def _get_translation():
    """Return a gettext.GNUTranslations instance."""
    lang = locale.getdefaultlocale()[0]
    while True:
        try:
            path = 'locale/{}.mo'.format(lang)
            with resource_stream('pastetray', path) as fp:
                return gettext.GNUTranslations(fp)
        except FileNotFoundError:
            if '_' not in lang:
                # Give up.
                return gettext.NullTranslations()
        # Remove the last whitespace and everything after it, and keep
        # going.
        lang = lang.rpartition('_')[0]


gi.require_version('Gtk', '3.0')
GObject.threads_init()
signal.signal(signal.SIGINT, signal.SIG_DFL)
_ = _get_translation().gettext


# Add your name here if you've helped with making this program but your
# name is not here yet.
AUTHORS = ["Akuli"]
TRANSLATORS = {
    _("Finnish"): "Akuli",
}

# General information.
SHORT_DESC = _("a simple application for using online pastebins")
LONG_DESC = _("This program displays a paste icon in the system tray. "
              "The tray icon can be clicked and new pastes to online "
              "pastebins can be easily made.")
VERSION = '1.0-beta'
KEYWORDS = ["pastebin", "Gtk+3"]
USER_AGENT = "PasteTray/" + VERSION

# The setup.py needs to do other checks too, because not all
# dependencies can be installed with pip.
PIP_DEPENDS = ['appdirs', 'psutil', 'requests']
# This list is more complete.
DEBIAN_DEPENDS = ['gir1.2-gtk-3.0', 'gir1.2-appindicator3-0.1',
                  'python3-gi', 'python3-appdirs', 'python3-psutil',
                  'python3-requests']
