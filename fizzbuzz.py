from typing import List
from operator import mod, add
from functools import reduce


def fizzbuzzlist(l: List[int]) -> str:
    return reduce(
        lambda col, i: col + (
            reduce(
                add,
                map(lambda x: x[1] if not mod(i, x[0]) else '',
                    ((3, 'Fizz'), (5, 'Buzz'))
                    )
            ) or str(i)),
        l,
        '')
