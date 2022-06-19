from ctypes import Union
from typing import TextIO


class PyConfigParser:
    def __init__(self):
        self.file_content = None
        self._config = None

    def _parser(self) -> None:
        file_lines = self.file_content.split('\n')

        current_section = None
        file_config = {}

        for line in file_lines:
            line = line.strip()

            if len(line) > 0:
                # if is a section
                if line.endswith(':'):
                    section_name = line.replace(':', '')
                    current_section = section_name
                    file_config[section_name] = {}
                elif '=' in line:  # if is a option
                    option, value = line.split('=')
                    option = option.strip()
                    value = value.strip()

                    if not current_section:
                        file_config[option] = value
                    else:
                        file_config[current_section][option] = value

        self._config = file_config

    def read_file(self, filename: str) -> None:
        with open(filename, 'r') as file_r:
            self.file_content = file_r.read()

        self._parser()

    def read_string(self, string: str) -> None:
        self.file_content = string
        self._parser()

    def __getitem__(self, item: str) -> str:
        return self._config[item]


if __name__ == '__main__':
    parser = PyConfigParser()
    parser.read_file('config.txt')

    print(parser['project']['name'])
