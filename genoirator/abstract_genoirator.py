import os
from abc import ABC, abstractmethod
from typing import Any, List


class AbstractGenoirator(ABC):
    """
    Abstract base class for generating test cases.

    Subclasses must implement check_args(), parge_args() and gen() methods
    to define specific test case generation logic.

    Attributes:
        n: Number of test cases to generate
        std: Path to the standard executor file
    """

    _n: int
    _std: str

    def __init__(self, n: int, std: str):
        self._n = n
        self._std = std

    @abstractmethod
    def check_args(self, args) -> bool:
        """check args"""
        pass

    @abstractmethod
    def parse_args(self) -> List:
        """parse args"""
        pass

    @abstractmethod
    def gen(self) -> Any:
        """generator data"""
        pass

    def _validate_args(self, args) -> None:
        """raise error when args are illegal"""
        if not self.check_args(args):
            raise ValueError(f"args {args} illegal. Please check args.")

    def get_args(self) -> Any:
        args = self.parse_args()
        self._validate_args(args)
        return args
