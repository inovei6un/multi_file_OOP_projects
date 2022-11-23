class Validator:
    @staticmethod
    def raise_if_empty_string_or_whites_space(string, message):
        if string.strip() == '':
            raise ValueError(message)
