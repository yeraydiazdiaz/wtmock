class Field:
    def __init__(self, type_, default, value=None):
        self.type_ = type_
        self.default = default
        self._value = value

    @property
    def value(self):
        if self._value is None:
            return self.default
        else:
            return self._value
