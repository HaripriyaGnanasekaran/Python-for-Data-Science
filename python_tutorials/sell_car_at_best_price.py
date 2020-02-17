import seaborn as sbn
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys


# import sales car data here.

print("Importing data from the website")
path = 'https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data'
df = pd.read_csv(path, header=None)
header = ['symboling', 'normalized-losses', 'make', 'fuel-type', 'aspiration',
          'number-of-doors', 'body-style', 'drive-wheels', 'engine-location',
          'wheel-base', 'length', 'width', 'height', 'curb-weight', 'engine-type',
          'number-of-cylinders', 'engine-size', 'feul-system', 'bore', 'stroke',
          'compression-ration', 'horsepower', 'peak-rpm', 'city-mpg', 'highway-mpg',
          'price']
df.columns = header

# data preparation
df.replace('?', np.NaN, inplace=True)
df.dropna(axis=0, inplace=True)
df.reset_index(drop=True, inplace=True)
df[['price', 'normalized-losses', 'bore', 'stroke', 'horsepower', 'peak-rpm']
   ] = df[['price', 'normalized-losses', 'bore', 'stroke', 'horsepower', 'peak-rpm']].astype(float)


# data normalizations.
df['city-mpg'] = 235/df['city-mpg']  # converts miles per gallon to liter per 100km
df.rename(columns={'city-mpg': 'city-lp100km'}, inplace=True)
df['length'] = (df['length']-df['length'].min())/(df['length'].max()-df['length'].min())
df['length'] = (df['width']-df['width'].min())/(df['width'].max()-df['width'].min())
df['height'] = (df['height']-df['height'].min())/(df['height'].max()-df['height'].min())

# data Visualization
# plt.hist(x=df['price'], bins=3)
# plt.show()
