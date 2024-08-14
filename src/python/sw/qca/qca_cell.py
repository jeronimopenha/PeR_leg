from enum import Enum, auto

from src.python.sw.qca.qca_types import QcaCellType


class QcaCell:

    def __init__(self, cell_type: QcaCellType, max_dist: int = 3):
        self.cell_type: QcaCellType = cell_type
        self.max_dist: int = max_dist
        self.inputs: list[list[QcaCellType, list[int]]] = self.get_inputs()
        self.outputs: list[list[QcaCellType, list[int]]] = self.get_outputs()

    def get_inputs(self) -> list[list[QcaCellType, list[int]]]:
        return self.io_logic(self.get_previous_cells)

    def get_outputs(self) -> list[list[QcaCellType, list[int]]]:
        return self.io_logic(self.get_next_cells)

    def io_logic(self, function) -> list[list[QcaCellType, list[int]]]:
        vec_cells = [[]for _ in range(self.max_dist)]
        cells_queue = []

        cells_to_queue = function(self.cell_type)
        for c in cells_to_queue:
            c.append(1)

        cells_queue.extend(cells_to_queue)

        while cells_queue:
            cell = cells_queue.pop(0)
            vec_cells[cell[2]-1].append(cell[:-1])

            if cell[2] + 1 > self.max_dist:
                continue

            cells_to_queue = function(cell[0])
            for c in cells_to_queue:
                c[1][0] += cell[1][0]
                c[1][1] += cell[1][1]
                c.append(cell[2] + 1)

            cells_queue.extend(cells_to_queue)
        return vec_cells

    def get_previous_cells(self, cell_type: QcaCellType) -> list[list[QcaCellType, list[int]]]:
        """
        Cells line,column offsets

        Type ONE - inputs on left and down
        Type TWO - inputs on right and down
        Type THREE - inputs on left and up
        Type FOUR - inputs on right and up

        Cells of type ONE always connects to cells of type THREE and TWO 
        Cells of type TWO always connects to cells of type FOUR and ONE
        Cells of type THREE always connects to cells of type ONE and FOUR
        Cells of type FOUR always connects to cells of type TWO and THREE

        """

        if cell_type == QcaCellType.ONE:
            return [
                [QcaCellType.THREE, [0, -1]],
                [QcaCellType.TWO, [1, 0]]
            ]
        elif cell_type == QcaCellType.TWO:
            return [
                [QcaCellType.FOUR, [0, 1]],
                [QcaCellType.ONE, [1, 0]]
            ]

        elif cell_type == QcaCellType.THREE:
            return [
                [QcaCellType.ONE, [0, -1]],
                [QcaCellType.FOUR, [-1, 0]]
            ]
        else:
            return [
                [QcaCellType.TWO, [0, 1]],
                [QcaCellType.THREE, [-1, 0]]
            ]

    def get_next_cells(self, cell_type: QcaCellType) -> list[list[QcaCellType, list[int]]]:
        """
        Cells line,column offsets

        Type ONE - outputs on right and up
        Type TWO - outputs on left and up
        Type THREE - outputs on right and down
        Type FOUR - outputs on left and down

        Cells of type ONE always connects to cells of type THREE and TWO
        Cells of type TWO always connects to cells of type FOUR and ONE
        Cells of type THREE always connects to cells of type ONE and FOUR
        Cells of type FOUR always connects to cells of type TWO and THREE

        """

        if cell_type == QcaCellType.ONE:
            return [
                [QcaCellType.THREE, [0, 1]],
                [QcaCellType.TWO, [-1, 0]]
            ]
        elif cell_type == QcaCellType.TWO:
            return [
                [QcaCellType.FOUR, [0, -1]],
                [QcaCellType.ONE, [-1, 0]]
            ]

        elif cell_type == QcaCellType.THREE:
            return [
                [QcaCellType.ONE, [0, 1]],
                [QcaCellType.FOUR, [1, 0]]
            ]
        else:
            return [
                [QcaCellType.TWO, [0, -1]],
                [QcaCellType.THREE, [1, 0]]
            ]
