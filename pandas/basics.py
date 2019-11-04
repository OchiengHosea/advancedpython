import csv
from pathlib import Path
import datetime

data_path = Path('pandas/amazon.csv')

def clean_row(source_row):
    source_row['state'] = source_row['state']
    source_row['month'] = source_row['month']
    source_row['year'] = int(source_row['year'])
    source_row['number'] = float(source_row['number'])
    source_row['date'] = datetime.datetime.strptime(source_row['date'], '%Y-%m-%d').date()
    return source_row
    

def cleanse(reader):
    for row in reader:
        yield clean_row(row)

with data_path.open() as data_file:
    data_reader = csv.DictReader(data_file)
    clean_data_reader = cleanse(data_reader)
    print(list(clean_data_reader)[:5])