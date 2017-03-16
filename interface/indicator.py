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
import os

gi.require_version('AppIndicator3', '0.1')

from gi.repository import AppIndicator3 as appindicator


class Indicator():
    def __init__(self, name, icon_path, menu=None):
        """
        Creates a new indicator for the application! The best indicator Jerry. The best.

        :param name: The name to give the indicator
        :param icon_path: A path for the icon that will identify the indicator
        :param menu: An instance of interface.Menu with the list of menu items that belong to this indicator
        """
        self.name = name
        self.icon = os.path.abspath(icon_path)
        self.category = appindicator.IndicatorCategory.SYSTEM_SERVICES

        self.indicator = appindicator.Indicator.new(self.name, self.icon, self.category)
        self.indicator.set_status(appindicator.IndicatorStatus.ACTIVE)

        if menu is not None:
            self.indicator.set_menu(menu)

    def set_label(self, value):
        """
        Defines a label for the indicator. This is merely a wrapper for the indicator set_label method.

        :param value: A string containing a new label for the indicator
        :return: None
        """
        self.indicator.set_label(value, '')

    def get_label(self):
        """
        Obtain the label currently assigned to this indicator instance
        :return: A string containing the current indicator label
        """
        return self.indicator.get_label()