from pathlib import Path

number_of_rows: int = 0
number_of_columns: int = 0
frequencies_that_have_been_checked: set[str] = set(["."])
coordinates_with_antinodes: set[tuple[int, int]] = set()
coordinates_with_antinodes_any_position: set[tuple[int, int]] = set()

def get_day_8_solutions(file: list[str]) -> tuple[int, int]:
    global number_of_rows, number_of_columns
    number_of_rows = len(file)
    number_of_columns = len(file[0])
    for row in file:
        for char in row:
            if char not in frequencies_that_have_been_checked:
                get_antinodes_for_frequency(file, char)
                frequencies_that_have_been_checked.add(char)
    return len(coordinates_with_antinodes), len(coordinates_with_antinodes_any_position)

def get_antinodes_for_frequency(file: list[str], frequency: str):
    frequency_coordinates: list[tuple[int, int]] = []
    for i in range(number_of_rows):
        for j in range(number_of_columns):
            if file[i][j] == frequency:
                frequency_coordinates.append((i, j))
    for i in range(len(frequency_coordinates)):
        for j in range(i + 1, len(frequency_coordinates)):
            distance = get_distance_between_coordinates(frequency_coordinates[i], frequency_coordinates[j])
            get_antinodes_for_coordinate(frequency_coordinates[i], distance)
            get_antinodes_for_coordinates_any_position(frequency_coordinates[i], distance)
            get_antinodes_for_coordinates_any_position(frequency_coordinates[i], (distance[0] * -1, distance[1] * -1))

def get_antinodes_for_coordinate(coordinate: tuple[int, int], distance: tuple[int, int]):
    coordinate_to_check_1: tuple[int, int] = (coordinate[0] + 2 *  distance[0], coordinate[1] + 2 * distance[1])
    coordinate_to_check_2: tuple[int, int] = (coordinate[0] - distance[0], coordinate[1] - distance[1])
    if coordinate_is_in_bounds(coordinate_to_check_1):
        coordinates_with_antinodes.add(coordinate_to_check_1)
    if coordinate_is_in_bounds(coordinate_to_check_2):
        coordinates_with_antinodes.add(coordinate_to_check_2)

def get_antinodes_for_coordinates_any_position(coordinate: tuple[int, int], distance: tuple[int, int]):
    coordinate_in_range = True
    while(coordinate_in_range):
        if coordinate_is_in_bounds(coordinate):
            coordinates_with_antinodes_any_position.add(coordinate)
            coordinate = (coordinate[0] + distance[0], coordinate[1] + distance[1])
        else:
            coordinate_in_range = False

def get_distance_between_coordinates(coordinate_1: tuple[int, int], coordinate_2: tuple[int, int]) -> tuple[int, int]:
    return (coordinate_2[0] - coordinate_1[0], coordinate_2[1] - coordinate_1[1])

def coordinate_is_in_bounds(coordinate: tuple[int, int]) -> bool:
    return 0 <= coordinate[0] < number_of_rows and 0 <= coordinate[1] < number_of_columns

if __name__ == "__main__":
    file = Path("Advent Of Code 2024/Day_8/input.txt").read_text().splitlines()
    solution_1, solution_2 = get_day_8_solutions(file)
    print(f"Total sum of Scores of Trailheads: {solution_1}")
    print(f"Total sum of Ratings of Trailheads: {solution_2}")