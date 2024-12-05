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

#Checking which codes work
good_codes = []
for code_str in codes_str.split('\n'):
    is_good_code = True
    seen_set = set()
    code = np.array([int(elem) for elem in code_str.split(',')])
    code_set = set(code)
    for num in code:
        if num in prerequisites_dict.keys() and not (prerequisites_dict[num].intersection(code_set)).issubset(seen_set):
            is_good_code = False
            break
        seen_set.add(num)
    
    if is_good_code:
        good_codes.append(code)

print(np.array([code[int((len(code)-1)/2)] for code in good_codes]).sum())