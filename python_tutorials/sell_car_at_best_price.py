"""
This is a python public module to predict the best selling price for used cars.

However, we are still currently working on the module.
"""
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys
from sklearn.linear_model import LinearRegression

print(sys.version)
# import sales car data here.

print("Importing data from the website")
path = 'https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data'
df = pd.read_csv(path, header=None)
header = ['symboling', 'normalized-losses', 'make', 'fuel-type', 'aspiration',
          'number-of-doors', 'body-style', 'drive-wheels', 'engine-location',
          'wheel-base', 'length', 'width', 'height', 'curb-weight',
          'engine-type', 'number-of-cylinders', 'engine-size', 'feul-system',
          'bore', 'stroke', 'compression-ration', 'horsepower', 'peak-rpm',
          'city-mpg', 'highway-mpg', 'price']
df.columns = header

# data preparation
df.replace('?', np.NaN, inplace=True)
df.dropna(axis=0, inplace=True)
df.reset_index(drop=True, inplace=True)
df[['price', 'normalized-losses', 'bore', 'stroke', 'horsepower', 'peak-rpm']
   ] = df[['price', 'normalized-losses', 'bore', 'stroke', 'horsepower',
           'peak-rpm']].astype(float)


# data normalizations.

# convert miles per gallon to liters per km
df['city-mpg'] = 0.425144*df['city-mpg']
df['highway-mpg'] = 0.425144*df['highway-mpg']
df.rename(columns={'city-mpg': 'city-kpl'}, inplace=True)
df.rename(columns={'highway-mpg': 'highway-kpl'}, inplace=True)

# min-max normalizations
df['length'] = (df['length']-df['length'].min()) / \
    (df['length'].max()-df['length'].min())
df['length'] = (df['width']-df['width'].min()) / \
    (df['width'].max()-df['width'].min())
df['height'] = (df['height']-df['height'].min()) / \
    (df['height'].max()-df['height'].min())

# data Visualization
# plt.hist(x=df['price'], bins=3)
# plt.show()
# plt.title = 'Scatter plot of Drive wheel location vs the Price.'
# plt.xlabel = 'Drive Wheels'
# plt.ylabel = 'Price'
# sns.boxplot(x='drive-wheels', y='price', data=df)
# plt.show()

# plt.title = 'Scatter plot of Engine size vs the Price.'
# plt.xlabel = 'Engine Size'
# plt.ylabel = 'Price'
# plt.scatter(x=df['engine-size'], y=df['price'])
# plt.show()

# group data and make heat plot
# dfgrp = df[['drive-wheels', 'body-style', 'price']]
# dfgrp = dfgrp.groupby(['drive-wheels', 'body-style'], as_index=False).mean()
# dfpiv = dfgrp.pivot(index='drive-wheels', columns='body-style')
# fig, ax = plt.subplots(figsize=(10, 10))
# sns.heatmap(dfpiv, cmap='RdBu', annot=True, ax=ax)
# plt.show()

# sns.regplot(x='highway-kpl', y='price', data=df)
# plt.ylim(0,)
# plt.show()

# explorative data analysis
statistics = df.describe()
statistics.to_csv('./descriptivestatistics.csv')
drivewheel = df['drive-wheels'].value_counts()
dwdf = pd.DataFrame(drivewheel)
dwdf.rename(columns={'drive-wheels': 'value-counts'}, inplace=True)

correlationmatrix = df.corr()
fig, ax = plt.subplots()
sns.heatmap(correlationmatrix, cmap='RdYlGn_r', ax=ax)
fig.savefig('./assets/figure_6.png')

# Model development
"""
Simple, multiple, polynomial linear regression can be used.
"""

lm = LinearRegression()
lm.fit(df[["highway-kpl"]], df[['price']])

prd = pd.DataFrame({'kpl': [12]})
Yhat = lm.predict(prd[["kpl"]])
print(Yhat)
print(df['highway-kpl'].head(10))
print(df['price'].head(10))
