from collections import defaultdict
from pathlib import Path


def get_day_5_solutions(file: list[str]) -> tuple[int, int]:
    page_number_to_pages_that_come_after = defaultdict(list)
    for line in file[0].split("\n"):
        split_line = line.split("|")
        page_number = int(split_line[0])
        page_number_to_pages_that_come_after[page_number].append(int(split_line[1]))
    sum_of_middle_pages_for_valid: int = 0
    sum_of_middle_pages_for_originally_invalid: int = 0
    for line in file[1].split("\n"):
        center_page: tuple[int, int] = get_centre_page_of_update(page_number_to_pages_that_come_after, line)
        sum_of_middle_pages_for_valid += center_page[0]
        sum_of_middle_pages_for_originally_invalid += center_page[1]
    return sum_of_middle_pages_for_valid, sum_of_middle_pages_for_originally_invalid

def get_centre_page_of_update(page_number_to_pages_that_come_after: dict[list], pages: str) -> tuple[int, int]:
    split_pages: list[int] = [int(x) for x in pages.split(",")]
    for i in range (1, len(split_pages)):
        current_page = split_pages[i]
        for page_that_comes_before in split_pages[:i]:
            if page_that_comes_before in page_number_to_pages_that_come_after[current_page]:
                return 0, get_centre_page_of_incorrectly_ordered_update(page_number_to_pages_that_come_after, split_pages)
    return get_centre_value_of_list(split_pages), 0

def get_centre_page_of_incorrectly_ordered_update(page_number_to_pages_that_come_after: dict[list], split_pages: list[int]) -> int:
    ordered_list = []
    for i in range (len(split_pages)):
        latest_index_can_be_inserted = len(ordered_list)
        for j in range(1, len(ordered_list) + 1):
            if (ordered_list[len(ordered_list)- j] in page_number_to_pages_that_come_after[split_pages[i]]):
                latest_index_can_be_inserted = len(ordered_list) - j
        ordered_list.insert(latest_index_can_be_inserted, split_pages[i])
    return get_centre_value_of_list(ordered_list)

def get_centre_value_of_list(list: list[int]) -> int:
    return list[len(list) // 2]

if __name__ == "__main__":
    file = Path("Advent Of Code 2024/Day_5/input.txt").read_text().split("\n\n")
    solution_1, solution_2 = get_day_5_solutions(file)
    print(f"Sum of Middle Pages of Valid Printed Updates: {solution_1}")
    print(f"Sum of Middle Pages of Originally Invalid Printed Updates: : {solution_2}")