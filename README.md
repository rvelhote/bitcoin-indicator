[![Code Climate](https://codeclimate.com/github/rvelhote/bitcoin-indicator/badges/gpa.svg)](https://codeclimate.com/github/rvelhote/bitcoin-indicator) [![Test Coverage](https://codeclimate.com/github/rvelhote/bitcoin-indicator/badges/coverage.svg)](https://codeclimate.com/github/rvelhote/bitcoin-indicator/coverage) [![Issue Count](https://codeclimate.com/github/rvelhote/bitcoin-indicator/badges/issue_count.svg)](https://codeclimate.com/github/rvelhote/bitcoin-indicator)

# Bitcoin Indicator

This is a very simple indicator so you can always know the price of a Bitcoin in the Bitstamp exchange. It refreshes every 5 seconds with the latest price. If there is any error with the HTTP request you will see a message warning you about the error and also the last known price (before the error ocurred).

![Screenshot](http://i.imgur.com/q638xP2.png)

## Planned Features
- A up or down signal to tell if the price is going up or down
- Implement some more exchanges
- Configuration screen with some options (e.g. refresh rate, currency)
- Set the indicator to run at startup or not (although it can be done manually)