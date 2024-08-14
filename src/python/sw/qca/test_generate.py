from enum import Enum, auto


class QcaCellType(Enum):
    """
    Types of QCA Cells
    Type ONE - inputs on left and down
    Type TWO - inputs on right and down
    Type THREE - inputs on left and up
    Type FOUR - inputs on right and up

    """

    ONE: int = 0
    TWO: int = 1
    THREE: int = 2
    FOUR: int = 3


def get_cell_offsets(cell_type: QcaCellType) -> list[int]:
    """
    Cells line,column offsets

    Type ONE - inputs on left and down
    Type TWO - inputs on right and down
    Type THREE - inputs on left and up
    Type FOUR - inputs on right and up

    """
    if cell_type == QcaCellType.ONE:
        return [[0, -1], [1, 0]]
    elif cell_type == QcaCellType.TWO:
        return [[0, 1], [1, 0]]
    elif cell_type == QcaCellType.THREE:
        return [[0, -1], [-1, 0]]
    else:
        return [[0, 1], [-1, 0]]


def get_next_cells_types(cell_type: QcaCellType) -> list[QcaCellType]:
    """
        Cells of type ONE always connects to cells of type TWO and THREE
        Cells of type TWO always connects to cells of type FOUR and ONE
        Cells of type THREE always connects to cells of type FOUR and ONE
        Cells of type FOUR always connects to cells of type TWO and THREE
    """
    if cell_type == QcaCellType.ONE:
        return [QcaCellType.TWO, QcaCellType.THREE]
    elif cell_type == QcaCellType.TWO:
        return [QcaCellType.FOUR, QcaCellType.ONE]
    elif cell_type == QcaCellType.THREE:
        return [QcaCellType.FOUR, QcaCellType.ONE]
    else:
        return [QcaCellType.TWO, QcaCellType.THREE]


def next_c_l(cell_type: QcaCellType, level: int):
    if level == 1:
        return get_cell_offsets(cell_type)

    level = level - 1
    next_cells_types = get_next_cells_types(cell_type)
    result = []
    for c_t in next_cells_types:
        ret = next_c_l(c_t, level)
        for r in ret:
            result.append(r)
    actual_cell_offsets = get_cell_offsets(cell_type)

    return result


level = 3
cell_type = QcaCellType.ONE
result = next_c_l(cell_type, level)
a  = 1
