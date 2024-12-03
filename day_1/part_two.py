import pandas as pd
import numpy as np

INPUT_PATH = "input.csv"

df = pd.read_csv(INPUT_PATH, header=None, names=['a','b'], sep='\s+')
left_arr = np.sort(df['a'].to_numpy())
right_arr = np.sort(df['b'].to_numpy())
right_dict = {}
for key in right_arr:
    right_dict.setdefault(key,0)
    right_dict[key] += 1
print(np.array([i*right_dict[i] if (i in right_dict) else 0 for i in left_arr]).sum())