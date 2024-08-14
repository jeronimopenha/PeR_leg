from src.python.sw.qca.qca_utils import QcaBoardType

from src.python.util.util import Util


class QcaBoard:
    def __init__(self, type: QcaBoardType, width: int, height: int):
        self.type: QcaBoardType = type
        self.width: int = width
        self.height: int = height
        self.four_first_cells: list[list[QcaCell]] = [[]]

    def get_cell(self, x: int, y: int):
        return
