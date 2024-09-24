import pytest

from src.domain.value_objects.coord import Coord


def test_valid_coord():
    lat = -20.23
    long = -20.23

    coord = Coord(lat, long)

    assert coord.get_long() == long
    assert coord.get_lat() == lat


@pytest.mark.parametrize(
    'lat, long, message',
    [
        (-100, -90, 'invalid latitude'),
        (-80, 190, 'invalid longitude'),
        (100, -90, 'invalid latitude'),
        (80, -190, 'invalid longitude'),
    ],
)
def test_invalid_coord(lat, long, message):
    with pytest.raises(Exception, match=message):
        Coord(lat, long)
