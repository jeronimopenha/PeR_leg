import os


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

    @staticmethod
    def get_distance_table(cells_sqrt: int) -> list[list]:
        distance_tale_tmp: list[list] = [[] for i in range((cells_sqrt - 1) * 2)]
        distance_tale: list[list] = []
        for i in range(cells_sqrt):
            for j in range(cells_sqrt):
                if j == i == 0:
                    continue
                d: int = i + j
                if [i, j] not in distance_tale_tmp[d - 1]:
                    distance_tale_tmp[d - 1].append([i, j])
                if [i, -j] not in distance_tale_tmp[d - 1]:
                    distance_tale_tmp[d - 1].append([i, -j])
                if [-i, -j] not in distance_tale_tmp[d - 1]:
                    distance_tale_tmp[d - 1].append([-i, -j])
                if [-i, j] not in distance_tale_tmp[d - 1]:
                    distance_tale_tmp[d - 1].append([-i, j])
        for d in range(len(distance_tale_tmp)):
            for p in distance_tale_tmp[d]:
                distance_tale.append(p)

        return distance_tale

    @staticmethod
    def get_cell_from_line_column(cell_line: int, cell_column: int, n_lines: int) -> int:
        cell: int = cell_line * n_lines + cell_column

        return cell

    @staticmethod
    def get_files_list_by_extension(path: str, extension: str) -> list[list]:
        dots_path_list = [[os.path.join(path, name), name] for name in os.listdir(path)]
        files_list = [file for file in dots_path_list if os.path.isfile(file[0])]
        files_list_by_extension = [arq for arq in files_list if arq[0].lower().endswith(extension)]
        return files_list_by_extension
