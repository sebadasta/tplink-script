This is based on the tplink-wr-api done by n1k0r0.

https://github.com/n1k0r/tplink-wr-api


I have modified the code to be able to update the Channel value whileusing the Router as a repeater. 

# TPLINK-API

Python API to some budget TP-Link routers.

## Supported devices

This library designed for budget models with firmware without API. Library interacts with router management interface like user (scrape HTML UI) so it may not work with others versions of firmware.

Tested with TL-WR841N with firmware version 3.16.9.

## Features

Sam as found in tplink-wr-api and have added the abiity to read the "Survey" page and get the channel for the desired SSID, then the script will compare that channel to the one set in the repater.

If the channel values don't match the scrit will set the Repeater's channel to the same value that the selected SSID (The SSID that we want to repeat).

