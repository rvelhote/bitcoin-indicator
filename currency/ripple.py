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
import requests
import logging
import currency

logger = logging.getLogger('indicator_bitcoin.ripple')


class Ripple(currency.BaseCurrency):
    """Bitstamp implements the Bitstamp v2 API"""
    url = {
        "xrpusd": "https://www.bitstamp.net/api/v2/ticker/xrpusd/",
        "xrpeur": "https://www.bitstamp.net/api/v2/ticker/xrpeur/",
        "xrpbtc": "https://www.bitstamp.net/api/v2/ticker/xrpbtc/",
        "xrpinv": "https://invalid-address.bitstamp.net/api/v2/ticker/xrpeur",
        "xrp404": "https://www.bitstamp.net/api/v2/ticker/xrpeur-404"
    }

    def query(self):
        """Perform a query to the API defined by the Exchange. The result will be a JSON object with all the data."""
        result = None

        try:
            response = requests.get(self.url["xrp" + self.currency], timeout=2)

            if response.status_code != 200:
                raise Exception("Request failed with a {} status code".format(response.status_code))

            result = response.json()
        except Exception as e:
            logging.warning(e)

        logging.debug(result)
        return result
