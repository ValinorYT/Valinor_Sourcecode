class HashWrapper:
    def __init__(self, val):
        self.val = val

    def __hash__(self):
        return hash(str(self.val))

    def __repr__(self):
        return str(self.val)

    def __eq__(self, other):
        return str(self.val) == str(other.val)
