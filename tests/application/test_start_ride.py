import pytest


def test_start_ride_valid(ride_requested, driver, accept_ride, get_ride, start_ride):
    input_accept_ride = {
        'ride_id': ride_requested['ride_id'],
        'driver_id': driver['account_id'],
    }

    accept_ride.execute(input_accept_ride)

    input_start_ride = {'ride_id': ride_requested['ride_id']}

    start_ride.execute(input_start_ride)
    output_get_ride = get_ride.execute(ride_requested['ride_id'])
    assert output_get_ride['status'] == 'in_progress'


def test_start_ride_status_invalid(ride_requested, driver, accept_ride, start_ride):
    input_accept_ride = {
        'ride_id': ride_requested['ride_id'],
        'driver_id': driver['account_id'],
    }

    accept_ride.execute(input_accept_ride)

    input_start_ride = {'ride_id': ride_requested['ride_id']}

    start_ride.execute(input_start_ride)

    with pytest.raises(Exception, match='invalid status'):
        start_ride.execute(input_start_ride)
