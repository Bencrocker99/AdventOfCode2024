from pathlib import Path
import re


def get_day_3_solutions(file: str) -> tuple[int, int]:
    file_using_conditionals: str = re.sub("don't\(\)(\n|.)+?do\(\)", "", file)
    return get_result_of_multiply_instructions(file), get_result_of_multiply_instructions(file_using_conditionals)

def get_result_of_multiply_instructions(file: str) -> int:
    multiply_instructions: str = "".join(re.findall("mul\(\d*,\d*\)", file))
    numbers_to_multiply: list[int] = [int(x) for x in re.findall("\d+",multiply_instructions)]
    return sum(list(map(lambda x, y: x * y, numbers_to_multiply[::2], numbers_to_multiply[1::2])))


if __name__ == "__main__":
    file = Path("Advent Of Code 2024/Day_3/input.txt").read_text()
    solution_1, solution_2 = get_day_3_solutions(file)
    print(f"Total of Multiplications: {solution_1}")
    print(f"Total of Multiplications Using Conditionals: {solution_2}")