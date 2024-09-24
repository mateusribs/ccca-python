import pytest

from src.domain.value_objects.car_plate import CarPlate


def test_valid_car_plate():
    input = 'AAA1234'

    car_plate = CarPlate(input)

    assert car_plate.get_value() == input


@pytest.mark.parametrize(
    'input',
    [
        ('AA1234'),
        ('AAA123'),
        ('AA12'),
    ],
)
def test_invalid_car_plate(input):
    with pytest.raises(Exception, match='invalid car plate'):
        CarPlate(input)
