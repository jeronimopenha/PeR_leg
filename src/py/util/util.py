from pathlib import Path

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
