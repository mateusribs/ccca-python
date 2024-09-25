import uuid

import pytest


def test_accept_ride_valid(ride_requested, driver, accept_ride, get_ride, get_account):
    input_accept_ride = {
        'ride_id': ride_requested['ride_id'],
        'driver_id': driver['account_id'],
    }

    accept_ride.execute(input_accept_ride)

    output_get_ride = get_ride.execute(ride_requested['ride_id'])
    assert output_get_ride['driver_id'] == driver['account_id']
    assert output_get_ride['status'] == 'accepted'


def test_accept_ride_when_driver_not_valid(ride_requested, passenger, accept_ride):
    input_accept_ride = {
        'ride_id': ride_requested['ride_id'],
        'driver_id': passenger['account_id'],
    }

    with pytest.raises(Exception, match='must be driver to accept ride'):
        accept_ride.execute(input_accept_ride)


def test_accept_ride_when_not_exists(passenger, accept_ride):
    input_accept_ride = {
        'ride_id': uuid.uuid4(),
        'driver_id': passenger['account_id'],
    }

    with pytest.raises(Exception, match='ride not found'):
        accept_ride.execute(input_accept_ride)


def test_accept_ride_when_ride_is_not_requested_status(ride_requested, driver, accept_ride):
    input_accept_ride = {
        'ride_id': ride_requested['ride_id'],
        'driver_id': driver['account_id'],
    }

    accept_ride.execute(input_accept_ride)

    with pytest.raises(Exception, match='invalid status'):
        accept_ride.execute(input_accept_ride)
