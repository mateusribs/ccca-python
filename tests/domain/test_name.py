import pytest

from src.domain.value_objects.name import Name


def test_valid_name():
    input = 'John Doe'

    name = Name(input)

    assert name.get_value() == input


def test_invalid_name():
    input = 'John'
    with pytest.raises(Exception, match='invalid name'):
        Name(input)
