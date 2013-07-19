Ambit
=====

A library for manipulating ranges within a series.

    >>> from ambit.range import Range
    >>> Range(2, 8) | Range(5, 13)
    Range(2, 13)
    >>> Range(2, 8) & Range (5, 10)
    Range(5, 8)
    >>> len(Range(0, 3))
    3
    >>> Range(0, 3) + Range (2, 4)
    5

And other such things.