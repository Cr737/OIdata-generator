from typing import Any, List

import cyaron

from genoirator.abstract_genoirator import AbstractGenoirator
from genoirator.base.base_oitype import OI_integer, OI_vector


class BaseGenoirator(AbstractGenoirator):
    """
    Input: two integers L, R
    Output: 1 integers between [L, R]
    """

    def check_args(self, args):
        for arg in args:
            if not isinstance(arg, OI_integer):
                return False
        return True

    def parse_args(self) -> List:
        args = [OI_integer() for i in range(self._n)]
        for arg in args:
            arg.input()
        return args

    def gen(self):
        args = self.get_args()
        ret = []
        for arg in args:
            ret.append(arg.gen())
        return ret


class VectorGenoirator(BaseGenoirator):
    """
    Input: three integers n, L, R
    Output: n integers between [L, R]
    """

    def check_args(self, args):
        for arg in args:
            if not isinstance(arg, OI_vector):
                return False
        return True

    def parse_args(self) -> List:
        args = [OI_vector() for i in range(self._n)]
        for arg in args:
            arg.input()
        return args

    def gen(self):
        args = self.get_args()
        ret = []
        for arg in args:
            ret.append(arg.gen())
        return ret
