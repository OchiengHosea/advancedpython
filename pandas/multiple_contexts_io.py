# Commonly used when converting a file data from one format to another
# this needs to have two contexts 
# one for reading the file and one for writting
import re
pattern_text = r'\[(?P<date>\d+-\d+-\d+ \d+:\d+:\d+, \d+)\]'