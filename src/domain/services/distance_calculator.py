import math

from src.domain.value_objects.coord import Coord

EARTH_RADIUS = 6371
DEGREES_TO_RADIUS = math.pi / 180


def compute_distance(from_coord: Coord, to_coord: Coord):
    delta_lat = (to_coord.get_lat() - from_coord.get_lat()) * DEGREES_TO_RADIUS
    delta_long = (to_coord.get_long() - from_coord.get_long()) * DEGREES_TO_RADIUS
    a = math.sin(delta_lat / 2) * math.sin(delta_lat / 2) + math.cos(
        from_coord.get_lat() * DEGREES_TO_RADIUS
    ) * math.cos(to_coord.get_lat() * DEGREES_TO_RADIUS) * math.sin(delta_long / 2) * math.sin(
        delta_long / 2
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = EARTH_RADIUS * c
    return round(distance)


def calculate_distance_by_positions(positions: list) -> int:
    distance = 0
    for index, position in enumerate(positions):
        try:
            next_position = positions[index + 1]
        except IndexError:
            continue
        distance += compute_distance(position.get_coord(), next_position.get_coord())

    return distance
