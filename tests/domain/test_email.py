import pytest

from src.domain.value_objects.email import Email


def test_valid_email():
    input = 'john.doe@gmail.com'

    email = Email(input)

    assert email.get_value() == input


@pytest.mark.parametrize(
    'input',
    [
        ('john.doe'),
        ('john@gmail.'),
        ('john.doe@'),
    ],
)
def test_invalid_email(input):
    with pytest.raises(Exception, match='invalid email'):
        Email(input)
