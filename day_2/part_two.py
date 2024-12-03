import pandas as pd
import numpy as np

CHUNK_SIZE_PARAMETER = 1 
INPUT_PATH = "input.csv"
MAX_LENGTH_CODES = 15

def sequence_is_clean(arr) -> bool:
    return np.all(np.array([i >= 1 and i <= 3 for i in arr]))

def normalize_sequence_sign(arr):
    return -arr if arr[0] < 0 else arr

num_safe_codes = 0
for chunk in pd.read_csv(INPUT_PATH, sep="\s+", header=None, chunksize=CHUNK_SIZE_PARAMETER, names=range(MAX_LENGTH_CODES)):
    original_reactor_data_matrix = chunk.to_numpy()
    original_reactor_data_matrix = [np.array(row[~np.isnan(row)]) for row in original_reactor_data_matrix] #cleaning the data, creating list of np_arrays
    for row in original_reactor_data_matrix:
        no_rem_diff_arr = (np.roll(row, -1) - row)[:-1]
        no_rem_diff_arr = normalize_sequence_sign(no_rem_diff_arr)
        if sequence_is_clean(no_rem_diff_arr):
            num_safe_codes += 1
            continue
        
        for j, col in enumerate(row):
            if j == len(row):
                continue
            remed_diff_arr = np.delete(row, j) #makes a copy
            remed_diff_arr = (np.roll(remed_diff_arr, -1) - remed_diff_arr)[:-1]
            remed_diff_arr = normalize_sequence_sign(remed_diff_arr)
            if sequence_is_clean(remed_diff_arr):
                num_safe_codes += 1
                break
    
print(num_safe_codes)

