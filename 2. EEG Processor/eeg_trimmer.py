# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 17:56:01 2018

@author: wanzh
"""
from pandas import DataFrame, read_csv
import pandas as pd
import os
from os.path import join
from data.utils import get_input_electrode_path, get_input_event_path, get_output_eeg_path

# Event File Location
event_Location = get_input_event_path()

# List of Event Files
event_files = os.listdir(event_Location)

# Electrode File Location
electrodes_Location = get_input_electrode_path()    #edit

# List of Electrode Files
electrode_files = os.listdir(electrodes_Location)

#%%

def process_eeg_data(event_data, electrode_data, file_code, num_classes=54, frames=749):
    
    # Make event file (.csv) into Panda Dataframe
    df_event = pd.read_csv(event_data)
    
    # Make electrode file (.csv) into Panda DataFrame
    df_electrodes = pd.read_csv(electrode_data)
    
    # Filter out weird types
    latency_list = df_event[(df_event.type != 255)]['latency'] # type = 255 is a known error type
    
    # Initialize output dataframe
    out = pd.DataFrame(columns=df_electrodes.columns)
    
    for i in latency_list:
        x = pd.DataFrame(df_electrodes[i:i+frames])
        out = out.append(x, ignore_index=True)      
        
    out_location = get_output_eeg_path()
    out_file_name = join(out_location,'{}processed.csv'.format(file_code))
    out.to_csv(out_file_name, sep=',')    #edit
    print("Saved under {}".format(out_file_name))
#%%

for i in range(len(event_files)):
    file_code = event_files[i][:6]
    event_data = join(event_Location, file_code + 'eventraw.csv')
    electrode_data = join(electrodes_Location, file_code + 'raw.csv')
    print("Processing {}".format(file_code))
    process_eeg_data(event_data, electrode_data, file_code)
    
    