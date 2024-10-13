from pathlib import Path
import json


class Util:

    @staticmethod
    def get_project_root() -> str:
        """
        Get the root path of the project.

        Returns:
            str: The root path of the project.
        """
        path: Path = Path(__file__).parent.parent.parent.parent
        return str(path)

    @staticmethod
    def save_json(path: str, file_name: str, data):
        if path[-1] != '/':
            path = path + '/'
        with open(path + file_name + '.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
