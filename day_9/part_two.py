import numpy as np
from numpy.typing import NDArray
from copy import deepcopy

INPUT_PATH = "input.txt"

def read_disk_map(filepath: str) -> str:
    disk_map = ""
    with open(filepath, 'r') as file:
        disk_map = file.read()
    return disk_map

#returns fileblock_map array to tuple
#1st index is id (-1 means free), second index is length
def create_raw_fileblock_map(map: str) -> NDArray:
    ret_arr = []
    for i, val in enumerate(map):
        ret_arr.append(((i // 2)*int(i%2 == 0) - int(i%2 != 0), int(val)))
    return np.array(ret_arr, dtype=np.int64)

def fileblock_map_to_arr(map: NDArray) -> NDArray:
    ret_arr = np.array([])
    for val in map:
        ret_arr = np.append(ret_arr, [val[0] for _ in range(val[1])])

    return ret_arr

def compress_fileblock_map(arr: NDArray) -> NDArray:
    ret_arr = deepcopy(arr)
    max_id = arr[-1][0]
    for id in range(max_id, -1, -1):
        id_index = np.where(np.array([val[0] for val in ret_arr]) == id)[0][0]
        file_with_id_index = ret_arr[id_index]
        for j in range(id_index):
            if ret_arr[j][0] == -1:
                if ret_arr[j][1] >= file_with_id_index[1]:
                    ret_arr[j][1] -= file_with_id_index[1]
                    ret_arr = np.insert(ret_arr, j, file_with_id_index, axis=0)
                    ret_arr[np.where(np.array([val[0] for val in ret_arr]) == id)[0][1]][0] = -1
                    ret_arr = np.array([val for val in ret_arr if val[1] != 0])
                    #print(fileblock_map_to_arr(ret_arr))
                    break

    return ret_arr

def compute_checksum(arr: NDArray) -> int:
    fileblock_arr = fileblock_map_to_arr(arr)
    return np.array([i*j for i, j in enumerate(fileblock_arr) if j != -1], dtype=np.uint64).sum()

if __name__ == "__main__":
    disk_map = read_disk_map(INPUT_PATH)
    fileblock_arr = create_raw_fileblock_map(disk_map)
    compressed_fileblock_arr = compress_fileblock_map(fileblock_arr)
    #print(compressed_fileblock_arr)
    print(compute_checksum(compressed_fileblock_arr))