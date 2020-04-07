import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

#create pre_numeric parquet to avoid index issues from pandas
def create_pre_numeric():
    numeric = ['id', 'points', 'price', 'country']
    df = pd.read_parquet('data/output.parquet.gzip')
    df_clean = df.filter(numeric, axis=1).dropna().reset_index()
    df_clean.to_parquet('data/output_pre_numeric.parquet.gzip', 
        compression = 'gzip')
    #print('prenumeric done')
    #print(df_clean)

# helper function for bonus 1 and 2
def get_top_points(df, n, below = 0, country=''):
    if country != '':
        df = df[df['country'] == country]
    if below != 0:
        df = df[df['price'] <= below]
    return df.sort_values('points', ascending = False).head(n)

#plot mean and std price and index
def plot_mean_std():
    df = pd.read_parquet('data/output_numeric.parquet.gzip')
    X = df['price'].unique()
    data = {}
    for index, row in df.iterrows():
        if row['price'] not in data.keys():
            data[row['price']] = []
        data[row['price']] += [df.loc[index, 'points']]
    plt.xlabel('price')
    plt.ylabel('points')
    plt.title('price vs points (Mean and std)')
    plt.errorbar(data.keys(), [np.mean(data[k]) for k in data.keys()], [np.std(data[k]) for k in data.keys()],  linestyle='None', marker='^')
    plt.show()

def plot_by_country(countries = ['Portugal', 'Italy', 'China','Chile']):
    figure, axes = plt.subplots(nrows=2, ncols=2)
    df = pd.read_parquet('data/output_pre_numeric.parquet.gzip')
    _df = df[df['country'] == countries[0]]
    axes[0,0].scatter(_df['price'], _df['points'])
    _df = df[df['country'] == countries[1]]
    axes[0,1].scatter(_df['price'], _df['points'])
    _df = df[df['country'] == countries[2]]
    axes[1,0].scatter(_df['price'], _df['points'])
    _df = df[df['country'] == countries[3]]
    axes[1,1].scatter(_df['price'], _df['points'])
    plt.show()


# helper function to create folder
def mkdir(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)