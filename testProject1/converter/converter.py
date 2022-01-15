from converter.mixins import JsonConverterMixin, YamlConverterMixin


__all__ = ['Converter']


class Converter(JsonConverterMixin, YamlConverterMixin):
    def __init__(self, path: str):
        super().__init__()
        # если можно использовать os
        # self.root = os.path.splitext(os.path.basename(path))[0]
        self._path = path
        self._root = self.get_base_filename()
        self._output_format = None
        self.read_file()

    def read_file(self):
        with open(self._path, 'r') as f:
            names = list(f.readline().split(','))
            self._output_format = names.pop().strip()
            self._names = names
            data = []
            rows = f.read().split('\n')
            for row in rows:
                list_row = row.split(',')
                if len(list_row) != len(names):
                    raise ValueError("Incorrect format of csv file")
                data.append(list_row)
            self._data = data

    def get_base_filename(self) -> str:
        index1 = self._path.rfind('\\')
        if index1 == -1:
            index1 = self._path.rfind('/')
        return self._path[index1 + 1:self._path.rfind('.')]

    def get_file(self):
        if self._output_format == 'json':
            new_data = self._convert_to_json()
        elif self._output_format == 'yaml':
            new_data = self._convert_to_yaml()
        else:
            raise ValueError("Incorrect convert format")
        with open(f'{self._root}.{self._output_format}', 'w') as f:
            f.write(new_data)
