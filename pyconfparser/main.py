from typing import TextIO


class PyConfigParser:
    def __init__(self):
        self.file_content = None
        self._config = None

    def read_file(self, filename: str) -> None:
        with open(filename, 'r') as file_r:
            self.file_content = file_r.read()
