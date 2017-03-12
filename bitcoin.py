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

"""Constant that defines the name of the EURO currency"""
EURO = "eur"


class Bitstamp():
    """Bitstamp implements the Bitstamp v2 API"""
    url = {
        "btceur": "https://www.bitstamp.net/api/v2/ticker/btceur",
        "btcinv": "https://invalid-address.bitstamp.net/api/v2/ticker/btceur",
        "btc404": "https://www.bitstamp.net/api/v2/ticker/btceur-404"
    }

    def __init__(self, currency):
        """Initialize the exchange with the currency that we want to use"""
        self.currency = currency.strip().lower()

    def query(self):
        """Perform a query to the API defined by the Exchange. The result will be a JSON object with all the data."""
        result = None

        try:
            response = requests.request("GET", self.url["btc" + self.currency])

            if response.status_code != 200:
                raise Exception("Request failed with a {} status code".format(response.status_code))

            result = response.json()
        except Exception as e:
            print(str(e))

        return result


class QueryLoop():
    """QueryLoop accepts the indicator to which the result will be written and an exchange to obtain the results from.
    To define an exchange you only need to implement the query method and return the results in a pre-determined
    format so that it will be consistent."""
    def __init__(self, indicator, exchange):
        self.indicator = indicator
        self.exchange = exchange

    def loop(self):
        """Loop calls it-self forever and ever and will consult the exchange for the most current value and update
        the indicator's label content."""
        result = self.exchange.query()

        if result is not None:
            indicator.set_label("{} EUR".format(result["last"]), '')
        else:
            indicator.set_label("Last Known: {} EUR (Error)".format(result["last"]), '')

        glib.timeout_add_seconds(5, self.loop)

    def start(self):
        """Starts the query loop it does not do anything else. It's merely a matter of naming because
        when initializing the loop in the main() point of entry."""
        self.loop()


def quit(self):
    """Quits the application. Usually called when the user chooses the menu item option."""
    gtk.main_quit()

if __name__ == "__main__":
    item = gtk.MenuItem("Quit")
    item.connect("activate", quit)
    item.show()

    menu = gtk.Menu()
    menu.append(item)

    indicator = appindicator.Indicator.new("Bitcoin Indicator",
                                           os.path.abspath("bitcoin.png"),
                                           appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(menu)

    exchange = Bitstamp(EURO)
    QueryLoop(indicator, exchange).start()

    signal.signal(signal.SIGINT, signal.SIG_DFL)
    gtk.main()
