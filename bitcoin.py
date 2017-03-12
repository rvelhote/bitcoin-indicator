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
import signal
import requests

gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')

from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import GLib as glib


class Bitstamp():
    """Bitstamp implements the Bitstamp v2 API"""
    url = {
        "btceur": "https://www.bitstamp.net/api/v2/ticker/btceur"
    }

    def __init__(self, currency):
        self.currency = currency

    def query(self):
        response = requests.request("GET", self.url[self.currency])
        return response.json()


class QueryLoop():
    def __init__(self, indicator, exchange):
        self.indicator = indicator
        self.exchange = exchange

    def loop(self):
        result = self.exchange.query()
        indicator.set_label("{} EUR".format(result["last"]), '')
        glib.timeout_add_seconds(5, self.loop)

    def start(self):
        self.loop()


if __name__ == "__main__":
    menu = gtk.Menu()
    item = gtk.MenuItem("item")

    menu.append(item)

    indicator = appindicator.Indicator.new("Bitcoin Indicator", os.path.abspath("bitcoin.png"),
                                           appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(menu)

    exchange = Bitstamp("btceur")

    loop = QueryLoop(indicator, exchange)
    loop.start()

    signal.signal(signal.SIGINT, signal.SIG_DFL)
    gtk.main()
