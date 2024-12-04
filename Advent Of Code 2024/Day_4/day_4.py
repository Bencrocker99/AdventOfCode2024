from pathlib import Path

number_of_rows: int = 0
number_of_columns: int = 0
directions: list[tuple[int, int]] = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def get_day_4_solutions(file: list[str]) -> tuple[int, int]:
    global number_of_rows
    global number_of_columns
    number_of_rows = len(file)
    number_of_columns = len(file[0])
    xmas_count: int = 0
    x_mas_count: int = 0
    for i in range(number_of_rows):
        for j in range(number_of_columns):
            if file[i][j] == "X":
                xmas_count += check_for_xmas(file, i, j)
            if file[i][j] == "A" and check_for_x_mas(file, i, j):
                x_mas_count += 1
    return xmas_count, x_mas_count

def check_for_xmas(file: list[str], row_number: int, column_number: int) -> int:
    substrings: list[str] = []
    for direction in directions:
        substrings.append(get_4_char_substring(file, row_number, column_number, direction))
    return sum(x == "XMAS" for x in substrings)

def get_4_char_substring(file: list[str], row_number: int, column_number: int, direction : tuple[int, int]) -> str | None:
    if not 0 <= row_number + direction[0] * 3 < number_of_rows or not 0 <= column_number + direction[1] * 3 < number_of_columns:
        return None
    string = "X"
    for i in range(1, 4):
        string = string + file[row_number + direction[0] * i][column_number + direction[1] * i]
    print(string)
    return string

def check_for_x_mas(file: list[str], row_number: int, column_number: int) -> bool:
    if not 0 < row_number < number_of_rows - 1 or not 0 < column_number < number_of_columns - 1:
        return False
    cross_string = file[row_number -1][column_number - 1] + file[row_number -1][column_number + 1] + file[row_number + 1][column_number - 1] + file[row_number + 1][column_number + 1]
    return cross_string == "MSMS" or cross_string == "MMSS" or cross_string == "SMSM" or cross_string == "SSMM"

if __name__ == "__main__":
    file = Path("Advent Of Code 2024/Day_4/input.txt").read_text().splitlines()
    solution_1, solution_2 = get_day_4_solutions(file)
    print(f"XMAS Count: {solution_1}")
    print(f"X-MAS Count: {solution_2}")