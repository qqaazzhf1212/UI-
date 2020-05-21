import yaml
import os

BasePath = os.path.dirname(__file__)
FilePath = os.path.join(BasePath, 'testconfig.yaml')


class yaml_data:
    def __init__(self):
        self.file = open(FilePath, 'r', encoding='utf-8')
        self.file_data = self.file.read()
        self.file.close()

    def data(self):
        data = yaml.load(self.file_data)
        return data


