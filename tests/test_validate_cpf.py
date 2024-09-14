from driver_app.validate_cpf import validate_cpf


def test_validate_cpf_digit_different_from_zero():
    cpf = '97456321558'
    is_valid = validate_cpf(cpf)
    assert is_valid


def test_validate_cpf_second_digit_equals_zero():
    cpf = '71428793860'
    is_valid = validate_cpf(cpf)
    assert is_valid


def test_validate_cpf_first_digit_equals_zero():
    cpf = '87748248800'
    is_valid = validate_cpf(cpf)
    assert is_valid


def test_validate_cpf_less_than_11_chars():
    cpf = '9745632155'
    is_valid = validate_cpf(cpf)
    assert not is_valid


def test_validate_cpf_all_chars_the_same():
    cpf = '11111111111'
    is_valid = validate_cpf(cpf)
    assert not is_valid


def test_validate_cpf_with_letter():
    cpf = '97a56321558'
    is_valid = validate_cpf(cpf)
    assert not is_valid
