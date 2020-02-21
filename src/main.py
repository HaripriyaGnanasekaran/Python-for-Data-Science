from car_features import file_operations


path = 'https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data'
file_instance = file_operations(path)
data_frame_instance = file_instance.get_data()
print(data_frame_instance.head())
