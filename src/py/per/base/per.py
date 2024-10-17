from abc import ABC, abstractmethod
from enum import Enum, auto


class PeR(ABC):
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
    ZIG_ZAG_NO_PRIORITY: int = auto()
    DEPTH_FIRST_NO_PRIORITY: int = auto()
    ZIG_ZAG_WITH_PRIORITY: int = auto()
    DEPTH_FIRST_WITH_PRIORITY: int = auto()
