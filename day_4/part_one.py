import numpy as np

TARGET_WORD = "XMAS"
INPUT_PATH = "input.txt"

num_occurances = 0

#1d array of char to int
def count_occurances(line: np.ndarray, word: str) -> int:
    num_occ = 0
    word_arr = np.array(list(word))
    for i, char in enumerate(line):
        try:
            num_occ += int(np.all(line[i:i+len(word)] == word_arr))
        except:
            break
    return num_occ

with open(INPUT_PATH, 'r') as file:
    word_string = file.read()

#turns the string into a 2d array of char
letter_arr = np.array([list(line) for line in word_string.split('\n')])

num_horizontal = np.sum(np.array([(count_occurances(row, TARGET_WORD)+count_occurances(row, TARGET_WORD[::-1])) for row in letter_arr]))
num_vertical = np.sum(np.array([(count_occurances(letter_arr[:,col], TARGET_WORD)+count_occurances(letter_arr[:,col], TARGET_WORD[::-1])) for col in range(letter_arr.shape[1])]))
num_diagonal = np.sum(np.array([(count_occurances(np.diag(letter_arr, k=i), TARGET_WORD)+count_occurances(np.diag(letter_arr, k=i), TARGET_WORD[::-1])) for i in range(-len(letter_arr),len(letter_arr))]))
num_off_diagonal = np.sum(np.array([(count_occurances(np.diag(letter_arr[::-1], k=i), TARGET_WORD)+count_occurances(np.diag(letter_arr[::-1], k=i), TARGET_WORD[::-1])) for i in range(-len(letter_arr),len(letter_arr))]))
print(num_diagonal+num_off_diagonal+num_horizontal+num_vertical)