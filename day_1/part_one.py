import pandas as pd
import numpy as np

INPUT_PATH = "input.csv"

df = pd.read_csv(INPUT_PATH, header=None, names=['a','b'], sep='\s+')
left_arr = np.sort(df['a'].to_numpy())
right_arr = np.sort(df['b'].to_numpy())
print(np.array([np.abs(left_arr[i] - right_arr[i]) for i in range(len(left_arr))]).sum())