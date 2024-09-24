import pytest

from src.domain.value_objects.cpf import CPF


@pytest.mark.parametrize(
    'valid_cpf',
    [
        ('97456321558'),
        ('71428793860'),
        ('87748248800'),
    ],
)
def test_cpf_when_cpf_is_valid(valid_cpf):
    cpf = CPF(valid_cpf)
    assert cpf.get_value() == valid_cpf


@pytest.mark.parametrize(
    'invalid_cpf',
    [
        ('9745632155'),
        ('11111111111'),
        ('97a56321558'),
    ],
)
def test_cpf_when_cpf_is_invalid(invalid_cpf):
    with pytest.raises(Exception, match='invalid cpf'):
        CPF(invalid_cpf)
