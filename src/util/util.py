class Util(object):

    @staticmethod
    def get_line_column_list_sqrt(cells: list, cells_sqrt: int) -> list[tuple[int, int]]:
        return Util.get_line_column_list(cells, cells_sqrt, cells_sqrt)

    @staticmethod
    def get_line_column_list(cells: list, n_lines: int, n_columns: int) -> list[tuple[int, int]]:
        line_column_list: list = []
        for cell in cells:
            line_column_list.append(Util.get_line_column_cell(cell, n_lines, n_columns))
        return line_column_list

    @staticmethod
    def get_line_column_cell_sqrt(cell: int, cells_sqrt: int) -> tuple[int, int]:
        return Util.get_line_column_cell(cell, cells_sqrt, cells_sqrt)

    @staticmethod
    def get_line_column_cell(cell: int, n_lines: int, n_columns: int) -> tuple[int, int]:
        line: int = cell // n_lines
        column: int = cell % n_columns
        return line, column
