from abc import ABC, abstractmethod


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
