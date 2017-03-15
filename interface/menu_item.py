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

from gi.repository import Gtk as gtk


class MenuItemQuit(gtk.MenuItem):
    """Extends the gtk.MenuItem class with our own implementation. This menu item just quits the application."""
    def __init__(self, name, visible=True):
        """
        Create an instance of MenuItemQuit to be set in the indicator.

        :param name: The name of this menu item.
        :param visible: Set it visible or not on instantiation
        """
        gtk.MenuItem.__init__(self, name)

        self.connect("activate", self.quit)

        if visible:
            self.show()

    @staticmethod
    def quit(item):
        """
        Quits the application. Usually called when the user chooses the menu item option.

        :param item: This should be an instance of the object where this was triggered from (MenuItemQuit)
        :return: None
        """
        logging.debug("Executing action for " + item.get_label())
        gtk.main_quit()
