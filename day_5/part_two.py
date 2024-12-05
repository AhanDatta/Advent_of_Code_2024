import numpy as np

INPUT_PATH = "input.txt"

prerequisites_dict = {}

prerequisites_str, codes_str = ("","")
with open(INPUT_PATH, 'r') as file:
    prerequisites_str, codes_str = file.read().split("\n\n")

#Creates the prerequisites dict, which maps number to set of number
for prereq in prerequisites_str.split('\n'):
    req, num = [int(elem) for elem in prereq.split('|')]
    if not num in prerequisites_dict:
        prerequisites_dict[num] = {req}
    else:
        prerequisites_dict[num].add(req)

#Checking which codes don't work
bad_codes = []
bad_indices_list = []
for code_str in codes_str.split('\n'):
    is_good_code = True
    bad_indices = []
    seen_set = set()
    code = np.array([int(elem) for elem in code_str.split(',')])
    code_set = set(code)
    for i, num in enumerate(code):
        if num in prerequisites_dict.keys() and not (prerequisites_dict[num].intersection(code_set)).issubset(seen_set):
            is_good_code = False
            bad_indices.append(i)
        seen_set.add(num)
    
    if not is_good_code:
        bad_codes.append(code)
        bad_indices_list.append(bad_indices)

#Fixing the codes
fixed_codes =  []
for i, code in enumerate(bad_codes):
    fixed_codes.append([num for j, num in enumerate(code) if not j in bad_indices_list[i]])
    code_set = set(code)
    for bad_index in bad_indices_list[i]:
        bad_num = code[bad_index]
        bad_num_prereq = prerequisites_dict[bad_num].intersection(code_set)
        for j in range(len(fixed_codes[i])-1, -1, -1):
            if fixed_codes[i][j] in bad_num_prereq:
                fixed_codes[i].insert(j+1, bad_num)
                break

print(np.array([code[int((len(code)-1)/2)] for code in fixed_codes]).sum())