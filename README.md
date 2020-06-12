# BeerList Searching
BeerList Searching found info about a list of beer at one time using Untappd

Module request_beer processes request to Untappd APIv4 for provide data.
It searches beer by the name and taking first of result list 
without any specified sorting.
It requires environment variables UNTAPPD_CLIENT_ID and 
UNTAPPD_CLIENT_SECRET to be set with valid key and id.
It's private, so it can't be stored in repository.

Modules read_xls and write_xls processed reading and writing to *xlsx file.
User should specify column with beer name and columns to store result same as in 
'settings.json'. If settings not specified DEFAULT_SETTINGS from main will be used.

Main read list of beer name from file, request every of it and append new
info to the same file as it was read from.

Example of using:
`py3 -m beerlist ~/Downloads/short_one.xlsx`

DEBUG flags is used for debug program and provides more output.