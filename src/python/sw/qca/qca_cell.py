from enum import Enum, auto
from src.python.sw.qca.qca_utils import QcaBoardType, QcaUtils


class QcaCell:
    input_patterns: list[list[list[int]]] = [
        # cell type
        # One
        [
            [[0, -1], [+1, 0]],
            [[0, -2], [-1, -1], [, ], [, ]],
            [[, ], [, ], [, ], [, ], [, ], [, ], [, ], [, ]]
        ],
        # Two
        [
            [[, ], [, ]],
            [[, ], [, ], [, ], [, ]],
            [[, ], [, ], [, ], [, ], [, ], [, ], [, ], [, ]]
        ],
        # Three
        [
            [[, ], [, ]],
            [[, ], [, ], [, ], [, ]],
            [[, ], [, ], [, ], [, ], [, ], [, ], [, ], [, ]]
        ],
        # Four
        [
            [[, ], [, ]],
            [[, ], [, ], [, ], [, ]],
            [[, ], [, ], [, ], [, ], [, ], [, ], [, ], [, ]]
        ]
    ]

    def __init__(self, type: QcaBoardType, x_even: bool, y_even: bool):
        self.board_type = type

        self.inputs_offset: list[int] = QcaUtils.getInputsOffset(type, x_even, y_even)
        self.outputs_offset: list[int] = QcaUtils.getOutputsOffset(type, x_even, y_even)

        self.inputs: list[list[QcaCell]] = [[]]
        self.outputs: list[list[QcaCell]] = [[]]



class QcaCellType(Enum):
    '''
    Types of QCA Cells
    Type ONE - inputs on left and down
    Type TWO - inputs on right and down
    Type THREE - inputs on left and up
    Type FOUR - inputs on right and up

    '''

    ONE: int = 0
    TWO: int = 1
    THREE: int = 2
    FOUR: int = 3


