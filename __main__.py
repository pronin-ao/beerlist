import json
import sys
from .read_xls import read_xlsx
from .request_beer import search_beer
from .write_xlsx import write_xlsx

DEFAULT_SETTINGS = {
  "key_column": "C",
  "result": {
    "name": "F",
    "abv": "G",
    "ibu": "H",
    "style": "I",
    "brewery": "J",
    "country": "K"
  }
}

MAX_BREAKS = 3


def main():
    if len(sys.argv) < 2:
        print('Program needs xlsx filename to work')
        return
    if sys.argv[1] in ['?', 'help', '-?']:
        print('arguments: filename [settings_file]')
    filename = sys.argv[1]
    settings = DEFAULT_SETTINGS
    if len(sys.argv) > 2:
        with open(sys.argv[2]) as settings_file:
            settings = json.load(settings_file)

    try:
        beer_list = read_xlsx(
            filename, settings['key_column'], settings['result']
        )
    except Exception as er:
        print('error reading file: ', er)
        return

    print('Scoped {} name of beer'.format(len(beer_list)))

    beer_data = {}
    breaks = 0
    for beer_name in beer_list:
        try:
            beer = search_beer(beer_name)
            if beer is not None:
                beer_data[beer_name] = beer
            else:
                print(beer, ' was not found!')
        except Exception as er:
            print('error processing request: ', er)
            breaks = breaks+1
            if breaks >= MAX_BREAKS:
                break

    try:
        write_xlsx(
            filename, settings['key_column'], settings['result'], beer_data
        )
    except Exception as er:
        print('error writing file: ', er)
        return


if __name__ == '__main__':
    main()
