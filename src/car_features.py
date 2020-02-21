"""
Inside car_features module.

In this module we will read the features of the car and return it back to
different classes, when required.
"""
import pandas as pd


class file_operations:
    """This is my docstring."""

    def __init__(self, path):
        """Initiate the path."""
        print('In init')
        self.path = path

    def get_data(self):
        """Read from file."""
        df = pd.read_csv(self.path, header=None)
        return df

    def put_data(self):
        """Write to a file."""
        self.to_csv('./data.csv')
