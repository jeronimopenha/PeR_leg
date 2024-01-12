class Util(object):

    @staticmethod
    def get_lc_node(cell: int, n_lines: int, n_columns: int) -> tuple[int, int]:
        line: int = cell // n_lines
        column: int = cell % n_columns
        return line, column
