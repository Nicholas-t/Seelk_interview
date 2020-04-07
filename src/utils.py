import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#pre_numeric is here to avoid index issues
def create_pre_numeric():
    numeric = ['id', 'points', 'price', 'country']
    df = pd.read_parquet('data/output.parquet.gzip')
    df_clean = df.filter(numeric, axis=1).dropna().reset_index()
    df_clean.to_parquet('data/output_pre_numeric.parquet.gzip', 
        compression = 'gzip')

    #print('prenumeric done')
    #print(df_clean)

def get_top_points(df, n, below = 0, country=''):
    if country != '':
        df = df[df['country'] == country]
    if below != 0:
        df = df[df['price'] <= below]
    return df.sort_values('points', ascending = False).head(n)

#SHOW mean and std
def plot_mean_std():
    df = pd.read_parquet('data/output_numeric.parquet.gzip')
    X = df['points'].unique()
    data = {}
    for index, row in df.iterrows():
        if row['points'] not in data.keys():
            data[row['points']] = []
        data[row['points']] += [df.loc[index, 'price']]
    plt.errorbar(data.keys(), [np.mean(data[k]) for k in data.keys()], [np.std(data[k]) for k in data.keys()],  linestyle='None', marker='^')
    plt.show()
