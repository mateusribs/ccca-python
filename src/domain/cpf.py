class CPF:
    CPF_VALID_LENGTH = 11
    FIRST_DIGIT_FACTOR = 10
    SECOND_DIGIT_FACTOR = 11

    def __init__(self, value: str) -> None:
        self.__value = self.__validate(value)

    def __validate(self, value: str):
        cpf = ''.join(filter(str.isdigit, value))
        if len(cpf) != self.CPF_VALID_LENGTH:
            raise Exception('invalid cpf')
        if self.__all_digits_the_same(cpf):
            raise Exception('invalid cpf')
        digit1 = self.__calculate_digit(cpf, self.FIRST_DIGIT_FACTOR)
        digit2 = self.__calculate_digit(cpf, self.SECOND_DIGIT_FACTOR)
        if not f'{digit1}{digit2}' == self.__extract_digit(cpf):
            raise Exception('invalid cpf')
        return value

    def __all_digits_the_same(self, cpf: str) -> bool:
        first_digit = cpf[0]
        return all(digit == first_digit for digit in cpf)

    def __calculate_digit(self, cpf: str, factor: int) -> int:
        total = 0
        for digit in cpf:
            if factor > 1:
                total += int(digit) * factor
                factor -= 1
        remainder = total % 11
        return 0 if remainder < 2 else 11 - remainder

    def __extract_digit(self, cpf: str) -> str:
        return cpf[9:]

    def get_value(self) -> str:
        return self.__value
