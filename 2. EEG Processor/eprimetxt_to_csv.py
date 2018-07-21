
# coding: utf-8

# # Convert E-Prime output files to more manageable formats

# In[1]:

import os
from os import remove
from os.path import join

import pandas as pd
from convert_eprime.utils import remove_unicode
from data.utils import get_test_data_path

data_dir = get_test_data_path()
config_dir = get_test_data_path()


# ## Convert a raw E-Prime output text file to csv
# The text files automatically outputted by E-Prime contain all of the information available in the edat file, although the data are in an unusual format that cannot be used directly. The function text_to_csv reads the data from the text file into a pandas DataFrame and writes the DataFrame out to a file without manipulating the data.


# In[2]:


from convert_eprime.convert import text_to_csv

file_directory = join (data_dir,"eprime_files")

for filename in os.listdir(file_directory):
    if filename.endswith("txt"):
        text_file = join(file_directory,filename)
        out_file = join(join(data_dir, "csv_files"), filename[:-4]+".csv")
        




        with open(text_file, encoding = "latin1") as fo:
            raw_data = fo.readlines()[:20]
            raw_data = [l.rstrip() for l in raw_data]
        
        # Remove unicode characters.
        filtered_data = [remove_unicode(row) for row in raw_data]
        
        print('The raw text file (after removing unicode characters):')
        for l in filtered_data:
            print(l)
        print('')
        
        text_to_csv(text_file, out_file)
        print('')
        
        df = pd.read_csv(out_file)
        print('The converted csv file:')
        print(df.head(10))
        
