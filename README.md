# Hodor - Hold the Door Challenge

## About

This is an advanced project from Holberton School.

In this project the objective is to circunvent the difficulties to automatize a cheat voting script.

The website is http://158.69.76.135/<levelnumber\>.php i.e. http://158.69.76.135/level0.php

## Levels
### Level 0
Vote 1024 times for your Holberton School's id.
Necessary to send a simple post request with the id. No headers nor any argument were required.

### Level 1
Vote 4096 times for your Holberton School's id.
Necessary to send a key with each post request. That key could be obtained by the cookies in the first get request. Also, both requests (get and post) are in the same session. The cookie was given back in the post request.

### Level 2
Vote 1024 times for your Holberton School's id.
Necessary to send all the requests modifying both User-Agent and referer headers.

### Level 3
Vote 1024 times for your Holberton School's id.
Necessary to send the post request with a captcha. The simple captcha can be solved with terresact (an specifically with the Python's module pytesseract). Creating a new VM with the latest Ubuntu and Python versions was required to install pytesseract.

### Level 4
Vote 98 times for your Holberton School's id.
Necessary to send the post request using proxies. Only one vote per person per day is authorized.
The proxies were obtained from https://proxy.webshare.io

### Level 5
Vote 1024 times for your Holberton School's id.
Necessary to send the post request with a hard-to-read captcha. The captcha can be solved with OpenCV and terresact (an specifically with the Python's module pytesseract).
