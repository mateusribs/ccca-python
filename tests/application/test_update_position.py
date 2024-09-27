import uuid

import pytest


def test_update_position_valid(ride_started, get_ride, update_position):
    input_update_position = {
        'ride_id': ride_started,
        'lat': -27.584905257808835,
        'long': -48.545022195325124,
    }

    update_position.execute(input_update_position)

    input_update_position2 = {
        'ride_id': ride_started,
        'lat': -27.496887588317275,
        'long': -48.522234807851476,
    }

    update_position.execute(input_update_position2)

    input_update_position3 = {
        'ride_id': ride_started,
        'lat': -27.584905257808835,
        'long': -48.545022195325124,
    }

    update_position.execute(input_update_position3)

    input_update_position4 = {
        'ride_id': ride_started,
        'lat': -27.496887588317275,
        'long': -48.522234807851476,
    }

    update_position.execute(input_update_position4)

    output_get_ride = get_ride.execute(ride_started)
    assert output_get_ride['distance'] == 30


def test_update_position_invalid(ride_started, update_position):
    with pytest.raises(Exception, match='ride not found'):
        input_update_position = {
            'ride_id': uuid.uuid4(),
            'lat': -27.584905257808835,
            'long': -48.545022195325124,
        }

        update_position.execute(input_update_position)
