from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

@dataclass
class Guard:
    current_coordinate: tuple[int, int]
    direction_vector: tuple[int, int]

@dataclass
class VisitedPosition:
    position_coordinate: tuple[int, int]
    rotation_vectors_visited: list[tuple[int, int]]

guard_position_to_movement_vector: dict[str, tuple[int, int]] = {"^": (-1, 0), ">": (0, -1), "v": (1, 0), "<": (0, 1)}
obstacle_positions: list[tuple[int, int]] = []
position_coordinates_to_visited_positions = {}
number_of_rows: int = 0
number_of_columns: int = 0

def get_day_6_solutions(file: list[str]) -> tuple[int, int]:
    global number_of_rows
    global number_of_columns
    number_of_rows = len(file)
    number_of_columns = len(file[0])
    guard = get_starting_guard(file)
    set_obstacle_positions(file)
    guard_has_exited = False
    while not guard_has_exited:
        guard_has_exited = move_guard_forwards(guard) == None
    distinct_positions_visited = len(position_coordinates_to_visited_positions)
    number_of_potential_infinite_loops = get_number_of_potential_infinite_loops(file)
    return distinct_positions_visited, number_of_potential_infinite_loops

def get_starting_guard(file: list[str]) -> Guard:
    for direction_symbol in guard_position_to_movement_vector.keys():
        for i in range(number_of_columns):
            for j in range(number_of_rows):
                if file[i][j] == direction_symbol:
                     guard = Guard((i, j), guard_position_to_movement_vector[direction_symbol])
                     position_coordinates_to_visited_positions[(i, j)] = VisitedPosition((i, j), [guard.direction_vector])
    return guard

def set_obstacle_positions(file: list[str]) -> None:
    for i in range(number_of_columns):
        for j in range(number_of_rows):
            if file[i][j] == "#":
                obstacle_positions.append((i, j))

def move_guard_forwards(guard: Guard) -> tuple[int, int] | None:
    global position_coordinates_to_visited_positions
    new_coordinate: tuple[int, int] = guard.current_coordinate[0] + guard.direction_vector[0], guard.current_coordinate[1]  + guard.direction_vector[1]
    if not 0 <= new_coordinate[0] < number_of_rows or not 0 <= new_coordinate[1] < number_of_columns:
        return None
    elif new_coordinate in obstacle_positions:
        guard.direction_vector = rotate_vector_90_degrees_clockwise(guard.direction_vector)
    else:
        guard.current_coordinate = new_coordinate
        if new_coordinate in position_coordinates_to_visited_positions:
            position_coordinates_to_visited_positions[new_coordinate].rotation_vectors_visited.append(guard.direction_vector)
        else:
            position_coordinates_to_visited_positions[(new_coordinate)] = VisitedPosition(new_coordinate, [guard.direction_vector])
    return new_coordinate

def get_number_of_potential_infinite_loops(file: list[str]) -> int:
    global position_coordinates_to_visited_positions
    number_of_potential_infinite_loops = 0
    positions_originally_visited: list[VisitedPosition] = position_coordinates_to_visited_positions.keys()
    for position in positions_originally_visited:
        position_coordinates_to_visited_positions = {}
        guard: Guard = get_starting_guard(file)
        if position == guard.current_coordinate:
            continue
        obstacle_positions.append((position[0], position[1]))
        guard_has_exited = False
        while not guard_has_exited:
            new_coordinate = move_guard_forwards(guard)
            guard_has_exited = new_coordinate == None
            if not guard_has_exited:
                if is_in_infinite_loop(new_coordinate, guard.direction_vector):
                    number_of_potential_infinite_loops += 1
                    break
            else:
                break
        obstacle_positions.remove((position[0], position[1]))
    return number_of_potential_infinite_loops

def is_in_infinite_loop(new_position_coordiante: tuple[int, int], new_rotation_vector) -> bool:
    global position_coordinates_to_visited_positions
    if new_position_coordiante in position_coordinates_to_visited_positions:
        return position_coordinates_to_visited_positions[new_position_coordiante].rotation_vectors_visited.count(new_rotation_vector) > 1
    return False

def rotate_vector_90_degrees_clockwise(vector: tuple[int, int]) -> tuple[int, int]:
    return vector[1], vector[0] * -1

if __name__ == "__main__":
    file = Path("Advent Of Code 2024/Day_6/input.txt").read_text().splitlines()
    solution_1, solution_2 = get_day_6_solutions(file)
    print(f"Distinct Positions Visited: {solution_1}")
    print(f"Number of Infinite Loop Causing Obstacles: {solution_2}")