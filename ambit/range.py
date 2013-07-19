from collections import namedtuple


class Range(namedtuple("Range", ["start", "end"])):

    __slots__ = ()

    @property
    def interval(self):
        return self.end - self.start

    def __add__(self, other):
        return self.interval + other.interval

    def __sub__(self, other):
        return self.interval - other.interval

    def __mul__(self, other):
        return self.interval * other.interval

    def __div__(self, other):
        return self.interval / other.interval

    def __iadd__(self, other):
        raise ValueError("Operation not supported")

    def __isub__(self, other):
        raise ValueError("Operation not supported")

    def __imul__(self, other):
        raise ValueError("Operation not supported")

    def __idiv__(self, other):
        raise ValueError("Operation not supported")

    def __nonzero__(self):
        if all([f is not None for f in self._fields]):
            if self.start or self.end:
                return True
        return False

    def __and__(self, other):
        if self.end < other.start or other.end < self.start:
            return Range(None, None)
        else:
            return Range(max([self.start, other.start]),
                         min([self.end, other.end]))

    def __or__(self, other):
        start = min([self.start, other.start])
        end = max([self.end, other.end])

        return Range(start, end)

    def __len__(self):
        return self.interval
