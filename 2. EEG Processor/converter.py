# Convert E-Prime output files to more manageable formats (.csv)

import os
from os import remove
from os.path import join

import pandas as pd
from convert_eprime.utils import remove_unicode
from data.utils import get_input_eprime_path, get_output_eprime_path
from convert import text_to_csv

# Locate the eprime txt data folder
in_directory = get_input_eprime_path()
out_directory = get_output_eprime_path()

for filename in os.listdir(in_directory):
    if filename.endswith("txt"):
        in_file = join(in_directory,filename)
        out_file = join(out_directory, filename[:-4]+".csv")

        with open(in_file, encoding = "latin1") as fo:
            raw_data = fo.readlines()[:20]
            raw_data = [l.rstrip() for l in raw_data]
        
        # Remove unicode characters.
        filtered_data = [remove_unicode(row) for row in raw_data]
        
        print('The raw text file (after removing unicode characters):')
        for l in filtered_data:
            print(l)
        print('')
        
        text_to_csv(in_file, out_file)
        print('')
        
        df = pd.read_csv(out_file)
        print('The converted csv file:')
        print(df.head(10))
        
