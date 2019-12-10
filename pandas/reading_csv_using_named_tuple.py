from collections import namedtuple
from pathlib import Path
import csv
from datetime import datetime

# Reading a Csv using named tuple

# Define named tuple that matches the actual data., give it a name
Amazon_Data = namedtuple('Amazon_Data', ['year', 'state', 'month', 'number', 'date'])
file_path = Path('pandas/amazon.csv')
parse_date = lambda txt: datetime.strptime(txt, '%Y-%m-%d').date()
def convert_data(amazon_data):
    return Amazon_Data(
        year = int(amazon_data.year),
        state = amazon_data.state,
        month = amazon_data.month,
        number = int(amazon_data.number),
        date = parse_date(amazon_data.date)
    )

with file_path.open() as amazon_file:
    raw_reader = csv.reader(amazon_file)
    data_only = filter(lambda row: row[0] != 'year', raw_reader)
    amazon_reader = (Amazon_Data(*row) for row in data_only)
    amazon_data_reader = (convert_data(ad) for ad in amazon_reader)
    print(next(amazon_data_reader))
    #  for row in amazon_reader:
    #      print(row.state, row.month, row.year, row.number)
        #  0792565176 juiliet