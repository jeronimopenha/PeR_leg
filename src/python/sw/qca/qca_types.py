from enum import Enum, auto


class QcaCellType(Enum):
    '''
    Types of QCA Cells
    Type ONE - inputs on left and down
    Type TWO - inputs on right and down
    Type THREE - inputs on left and up
    Type FOUR - inputs on right and up

    Type ONE - outputs on right and up
    Type TWO - outputs on left and up
    Type THREE - outputs on right and down
    Type FOUR - outputs on left and down
    '''

    ONE: int = auto()
    TWO: int = auto()
    THREE: int = auto()
    FOUR: int = auto()


class QcaBoardType(Enum):
    '''
    Types of QCA Cells
    Type ONE - inputs on left and down
    Type TWO - inputs on right and down
    Type THREE - inputs on left and up
    Type FOUR - inputs on right and up

    Type ONE - outputs on right and up
    Type TWO - outputs on left and up
    Type THREE - outputs on right and down
    Type FOUR - outputs on left and down
    '''

    ONE: list[list[QcaCellType]] = [
        [QcaCellType.ONE, QcaCellType.THREE],
        [QcaCellType.TWO, QcaCellType.FOUR],
    ]
    TWO: list[list[QcaCellType]] = [
        [QcaCellType.TWO, QcaCellType.FOUR],
        [QcaCellType.ONE, QcaCellType.THREE],
    ]
    THREE: list[list[QcaCellType]] = [
        [QcaCellType.THREE, QcaCellType.ONE],
        [QcaCellType.FOUR, QcaCellType.TWO],
    ]
    FOUR: list[list[QcaCellType]] = [
        [QcaCellType.FOUR, QcaCellType.TWO],
        [QcaCellType.THREE, QcaCellType.ONE],
    ]



