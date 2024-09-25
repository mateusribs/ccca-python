import pytest

from src.domain.value_objects.ride_status import RideStatus


def test_ride_status_initial():
    status = RideStatus('requested')

    assert status.get_value() == 'requested'


def test_ride_status_transition_from_request_to_accept():
    status = RideStatus('requested')

    status.accept()

    assert status.get_value() == 'accepted'


def test_ride_status_transition_from_accepted_to_in_progress():
    status = RideStatus('accepted')

    status.in_progress()

    assert status.get_value() == 'in_progress'


def test_ride_status_invalid_transition_from_request_to_in_progress():
    status = RideStatus('requested')

    with pytest.raises(Exception, match='invalid status'):
        status.in_progress()


def test_ride_status_invalid_transition_from_in_progress_to_accepted():
    status = RideStatus('in_progress')

    with pytest.raises(Exception, match='invalid status'):
        status.accept()
