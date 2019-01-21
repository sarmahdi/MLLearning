# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 10:52:31 2018

@author: syedm
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# import the dataset
dataset =  pd.read_csv('Data.csv')
X = dataset.iloc[:,:-1].values
Xtransformed = dataset.iloc[:,:-1].values
y = dataset.iloc[:,3].values

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0 )
imputer.fit(X[:,1:3])# upper bound is ignored. 

Xtransformed[:, 1:3 ] = imputer.transform(X[:, 1:3 ])

# Encoding Categorical data
from sklearn.preprocessing  import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
Xtransformed[:, 0] = labelencoder_X.fit_transform(Xtransformed[:, 0])
onehotencoder =  OneHotEncoder(categorical_features = [0])
XHT= onehotencoder.fit_transform(Xtransformed).toarray()

labelencoder_y = LabelEncoder()
yht = labelencoder_y.fit_transform(y)



datasetWithDummies = pd.get_dummies(dataset)
XWithDummies = datasetWithDummies.iloc[:,:-1].values
imputer.fit(XWithDummies[:,1:3])# upper bound is ignored.
XwDNantransformed= XWithDummies
XwDNantransformed[:, 1:3 ] = imputer.transform(XWithDummies[:, 1:3 ])


data = pd.read_csv('Data.csv')

X1 = data.drop(columns='Purchased')

y1 = data['Purchased']

#Then during the categorical encoding, it's as easy as:

X1 = pd.get_dummies(data=X1)
XnonNaned=X1.fillna(X1.mean())
#imputer2 = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0 )
##imputer2.fit(X1[:,1:4])# upper bound is ignored. 
#imputer2.transform(data[:,1:4])