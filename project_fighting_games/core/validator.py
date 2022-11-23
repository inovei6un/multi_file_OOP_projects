class Validator:
    @staticmethod
    def raise_if_empty_string(string, message):
        if string == '':
            raise ValueError(message)

    @staticmethod
    def raise_if_value_is_negative(value, message):
        if value < 0:
            raise ValueError(message)
