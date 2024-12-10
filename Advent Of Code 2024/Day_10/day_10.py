from pathlib import Path

number_of_rows: int = 0
number_of_columns: int = 0
distinct_9_coordiantes_reached: set[tuple[int, int]]

def get_day_10_solutions(file: list[str]) -> tuple[int, int]:
    global number_of_rows, number_of_columns, distinct_9_coordiantes_reached
    number_of_rows = len(file)
    number_of_columns = len(file[0])
    total_sum_of_scores_of_trailheads = 0
    total_sum_of_ratings_of_trailheads = 0
    for i in range(number_of_rows):
        for j in range(number_of_columns):
            if int(file[i][j]) == 0:
                distinct_9_coordiantes_reached = set()
                total_sum_of_ratings_of_trailheads += get_score_for_trailhead(file, i, j, 0)
                total_sum_of_scores_of_trailheads += len(distinct_9_coordiantes_reached)
    return total_sum_of_scores_of_trailheads, total_sum_of_ratings_of_trailheads

def get_score_for_trailhead(file: list[str], row: int, col: int, current_index: int) -> int:
    if not 0 <= row < number_of_rows or not 0 <= col < number_of_columns or int(file[row][col]) != current_index:
        return 0
    if current_index == 9:
        distinct_9_coordiantes_reached.add((row,col))
        return 1
    return ((get_score_for_trailhead(file, row + 1, col, current_index + 1)
            + get_score_for_trailhead(file, row, col + 1, current_index + 1)
            + get_score_for_trailhead(file, row - 1, col, current_index + 1)
            + get_score_for_trailhead(file, row, col - 1, current_index + 1)))

if __name__ == "__main__":
    file = Path("Advent Of Code 2024/Day_10/input.txt").read_text().splitlines()
    solution_1, solution_2 = get_day_10_solutions(file)
    print(f"Total sum of Scores of Trailheads: {solution_1}")
    print(f"Total sum of Ratings of Trailheads: {solution_2}")