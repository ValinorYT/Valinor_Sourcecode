class HashWrapper:
    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return str(self.val)

    def __hash__(self):
        return hash(self.__repr__())

    def __eq__(self, other):
        return self.__repr__() == other.__repr__()
