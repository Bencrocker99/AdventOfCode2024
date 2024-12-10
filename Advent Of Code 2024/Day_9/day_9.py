from dataclasses import dataclass
from pathlib import Path

@dataclass
class File:
    id: int
    starting_index: int
    length: int

@dataclass
class EmptySpace:
    starting_index: int
    length: int

def get_day_9_solutions(file: str) -> tuple[int, int]:
    empty_spaces, files = [], []
    current_index = 0
    for i in range(len(file)):
        if i % 2 == 0:
            files.append(File(i / 2, current_index, int(file[i])))
        else:
            empty_spaces.append(EmptySpace(current_index, int(file[i])))
        current_index += int(file[i])
    return get_checksum_of_files(files.copy(), empty_spaces.copy()), get_checksum_of_files_with_new_method(files.copy(), empty_spaces.copy())

def get_checksum_of_files(files: list[File], empty_spaces: list[EmptySpace]) -> int:
    checksum = 0
    current_id = 0
    next_position_is_empty_space = False
    while len(files) > 0:
        if next_position_is_empty_space and len(empty_spaces) > 0:
            for i in range(empty_spaces[0].length):
                last_file: File = files[len(files) - 1]
                checksum += current_id * last_file.id
                current_id += 1
                last_file.length = last_file.length - 1
                if last_file.length == 0:
                    files.remove(last_file)
                    if len(files) == 0:
                        break
            del empty_spaces[0]
            next_position_is_empty_space = False
        else:
            for i in range(files[0].length):
                checksum += current_id * files[0].id
                current_id += 1
            del files[0]
            next_position_is_empty_space = True
    return checksum

def get_checksum_of_files_with_new_method(files: list[File], empty_spaces: list[EmptySpace]):
    checksum = 0
    for i in range(len(files)):
        file = files[len(files) - i - 1]
        found_space = False
        for j in range(len(empty_spaces)):
            if empty_spaces[j].starting_index > file.starting_index:
                break
            if file.length <= empty_spaces[j].length:
                empty_spaces[j].length -= file.length
                for k in range(file.length):
                    checksum += (empty_spaces[j].starting_index + k) * file.id
                empty_spaces[j].starting_index += file.length
                found_space = True
                if empty_spaces[j].length == 0:
                    del empty_spaces[j]
                break
        if not found_space:
            for j in range(file.length):
                checksum += (file.starting_index + j) * file.id
    return checksum

if __name__ == "__main__":
    file = Path("Advent Of Code 2024/Day_9/input.txt").read_text()
    solution_1, solution_2 = get_day_9_solutions(file)
    print(f"Checksum: {solution_1}")
    print(f"Checksum with New Method: {solution_2}")