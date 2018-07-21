import pandas as pd
from utils import get_test_data_path
import os
from os.path import join

data_dir = get_test_data_path()

zero_csv_file = join(data_dir,"csv_files_zero")

if not os.path.exists(zero_csv_file): 
    os.makedirs(zero_csv_file)

files = join(data_dir,"csv_files")
print (files)
for filename in os.listdir(files):
    if "presentation" in filename:
        
        csv_file = join(files, filename)
       
        df = pd.read_csv(csv_file)
        lst = [0]

        for row in range(len(df["ImageDisplay1.OffsetTime"])):
            try:
                time_difference = df["ImageDisplay1.OffsetTime"][row]-df["ImageDisplay1.OffsetTime"][row-2]
                if time_difference > 7500 or row==0:
                    lst += [row]
                    print (lst)
            except:
                continue
        for i in lst:
            df["ImageDisplay1.OffsetTime"][i:] = df["ImageDisplay1.OffsetTime"][i:]-df["ImageDisplay1.OffsetTime"][i]
        
        
        df.to_csv(join(zero_csv_file,filename[:-4]+"_zero.csv"))
