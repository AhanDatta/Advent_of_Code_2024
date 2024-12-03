import re
import numpy as np

INPUT_PATH = "input.txt"

content = ''
full_sum = 0
with open(INPUT_PATH, 'r') as file:
    for line in file:
        content += line.rstrip('\n')

disabled_mask = np.ones(len(content), dtype=bool)
enable_indices = [match.start() for match in re.finditer(r'do\(\)', content)]
disable_indices = [match.start() for match in re.finditer(r'don\'t\(\)', content)]
enable_flag = True
for i in range(len(content)):
    if (i in enable_indices):
        enable_flag = True
    elif (i in disable_indices):
        enable_flag = False
    disabled_mask[i] = not enable_flag

for match in re.finditer(r'mul\((\d{1,3}),(\d{1,3})\)', content):
    full_sum += int(match.group(1)) * int(match.group(2)) * int(not disabled_mask[match.start()])

print(full_sum)