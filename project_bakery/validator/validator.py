class Validator:
    @staticmethod
    def raise_if_empty_string_or_whitespace(string: str, message: str):
        if string.strip() == '':
            raise ValueError(message)

    @staticmethod
    def raise_if_value_is_0_or_less(value, message: str):
        if value <= 0:
            raise ValueError(message)

    @staticmethod
    def raise_if_number_is_not_in_range(value: int, min_value: int, max_value: int, message: str):
        if value < min_value or value > max_value:
            raise ValueError(message)
