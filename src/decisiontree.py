import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model,tree
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# Load the dataset
df = pd.read_csv("../data/sgemm_preprocessed.csv")

# Split in train and test
x_train, x_test, y_train, y_test = train_test_split(df[df.columns[:-1]], df['Run (ms)'], test_size=0.25, random_state=42)

# Train the model
regr = tree.DecisionTreeRegressor(random_state = 32)
regr_5 = tree.DecisionTreeRegressor(random_state = 32,max_depth=5)
regr.fit(x_train, y_train)
regr_5.fit(x_train, y_train)

#tree.export_graphviz(regr,out_file='tree.dot') # warning this might be a big file
tree.export_graphviz(regr_5,out_file='tree5.dot')

print('Regressor without restrictions')

# Prediction train
y_train_pred = regr.predict(x_train)
# Prediction test
y_pred = regr.predict(x_test)

print("Max Depth: %d"%regr.tree_.max_depth)
print("Node Count: %d"% regr.tree_.node_count)

print("Mean squared error (train): %.2f"
      % mean_squared_error(y_train, y_train_pred))
print('Variance score (train): %.2f' % r2_score(y_train, y_train_pred))

print("Mean squared error (test): %.2f"
      % mean_squared_error(y_test, y_pred))
print('Variance score (test): %.2f' % r2_score(y_test, y_pred))

print('\nRegressor with max depth 5')

# Prediction train
y_train_pred = regr_5.predict(x_train)
# Prediction test
y_pred = regr_5.predict(x_test)

print("Max Depth: %d"%regr_5.tree_.max_depth)
print("Node Count: %d"% regr_5.tree_.node_count)

print("Mean squared error (train): %.2f"
      % mean_squared_error(y_train, y_train_pred))
print('Variance score (train): %.2f' % r2_score(y_train, y_train_pred))

print("Mean squared error (test): %.2f"
      % mean_squared_error(y_test, y_pred))
print('Variance score (test): %.2f' % r2_score(y_test, y_pred))
