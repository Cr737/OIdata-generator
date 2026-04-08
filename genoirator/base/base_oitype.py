"""base type"""

from typing import List, Optional

from cyaron import randint

from genoirator.base.abstract_oitype import AbstractOIType


class OI_integer(AbstractOIType):
    _L: Optional[int] = None
    _R: Optional[int] = None

    def __init__(self, L: Optional[int] = None, R: Optional[int] = -1):
        self._L = L
        self._R = R

    def input(self) -> None:
        s = input("input two integers in one line, separate by space, l <= r: ")
        self._L, self._R = map(int, s.split())

    def gen(self) -> int:
        if self._L is None or self._R is None:
            raise ValueError(f"Datarange L and R must be declared.")
        return randint(self._L, self._R)


class OI_vector(AbstractOIType):
    _n: Optional[OI_integer] = None
    _int: Optional[OI_integer] = None

    def __init__(
        self, n: Optional[OI_integer] = None, inte: Optional[OI_integer] = None
    ):
        self._n = n
        self._int = inte

    def input(self) -> None:
        print("input range of the length of vector:")
        self._n = OI_integer()
        self._n.input()
        print("input range of the element of vector:")
        self._int = OI_integer()
        self._int.input()

    def gen(self) -> List:
        if self._n is None or self._int is None:
            raise ValueError(f"Length n and Datarange must be declared.")
        ret = []
        n = self._n.gen()
        for i in range(n):
            ret.append(self._int.gen())
        return ret
