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
import unittest
import exchange
import interface


def make_indicator(self):
    """Reusable indicator instance for testing purposes"""
    name = "Bitcoin Indicator"
    icon_path = os.path.abspath("bitcoin.png")

    return interface.Indicator(name, icon_path, None)


class QueryLoopTest(unittest.TestCase):
    def test_valid_request(self):
        """Make sure that the indicator label is presenting the correct message to the user when all is good"""
        indicator = make_indicator(self)
        xchange = exchange.Bitstamp("eur")

        interface.QueryLoop(indicator, xchange).start()

        self.assertNotIn("Error", indicator.get_label())

    def test_invalid_request(self):
        """Make sure that the indicator displays an error message when there is an error"""
        indicator = make_indicator(self)
        xchange = exchange.Bitstamp("inv")

        interface.QueryLoop(indicator, xchange).start()
        self.assertIn("Error", indicator.get_label())
