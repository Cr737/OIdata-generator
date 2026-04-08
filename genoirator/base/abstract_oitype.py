from abc import ABC, abstractmethod
from typing import Any


class AbstractOIType(ABC):
    """abstract oi type"""

    @abstractmethod
    def input(self):
        """input data range"""
        pass

    @abstractmethod
    def gen(self) -> Any:
        """gen"""
        pass
