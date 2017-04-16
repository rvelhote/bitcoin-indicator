[![Code Climate](https://codeclimate.com/github/rvelhote/bitcoin-indicator/badges/gpa.svg)](https://codeclimate.com/github/rvelhote/bitcoin-indicator) [![Test Coverage](https://codeclimate.com/github/rvelhote/bitcoin-indicator/badges/coverage.svg)](https://codeclimate.com/github/rvelhote/bitcoin-indicator/coverage) [![Issue Count](https://codeclimate.com/github/rvelhote/bitcoin-indicator/badges/issue_count.svg)](https://codeclimate.com/github/rvelhote/bitcoin-indicator)

# Bitcoin Indicator

This is a very simple indicator so you can always know the price of a Bitcoin in the Bitstamp exchange. It refreshes every 5 seconds with the latest price. If there is any error with the HTTP request you will see a message warning you about the error and also the last known price (before the error ocurred).

![Screenshot](http://i.imgur.com/q638xP2.png)

# Build
Just run `bash makedeb` to generate the `deb` package. You will have to install the `cmake` package and its dependencies in case you don't have any build tools available. If you don't want to install this indicator in your system you may just as well clone this repository or download it as a zip file and just run `python3 indicator-bitcoin` or `./indicator-bitcoin`.

# Installing
Assuming you generated the `.deb` or obtained it from the releases section of Github, you can now install it with the following command: `sudo dpkg -i indicator-bitcoin-1.0.0-noarch.deb` (the version number might differ).

## Planned Features
- A up or down signal to tell if the price is going up or down
- Implement Ripple (XRP) and perhaps other currencies
- Configuration screen with some options (e.g. refresh rate, currency)
- Refactor exchanges into currencies and the indicator's name to indicator-cryptocurrency instead of being specific to Bitcoin

## Icons
The super cool SVG icons used in this indicator are from artist Martin Allien and you can find them in his (Github project page)[https://github.com/allienworks/cryptocoins]. I made only a slight modification to the colors so they can match the Ambience theme.