class Validator:
    @staticmethod
    def raise_if_empty_string(obj, message):
        if obj == '':
            raise ValueError(message)

    @staticmethod
    def raise_if_value_is_0_or_less(obj, message):
        if obj <= 0:
            raise ValueError(message)
