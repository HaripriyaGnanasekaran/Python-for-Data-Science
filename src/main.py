"""
Main module.

This program attempts to predict the price of a car using machine learning.
Data of used cars along with its attributes like speed, mileage are provided
as a training set. Multiple linear regression is used over chosen primary
components that directly correlates with the price of the car. Model is later
used to predic the price of test set. Model is evaluated and cross validated.
"""
from car_features import file_operations


path = 'https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data'
file_instance = file_operations(path)
data_frame_instance = file_instance.get_data()
print(data_frame_instance.head())
