Ambit
=====

A library for interval arithmetic, bisection, and analysis.

    >>> from ambit.interval import Interval
    >>> Interval(2, 8) | Interval(5, 13)
    Interval(2, 13)
    >>> Interval(2, 8) & Interval(5, 10)
    Interval(5, 8)
    >>> len(Interval(0, 3))
    4
    >>> Interval(1, 3) + Interval(2, 4)
    Interval(3, 7)

And other such things.
