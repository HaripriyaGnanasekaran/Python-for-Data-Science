"""
Inside CarFeatures module.

In this module we will read the features of the car and return it back to
different classes, when required.
"""
import pandas as pd


class CarFeatures:
    """This is my docstring."""

    def __init__(self, path):
        """Initiate the path."""
        print('In init')
        self.path = path

    def data(self):
        """Read from file."""
        df = pd.read_csv(self.path, header=None)
        return df

    def write(self):
        """Write to a file."""
        self.to_csv('./data.csv')
