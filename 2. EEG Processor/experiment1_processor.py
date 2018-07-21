import os
import pandas as pd
import numpy as np
from os.path import join
from data.utils import get_input_exp_path, get_input_merged_path, get_output_final_path

# EEG Files Directory
eeg_files = get_input_merged_path()

# EXP Files Directory
exp_files = get_input_exp_path()

# Output Folder
out_folder = get_output_final_path()

# Generates a placeholder Dataframe based on the number of classes
def image_number_list(f_in, temp=True):
    
    # Read EXP Data file
    df = pd.read_csv(f_in)
    
    # Initialize Variables
    count = 0
    num_list = []
    label_list = []
    dic = {}
    
    for i,cell in enumerate(df['Procedure']):
        if cell == 'ImageDisplayProc':
            count += 1
            num_list.append(count)
        if cell == 'ClassDisplayProc':
            count = 0
            for x in range(50):
                label_list.append(df['code'][i])
#    dic['Image Number'] = num_list
    dic['Label'] = label_list
#    dic['Duration'] = duration_list
    df_out = pd.DataFrame(dic)
#    print(df_out)
    df_out.to_csv('temp.csv', index=True, index_label = 'Index')
    
    return df_out

# Reshapes and Flatten EEG Data to 749*66
def reshape_eeg(eeg_csv, frames=749, features=66):
    
    # Read csv as DataFrame
    df_eeg = pd.read_csv(eeg_csv)
    
    # Filter out F1 - VEO Feature Columns
    df_eeg = df_eeg[df_eeg.columns[3:69]]
    
    # Output features as numpy array
    out = np.array(df_eeg)
    
    # Resize np array to 2D
    out = out.reshape(-1,frames*features)
    print(out.shape)
    
    return out

# Combine Features and Labels
def combine(eeg_csv, exp_csv, temp=True, frames=749, features=66):
    
    # Create a temporary DataFrame with a feature Column
    df_temp = image_number_list(exp_csv, temp)
    
    # labels np array
    label_list = np.array(df_temp)
    
    # features np array
    feature_list = reshape_eeg(eeg_csv)
    
    # Check shapes
#    print(feature_list)
#    print(feature_list.shape)
#    print(label_list)
#    print(label_list.shape)

    # Combines features and labels using concatenate
    combined = np.concatenate((label_list,feature_list), axis=1)

#    print(comb)
    
    # Save the 2D numpy array
    out_csv = eeg_csv[-13:-11] + '_combined.csv'
    np.savetxt(join(out_folder, out_csv), combined, delimiter=',')

# Get list of files to process (only if file name has S inside)
exp_file_list = [a for a in os.listdir(exp_files) if 'S' in a and '.csv' in a]
eeg_file_list = [a for a in os.listdir(eeg_files) if 'S' in a and '.csv' in a]

print(exp_file_list)
print(eeg_file_list)

for i in range(5,7):
    eeg = join(eeg_files, eeg_file_list[i])
    exp = join(exp_files, exp_file_list[i])
    print("Combining {} and {}...".format(eeg_file_list[i],exp_file_list[i])
    combine(eeg, exp)

    
    
    
    
    
    
    
    
    
    
    