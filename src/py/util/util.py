import os
from pathlib import Path
import json
from typing import List, Tuple, Dict


class Util:

    @staticmethod
    def get_project_root() -> str:
        path: Path = Path(__file__).parent.parent.parent.parent
        return str(path)

    @staticmethod
    def write_json(path: str, file_name: str, data):
        path = Util.verify_path(path)
        with open(path + file_name + '.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    @staticmethod
    def verify_path(path):
        if path[-1] != '/':
            path = path + '/'
        return path

    @staticmethod
    def get_files_list_by_extension(path: str, file_extension: str) -> List[Tuple[str, str]]:
        files_list_by_extension: List[Tuple[str, str]] = [
            (os.path.join(file_path, file_name), file_name)
            for file_path, _, filenames in os.walk(path)
            for file_name in filenames
            if os.path.splitext(file_name)[1] == file_extension
        ]
        return files_list_by_extension

    @staticmethod
    def read_json(file: str) -> Dict:
        with open(file) as p_file:
            content_dic = json.load(p_file)
        return content_dic