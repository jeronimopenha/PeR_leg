from pathlib import Path
import json


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
