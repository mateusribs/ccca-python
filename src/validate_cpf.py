CPF_VALID_LENGTH = 11
FIRST_DIGIT_FACTOR = 10
SECOND_DIGIT_FACTOR = 11


def validate_cpf(cpf: str):
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != CPF_VALID_LENGTH:
        return False
    if all_digits_the_same(cpf):
        return False
    digit1 = calculate_digit(cpf, FIRST_DIGIT_FACTOR)
    digit2 = calculate_digit(cpf, SECOND_DIGIT_FACTOR)
    return f'{digit1}{digit2}' == extract_digit(cpf)


def all_digits_the_same(cpf: str) -> bool:
    first_digit = cpf[0]
    return all(digit == first_digit for digit in cpf)


def calculate_digit(cpf: str, factor: int) -> int:
    total = 0
    for digit in cpf:
        if factor > 1:
            total += int(digit) * factor
            factor -= 1
    remainder = total % 11
    return 0 if remainder < 2 else 11 - remainder


def extract_digit(cpf: str) -> str:
    return cpf[9:]
