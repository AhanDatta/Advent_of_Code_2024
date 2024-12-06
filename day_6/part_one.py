from enum import IntEnum
from typing import Tuple

INPUT_PATH = "test_1.txt"

class Direction(IntEnum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

class Guard:
    def __init__(self, pos: Tuple[int, int], dir: Direction):
        self.row = pos[0]
        self.col = pos[1]
        self.dir = dir

    def __str__(self):
        return f"Guard(position = ({self.row},{self.col}), direction = {self.dir})"

    #Returns false if it hits a boundary
    def move_forward(self, map: list[list[str]]) -> bool:
        try:
            idx_row = self.row + int(int(self.dir)%2 == 0) * (1 if self.dir == Direction.SOUTH else -1)
            idx_col = self.col + int(int(self.dir)%2 == 1) * (1 if self.dir == Direction.EAST else -1)
            if idx_row < 0 or idx_col < 0:
                raise IndexError
            object_in_way = True if map[idx_row][idx_col] == '#' else False
        except IndexError:
            return False
        if not object_in_way:
            match self.dir:
                case Direction.NORTH:
                    self.row -= 1
                case Direction.EAST:
                    self.col += 1
                case Direction.SOUTH:
                    self.row += 1
                case Direction.WEST:
                    self.col -= 1
        else:
            self.dir = Direction((int(self.dir)+1)%4) #turning to the right
        return True

def read_file_to_map(map_filepath: str) -> list[list[str]]:
    map_str = ""
    with open(map_filepath, 'r') as file:
        map_str = file.read()
    
    return [list(line) for line in map_str.split('\n')]

def find_start_position(map: list[list[str]]) -> Tuple[int, int]:
    for i, row in enumerate(map):
        for j, val in enumerate(row):
            if val == "^":
                return (i,j)
            
    raise ValueError("Could not find the desired value")

if __name__ == "__main__":
    map = read_file_to_map(INPUT_PATH)
    starting_position = find_start_position(map)
    guard = Guard(starting_position, Direction.NORTH)

    visited_positions = {(guard.row, guard.col)}
    while guard.move_forward(map):
        visited_positions.add((guard.row, guard.col))

    print(len(visited_positions))
