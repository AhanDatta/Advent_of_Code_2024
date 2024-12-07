import numpy as np
import itertools

INPUT_PATH = "input.txt"

test_values_arr = []
codes_arr = []
with open(INPUT_PATH, 'r') as file:
    for line in file:
        test_val = int(line.split(':')[0])
        code = line.split(':')[1].split(' ')[1:] #stripping the first whitespace
        code[-1] = code[-1].replace("\n","") #stripping the \n from the last elem
        code = [int(elem) for elem in code]
        test_values_arr.append(test_val)
        codes_arr.append(code)

good_indices_and_orderings = {}
for i in range(len(test_values_arr)):
    test_val = test_values_arr[i]
    code = codes_arr[i]
    
    Z2n_elements = list(itertools.product([0,1], repeat=len(code)-1)) #creates all elements of the set (Z/2Z)^n for n = len(code)-1

    for op_ordering in Z2n_elements:
        operator_total = code[0]
        for j in range(len(code)-1):
            if op_ordering[j] == 0:
                operator_total += code[j+1]
            elif op_ordering[j] == 1:
                operator_total *= code[j+1]

            if operator_total > test_val:
                break

        if test_val == operator_total:
            good_indices_and_orderings[i] = op_ordering
            break

print([(i, good_indices_and_orderings[i]) for i in good_indices_and_orderings])
print(np.sum(np.array([test_values_arr[i] for i in good_indices_and_orderings]), dtype=np.uint64))