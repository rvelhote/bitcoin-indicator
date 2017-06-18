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

logger = logging.getLogger('indicator_bitcoin.cryptocurrency')


class CryptoCurrency():
    """CryptoCurrency implements the coinmarketcap.com REST API for a specific cryptocurrency"""
    url = "https://api.coinmarketcap.com/v1/ticker/{}?convert={}"

    def __init__(self, crypto, currency="USD"):
        """
        Initialize the crypto cryptocurrency that we want to track.
        :param crypto: The crypto cryptocurrency ticker that we want to display
        :param fiat The fiat cryptocurrency that we want to convert the value of the crypto to
        :
        """
        self.crypto = crypto.strip().lower()
        self.currency = currency.strip().lower()

    def get_ticker(self):
        """
        Obtain the destination cryptocurrency ticker to display next to the price
        :return: The cryptocurrency ticker (e.g. EUR, USD, BTC)
        """
        return self.currency.strip().upper()

    def query(self):
        """Perform a query to the API defined by the Exchange. The result will be a JSON object with all the data."""
        result = None
        json_response = None

        try:
            response = requests.get(self.url.format(self.crypto, self.currency), timeout=5)

            if response.status_code != 200:
                raise Exception("Request failed with a {} status code".format(response.status_code))

            json_response = response.json()
            result = {
                "last": json_response[0]["price_" + self.currency]
            }

        except Exception as e:
            logger.warning(e)

        logger.debug(json_response)
        return result
