from abc import ABC, abstractmethod
from enum import Enum, auto


class PeR(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def per_sa(self):
        pass

    @abstractmethod
    def per_yoto(self):
        pass

    @abstractmethod
    def per_yott(self):
        pass


class EdgesAlgEnum(Enum):
    ZIG_ZAG: int = auto()
    DEPTH_FIRST: int = auto()
