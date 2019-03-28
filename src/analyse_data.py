import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

df = pd.read_csv("../data/sgemm_preprocessed.csv")
pred_cols = df.columns[:-1]
target_col = df.columns[-1]

# Summary the data
for col in df.columns[:-1]:
    print('\n'+col+':')
    print(df[col].describe())

# Save individual plots
plt.figure(figsize=(2.5,2.5))
for col in df.columns[:-1]:
    plt.scatter(df[col], df["Run (ms)"],s=0.1,c='blue', alpha=1)
    plt.title(col)
    if df[col].describe().min() > 0:
        plt.xscale('log',basex=2)
    else:
        plt.xscale('linear')
    plt.savefig('../doc/img/'+col+'.png')
    plt.cla()
plt.close()

# Plot the data
plt.figure(figsize=(8,8))
pos=1
for col in df.columns[:-1]:
    plt.subplot(4, 4, pos)
    plt.scatter(df[col], df["Run (ms)"],s=0.1,c='blue', alpha=1)
    plt.title(col)
    if df[col].describe().min() > 0:
        plt.xscale('log',basex=2)
    else:
        plt.xscale('linear')
    pos+=1
plt.show()
