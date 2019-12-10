# Why? 
# When reading a csv using a csv reader each row becomes a simple list of column values
# when using a dict reader each row becomes a dictionsry, by default the contents of the first row becomes the keys for the dictionary.
# We can also provide a list of values that will be used as the keys
# When we use a reader, we must use row[0]

from types import SimpleNamespace
from pathlib import Path
import csv
from datetime import datetime

amazone_data_path = Path('pandas/amazon.csv')

# Create a processing context
parse_date = lambda txt: datetime.strptime(txt, '%Y-%m-%d')

def make_row(source):
    return SimpleNamespace(
        year = int(source['year']),
        state = source['state'],
        month = source['month'],
        number = int(source['number']),
        date = parse_date(source['date'])
    )
with amazone_data_path.open() as amazon_file:
    raw_reader = csv.DictReader(amazon_file)
    # Define a generator that will convert these dictionaries into SimpleNamespaceObjects
    ns_reader = (SimpleNamespace(**row) for row in raw_reader)
    ns_data_reader = (make_row(row) for row in raw_reader)
    print(next(ns_data_reader))