import pandas as pd
import numpy as np

CHUNK_SIZE_PARAMETER = 100
INPUT_PATH = "input.csv"
MAX_LENGTH_CODES = 20

num_safe_codes = 0
#line_num = 0
for chunk in pd.read_csv(INPUT_PATH, sep="\s+", header=None, chunksize=CHUNK_SIZE_PARAMETER, names=range(MAX_LENGTH_CODES)):
    original_reactor_data_matrix = chunk.to_numpy()
    original_reactor_data_matrix = [np.array(row[~np.isnan(row)]) for row in original_reactor_data_matrix] #cleaning the data, creating list of np_arrays
    rolled_reactor_data_matrix = [np.roll(row, -1) for row in original_reactor_data_matrix] #creating the rolled array
    diff_reactor_data_matrix = [rolled_reactor_data_matrix[i]-original_reactor_data_matrix[i] for i in range(len(original_reactor_data_matrix))] #taking the difference row-wise, positive is increasing
    diff_reactor_data_matrix = [row[:-1] for row in diff_reactor_data_matrix] #removes the last datapoint, which is irrelevant, from each row
    diff_reactor_data_matrix = [-row if row[0]<0 else row for row in diff_reactor_data_matrix] #normalizes the sign of each row
    safe_code_bools_array = np.array([int(np.all(np.array([i >= 1 and i <= 3 for i in row]))) for row in diff_reactor_data_matrix]) #checks if the steps are within expectations
    num_safe_codes += safe_code_bools_array.sum()
    #print(str(diff_reactor_data_matrix) + " " + str(line_num))
    #line_num += 1
    
print(num_safe_codes)