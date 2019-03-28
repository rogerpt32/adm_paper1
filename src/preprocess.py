import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/sgemm_product.csv")
single_df = df.drop(columns=df.columns[[15,16,17]])
single_df = single_df.rename(index=str, columns={"Run1 (ms)": "Run2 (ms)"})
single_df = single_df.append(df.drop(columns=df.columns[[14,16,17]]),ignore_index=True)
single_df = single_df.rename(index=str, columns={"Run2 (ms)": "Run3 (ms)"})
single_df = single_df.append(df.drop(columns=df.columns[[14,15,17]]),ignore_index=True)
single_df = single_df.rename(index=str, columns={"Run3 (ms)": "Run4 (ms)"})
single_df = single_df.append(df.drop(columns=df.columns[[14,15,16]]),ignore_index=True)
single_df = single_df.rename(index=str, columns={"Run4 (ms)": "Run (ms)"})
single_df.to_csv('../data/sgemm_preprocessed.csv', sep=',', encoding='utf-8',index=False)
