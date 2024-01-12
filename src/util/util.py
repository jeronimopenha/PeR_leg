class Util(object):

    @staticmethod
    def get_line_column_cell_sqr(cell: int, cells_sqrt: int) -> tuple[int, int]:
        return Util.get_line_column_cell(cell, cells_sqrt, cells_sqrt)

    @staticmethod
    def get_line_column_cell(cell: int, n_lines: int, n_columns: int) -> tuple[int, int]:
        line: int = cell // n_lines
        column: int = cell % n_columns
        return line, column
