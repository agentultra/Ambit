from collections import namedtuple
from operator import div, floordiv, mul, truediv


class Interval(namedtuple("Interval", ["start", "end"])):

    __slots__ = ()

    @property
    def size(self):
        return self.end - self.start

    def _quotients(self, divop, other):
        if not all([other.start, other.end]):
            raise ZeroDivisionError("Cannot divide %r "
                                    "by %r" % (self, other))
        return [divop(x, y)
                for x in (self.start, self.end)
                for y in (other.start, other.end)]

    def __add__(self, other):
        return Interval(self.start + other.start,
                        self.end + other.end)

    def __sub__(self, other):
        return Interval(self.start - other.end,
                        self.end - other.start)

    def __mul__(self, other):
        products = [mul(x, y)
                    for x in (self.start, self.end)
                    for y in (other.start, other.end)]
        return Interval(min(products), max(products))

    def __div__(self, other):
        quotients = self._quotients(div, other)
        return Interval(min(quotients), max(quotients))

    def __floordiv__(self, other):
        quotients = self._quotients(floordiv, other)
        return Interval(min(quotients), max(quotients))

    def __truediv__(self, other):
        quotients = self._quotients(truediv, other)
        return Interval(min(quotients), max(quotients))

    def __iadd__(self, other):
        raise ValueError("Operation not supported")

    def __isub__(self, other):
        raise ValueError("Operation not supported")

    def __imul__(self, other):
        raise ValueError("Operation not supported")

    def __idiv__(self, other):
        raise ValueError("Operation not supported")

    def __itruediv__(self, other):
        raise ValueError("Operation not supported")

    def __nonzero__(self):
        if all([f is not None for f in self._fields]):
            if self.start or self.end:
                return True
        return False

    def __and__(self, other):
        if self.end < other.start or other.end < self.start:
            return Interval(None, None)
        else:
            return Interval(max([self.start, other.start]),
                         min([self.end, other.end]))

    def __or__(self, other):
        start = min([self.start, other.start])
        end = max([self.end, other.end])

        return Interval(start, end)

    def __len__(self):
        return self.size
