import numpy as np

TARGET_WORD = "XMAS"
INPUT_PATH = "input.txt"

num_occurances = 0

letter_string = ""
with open(INPUT_PATH, 'r') as file:
    word_string = file.read()

#turns the string into a 2d array of char
letter_arr = np.array([list(line) for line in word_string.split('\n')])

A_indices = np.array(np.where(letter_arr == 'A'))
A_indices = A_indices[:, [col for col in range(A_indices.shape[1]) if np.all(A_indices[:, col] != 0) and A_indices[0,col] != (letter_arr.shape[0]-1) and A_indices[1,col] != (letter_arr.shape[1]-1)]] #ignoring all indices on the boundary

num_occurances = np.array([int(((letter_arr[A_indices[0][index_index]-1][A_indices[1][index_index]-1] == 'M' and letter_arr[A_indices[0][index_index]+1][A_indices[1][index_index]+1] == 'S') or (letter_arr[A_indices[0][index_index]-1][A_indices[1][index_index]-1] == 'S' and letter_arr[A_indices[0][index_index]+1][A_indices[1][index_index]+1] == 'M')) and ((letter_arr[A_indices[0][index_index]-1][A_indices[1][index_index]+1] == 'M' and letter_arr[A_indices[0][index_index]+1][A_indices[1][index_index]-1] == 'S') or (letter_arr[A_indices[0][index_index]-1][A_indices[1][index_index]+1] == 'S' and letter_arr[A_indices[0][index_index]+1][A_indices[1][index_index]-1] == 'M'))) for index_index in range(A_indices.shape[1])]).sum()

print(num_occurances)