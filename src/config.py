import yaml


class Config:
    """
    A class to read YAML configuration file
    """

    def __init__(self, filepath):
        self.filepath = filepath

    def read(self):
        """
        Reads project configurations
        :return: all project configurations
        """
        with open(self.filepath) as stream:
            return yaml.safe_load(stream)
