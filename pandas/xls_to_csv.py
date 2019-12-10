import os, glob
import csv
import pandas
os.chdir('pandas')
data_files = glob.glob('*.xlsx')
data_frames = [pandas.read_excel(file, skiprows=5, sheet_name=0) for file in data_files]

for df in data_frames:
    for row in df.index:
        print(df['Receipt No.'][row])