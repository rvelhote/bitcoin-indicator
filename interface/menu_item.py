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
import os
import gi
import logging

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk as gtk
from xdg import BaseDirectory as base
from xdg import DesktopEntry as desktop


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


class MenuItemAutostart(gtk.CheckMenuItem):
    """Handles the autostart checkbox option that is a part of the menu"""
    def __init__(self, name, checked=True, visible=True):
        """
        Create an instance of MenuItemAutostart to be set in the indicator. It will allow the user to start the
        indicator on system startup.
        :param name: The name of this menu item.
        :param visible: Set it visible or not on instantiation
        """
        gtk.CheckMenuItem.__init__(self, name)
        self.set_active(checked)

        if visible:
            self.show()

        self.connect("toggled", self.set_autostart)

    @staticmethod
    def get_xdg_file():
        """
        Obtain the desktop entry file with the configuration about this indicator
        :return:
        """
        autostart_dir = base.save_config_path("autostart")
        autostart_file = os.path.join(autostart_dir, "indicator-bitcoin.desktop")

        if not os.path.exists(autostart_file):
            return None, autostart_file

        return desktop.DesktopEntry(autostart_file), autostart_file

    @staticmethod
    def set_autostart(item, data=None):
        """

        :param item:
        :param data:
        :return:
        """
        dfile, path = MenuItemAutostart.get_xdg_file()

        if dfile is None:
            return

        dfile.set("X-GNOME-Autostart-enabled", item.get_active())
        dfile.write(filename=path)

    @staticmethod
    def is_autostart_set():
        """
        Checks if the autostart menu item option should be checked or not
        :return:
        """
        startup = False
        dfile, path = MenuItemAutostart.get_xdg_file()

        if dfile is not None:
            if dfile.get("X-GNOME-Autostart-enabled").upper() == "TRUE":
                startup = True

        return startup
