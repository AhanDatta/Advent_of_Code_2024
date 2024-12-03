import re

INPUT_PATH = "input.txt"


content = ''
full_sum = 0
with open(INPUT_PATH, 'r') as file:
    for line in file:
        content += line.rstrip('\n')

special_indices = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', content)

for match in special_indices:
    print(f"Full match: mul({match[0]},{match[1]})")
    full_sum += int(match[0]) * int(match[1])

print(full_sum)