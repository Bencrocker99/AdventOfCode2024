import bisect
from pathlib import Path


def get_day_1_solutions(file: list[str]) -> tuple[int, int]:
    list_1, list_2 = [], []

    for line in file:
        bisect.insort(list_1, line.split()[0])
        bisect.insort(list_2, line.split()[1])

    total_distance, similarity_score = 0, 0

    for i in range(len(list_1)):
        total_distance += abs(int(list_1[i]) - int(list_2[i]))
        similarity_score += list_2.count(list_1[i]) * int(list_1[i])

    return total_distance, similarity_score

if __name__ == "__main__":
    file = Path("Day_1/input.txt").read_text().splitlines()
    solution_1, solution_2 = get_day_1_solutions(file)
    print(f"Total Distance: {solution_1}")
    print(f"Similarity Score: {solution_2}")