from typing import Dict


class KeyValueStorage:
    builtins_attr = [
        '__dict__',
        '__doc__',
        '__name__',
        '_module__',
        '__bases__'
    ]

    def __init__(self, path_to_file: str):
        storage_dictionary = self.file_to_dict(path_to_file)
        for key, value in storage_dictionary.items():
            self.__setattr__(key, value)
            self.__setitem__(key, value)

    def file_to_dict(self, path_to_file) -> Dict:
        storage_dictionary = {}
        with open(path_to_file) as file:
            for line in file:
                key, value = line.strip().split('=')
                if self.check_key_is_string(key):
                    self.value_converter(value)
                    storage_dictionary[key] = value
        return storage_dictionary

    def __setattr__(self, key, value):
        if self.check_key_is_not_built_in(key):
            super().__setattr__(key, value)

    def __setitem__(self, key, value):
        if self.check_key_is_not_built_in(key):
            self.__dict__[key] = value

    def __getitem__(self, item):
        return self.__dict__[item]

    @staticmethod
    def check_key_is_string(key):
        if not isinstance(key, str) or key.isdigit():
            raise ValueError('Key should be string')
        else:
            return True

    @staticmethod
    def value_converter(value):
        return int(value) if value.isdigit() else value

    def check_key_is_not_built_in(self, key):
        return True if key not in self.builtins_attr else False
