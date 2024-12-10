import numpy as np
from numpy.typing import NDArray

INPUT_PATH = "input.txt"

def read_disk_map(filepath: str) -> str:
    disk_map = ""
    with open(filepath, 'r') as file:
        disk_map = file.read()
    return disk_map

#returns fileblock_map array, where -1 means free space
def create_raw_fileblock_map(map: str) -> NDArray:
    ret_arr = np.array([], dtype=np.int64)
    for i, curr_num in enumerate([int(char) for char in list(map)]):
        if i%2 == 0:
            curr_id = i // 2
            ret_arr = np.append(ret_arr, np.full(curr_num, curr_id, dtype=np.int64))       
        else:
            ret_arr = np.append(ret_arr, np.full(curr_num, -1, dtype=np.int64))

    return ret_arr

def compress_fileblock_map(arr: NDArray) -> NDArray:
    ret_arr = np.array([], dtype=np.int64)
    write_from_arr = np.flip(np.delete(arr, np.where(arr == -1)))
    flipped_arr = np.flip(arr)
    curr_read_id = 1
    j = 0
    k = 0
    curr_write_id = write_from_arr[k]

    while curr_read_id <= curr_write_id:
        curr_val = arr[j]
        if curr_val != -1:
            curr_read_id = curr_val
            ret_arr = np.append(ret_arr, curr_val)
        else:
            ret_arr = np.append(ret_arr, write_from_arr[k])
            k += 1
            curr_write_id = write_from_arr[k]

        j += 1

    num_final_num_arr = np.array([1 if val == ret_arr[-1] else 0 for val in arr]).sum()
    num_final_num_ret_arr = np.array([1 if val == ret_arr[-1] else 0 for val in ret_arr]).sum()
    if num_final_num_arr < num_final_num_ret_arr:
        print(num_final_num_arr)
        print(num_final_num_ret_arr)
        ret_arr = ret_arr[:-(num_final_num_ret_arr - num_final_num_arr)]

    return ret_arr

if __name__ == "__main__":
    disk_map = read_disk_map(INPUT_PATH)
    fileblock_arr = create_raw_fileblock_map(disk_map)
    compressed_fileblock_arr = compress_fileblock_map(fileblock_arr)
    print(compressed_fileblock_arr)
    print(np.array([i * val for i, val in enumerate(compressed_fileblock_arr)], dtype=np.uint64).sum())