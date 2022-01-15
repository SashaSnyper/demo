__all__ = ['JsonConverterMixin', 'YamlConverterMixin']


class BaseConverterMixin:
    def __init__(self):
        self._root = None
        self._data = None
        self._names = None


class JsonConverterMixin(BaseConverterMixin):
    def _convert_to_json(self) -> str:
        output = f'{{\n\t"{self._root}": ['
        for row in self._data:
            output += "{\n"
            for name, el in zip(self._names, row):
                output += f'\t\t"{name}": "{el}",\n'
            output = output.rstrip(',\n')
            output += "\n\t}, "
        output = output.rstrip(', ')
        output += "]\n}"
        return output


class YamlConverterMixin(BaseConverterMixin):
    def _convert_to_yaml(self) -> str:
        output = f'{self._root}:\n'
        for row in self._data:
            output += "  -\n"
            for name, el in zip(self._names, row):
                output += f'\t{name}: "{el}"\n'
        return output
