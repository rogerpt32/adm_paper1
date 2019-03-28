import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# Load the dataset
df = pd.read_csv("../data/sgemm_preprocessed.csv")

# Split in train and test
x_train, x_test, y_train, y_test = train_test_split(df[df.columns[:-1]], df['Run (ms)'], test_size=0.1, random_state=32)

# Train the model
regr = linear_model.LinearRegression()
regr.fit(x_train, y_train)

# Prediction train
y_train_pred = regr.predict(x_train)
# Prediction test
y_pred = regr.predict(x_test)

# The coefficients
print('Coefficients: \n', regr.coef_)

print("Mean squared error (train): %.2f"
      % mean_squared_error(y_train, y_train_pred))
print('Variance score (train): %.2f' % r2_score(y_train, y_train_pred))

print("Mean squared error (test): %.2f"
      % mean_squared_error(y_test, y_pred))
print('Variance score (test): %.2f' % r2_score(y_test, y_pred))

for i in range(10):
      print(np.array(y_test)[i],y_pred[i])
