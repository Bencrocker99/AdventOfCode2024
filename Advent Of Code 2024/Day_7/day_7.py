import itertools
from pathlib import Path

def get_day_7_solutions(file: list[str]) -> tuple[int, int]:
    total_calibration_result = 0
    total_calibration_result_with_concatenation = 0
    for line in file:
        split_line: list[str] = line.split(":")
        calibration_result = int(split_line[0])
        equation_numbers: list[int] = [int(x) for x in split_line[1].strip().split()]
        calibration_result_without_concatenation = get_calibration_result_if_possible(calibration_result, equation_numbers, ["*","+"])
        if calibration_result_without_concatenation != 0:
            total_calibration_result += calibration_result_without_concatenation
            total_calibration_result_with_concatenation += calibration_result_without_concatenation
        else:
            total_calibration_result_with_concatenation += get_calibration_result_if_possible(calibration_result, equation_numbers, ["*", "+", "||"])
    return total_calibration_result, total_calibration_result_with_concatenation

def get_calibration_result_if_possible(calibration_result: int, equation_numbers:list[int], operators_list: list[str]) -> int:
    number_of_operators = len(equation_numbers) - 1
    operator_combinations = itertools.product(operators_list, repeat=number_of_operators)
    return calibration_result if is_equation_possible(calibration_result, equation_numbers, operator_combinations) else 0

def is_equation_possible(calibration_result: int, equation_numbers: list[int], operator_combinations) -> bool:
        for combination in operator_combinations:
            equation_result = equation_numbers[0]
            for i in range(len(combination)):
                if combination[i] == "+":
                    equation_result += equation_numbers[i + 1]
                elif combination[i] == "*":
                    equation_result *= equation_numbers[i + 1]
                else:
                    equation_result = int(str(equation_result) + str(equation_numbers[i + 1]))
            if calibration_result == equation_result:
                return True
        return False

if __name__ == "__main__":
    file = Path("Advent Of Code 2024/Day_7/input.txt").read_text().splitlines()
    solution_1, solution_2 = get_day_7_solutions(file)
    print(f"Total Calibration Result: {solution_1}")
    print(f"Total Calibration Result With Concatenation: {solution_2}")