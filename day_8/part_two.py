import numpy as np 
from numpy.typing import NDArray
import math

INPUT_PATH = "input.txt"

def read_file_to_map(filepath: str) -> NDArray:
    file_str = ""    
    with open(filepath, 'r') as file:
        file_str = file.read()

    return np.array([list(line) for line in file_str.split('\n')])

def create_signal_bitmap_dict(map: NDArray) -> dict[str, NDArray]:
    ret_dict = {}
    unique_nontrivial_char_arr = np.array(list(set(np.unique(map)) - {'.'}))
    for unique_char in unique_nontrivial_char_arr:
        ret_dict[unique_char] = np.full(np.shape(map), False, dtype=bool)

    for char, bitmap in ret_dict.items():
        char_occ_indices = np.where(map == char)
        char_occ_rows, char_occ_cols = char_occ_indices
        bitmap[char_occ_rows, char_occ_cols] = True

    return ret_dict

def create_antinode_bitmap_dict(signal_bitmap_dict: dict[str, NDArray]) -> dict[str, NDArray]:
    ret_dict = {}
    for key in signal_bitmap_dict:
        ret_dict[key] = np.full(np.shape(signal_bitmap_dict[key]), False, dtype=bool)

    for char in signal_bitmap_dict:
        signal_exist_coords = np.where(signal_bitmap_dict[char] == True)
        signal_exist_coords = np.array([(signal_exist_coords[0][i], signal_exist_coords[1][i]) for i in range(len(signal_exist_coords[0]))])
        signal_exist_coords_cart_prod = compute_cart_product(signal_exist_coords)
        for coord_pair in signal_exist_coords_cart_prod:
            coord_1, coord_2 = coord_pair
            if (coord_1 == coord_2).all():
                continue
            delta_coord = coord_1 - coord_2
            gcd = math.gcd(delta_coord[0], delta_coord[1])
            delta_coord = np.array(list((delta_coord[0] // gcd, delta_coord[1] // gcd)))
            k = 0
            while True:
                try:
                    new_coord = coord_1 + k * delta_coord
                    if (new_coord < 0).any():
                        raise IndexError
                    
                    ret_dict[char][new_coord[0]][new_coord[1]] = True
                    k += 1
                except IndexError:
                    break

    return ret_dict

def compute_cart_product(arr: NDArray) -> NDArray:
    ret_arr = []
    for val_1 in arr:
        for val_2 in arr:
            ret_arr.append((val_1, val_2))

    return np.array(ret_arr)

def create_final_antinode_bitmap(bitmap_dict: dict[str, NDArray]) -> NDArray:
    ored_bitmap = np.full(np.shape(bitmap_dict[list(bitmap_dict.keys())[0]]), False, dtype=bool)
    for key, bitmap in bitmap_dict.items():
        ored_bitmap = np.bitwise_or(ored_bitmap, bitmap)

    return ored_bitmap


if __name__ == "__main__":
    original_map = read_file_to_map(INPUT_PATH)
    signal_bitmap_dict = create_signal_bitmap_dict(original_map)
    antinode_bitmap_dict = create_antinode_bitmap_dict(signal_bitmap_dict)
    ored_bitmap = create_final_antinode_bitmap(antinode_bitmap_dict)
    print(np.sum(ored_bitmap == True))