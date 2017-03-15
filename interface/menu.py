# MIT License
#
# Copyright (c) 2017 Ricardo Velhote
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import gi
import logging

gi.require_version('Gtk', '3.0')
logging.basicConfig(level=logging.WARNING)

from gi.repository import Gtk as gtk


class Menu(gtk.Menu):
    """Extends the gtk.Menu class with our own implementation just to separate things in our app."""
    def __init__(self, menu_items):
        """
        Creates a menu instance with a bunch of menu items.
        :param menu_items: A list of interface.menu_item objects that will compose the menu of the indicator
        """
        super().__init__()

        if len(menu_items) == 0:
            logging.warning("Watch out! You have not specified any menu items!")

        for item in menu_items:
            self.append(item)
