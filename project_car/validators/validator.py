class Validator:

    @staticmethod
    def raise_if_len_is_less_than(obj, min_len, message):
        if len(obj) < min_len:
            raise ValueError(message)

    @staticmethod
    def raise_if_num_is_not_in_range(value, min_value, max_value, message):
        if value < min_value or value > max_value:
            raise ValueError(message)
