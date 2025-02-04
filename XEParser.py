import requests
import datetime
from bs4 import BeautifulSoup
from dataclasses import dataclass
from typing import Dict

@dataclass
class ExchangeRates:
    dictionary: Dict[str, float]

    def __post_init__(self):
        # Dynamically add attributes for each key-value pair
        for key, value in self.dictionary.items():
            setattr(self, key, value)

    def json(self):
        return self.dictionary


class XEParser:
    def __init__(self, currency: str, date):
        self._date = datetime.datetime.strptime(date, "%Y-%m-%d")
        self._currency = currency
        self._base_url = 'https://www.xe.com/currencytables'
    
    def parse(self):
        self._make_request(self._date)
        self._parse_response()

        return ExchangeRates(self._rows_to_var()) 

    def _make_request(self, date):
        # make request
        url = self._base_url + f"/?from={self._currency}&date={date.strftime("%Y-%m-%d")}"
        self._response = requests.get(url)
    
    def _parse_response(self):
        # initialize parser
        soup = BeautifulSoup(self._response.content, 'html.parser')

        # find table
        table = soup.find('table')
        if not table: raise Exception('Table is not found')

        # obtain rows
        rows = table.find_all('tr')
        if not rows: raise Exception('Row is not found')
        del rows[0] # Remove the header row

        self._rows = rows

    def _rows_to_var(self):
        # parse rows to var
        output = {}

        for row in self._rows:
            headers = row.find_all('th')
            columns = row.find_all('td')

            header_text = [head.get_text() for head in headers]
            column_text = [col.get_text() for col in columns]

            table = {
                'full_name': column_text[0],
                'forward_rate': column_text[1],
                'reverse_rate': column_text[2],
            }

            output[header_text[0]] = table
        
        return output
