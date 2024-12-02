from pathlib import Path

MAXIMUM_INCREMENT_VALUE = 3

def get_day_2_solutions(file: list[str]) -> tuple[int, int]:
    number_of_safe_reports, number_of_safe_reports_with_dampener = 0, 0
    for line in file:
        report: list[int] = [int(x) for x in line.split()]
        if _is_report_safe(report):
            number_of_safe_reports += 1
        if _is_report_safe_with_dampener(report):
            number_of_safe_reports_with_dampener += 1

    return number_of_safe_reports, number_of_safe_reports_with_dampener


def _is_report_safe(report) -> bool:
        is_ascending: bool = report[0] < report[1]
        for i in range(len(report) - 1):
            if is_ascending and report[i] >= report[i + 1] or report[i + 1] > report[i] + MAXIMUM_INCREMENT_VALUE:
                return False
            elif not is_ascending and report[i] <= report[i + 1] or report[i + 1] < report[i] - MAXIMUM_INCREMENT_VALUE:
                return False
        return True

def _is_report_safe_with_dampener(report) -> bool:
    for i in range(len(report)):
        report_duplicate = report.copy()
        del report_duplicate[i]
        if _is_report_safe(report_duplicate):
            return True
    return False


if __name__ == "__main__":
    file = Path("Advent Of Code 2024/Day_2/input.txt").read_text().splitlines()
    solution_1, solution_2 = get_day_2_solutions(file)
    print(f"Number of Safe Reports: {solution_1}")
    print(f"Number of Safe Reports with Dampener: {solution_2}")