import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import seaborn
seaborn.set(style='ticks')

import numpy as np

countries = ['Portugal', 'US', 'Spain', 'Italy', 'France', 'Germany', 'Argentina', 'Chile',
    'Australia', 'Austria', 'South Africa', 'New Zealand', 'Israel', 'Hungary',
    'Greece', 'Romania', 'Mexico', 'Canada', 'Turkey', 'Czech Republic', 'Slovenia',
    'Luxembourg', 'Croatia', 'Georgia', 'Uruguay', 'England', 'Lebanon', 'Serbia',
    'Brazil', 'Moldova', 'Morocco', 'Peru', 'India', 'Bulgaria', 'Cyprus', 'Armenia',
    'Switzerland', 'Bosnia and Herzegovina', 'Ukraine', 'Slovakia', 'Macedonia',
    'China']

def func(x, a, b):
    return a*x + b

#Bonus 3
def bon3(fit = False, color = True):
    df = pd.read_parquet('data/output_pre_numeric.parquet.gzip')

    plt.plot(df['price'], df['points'], 'bo', label='data')
    if fit:
        x_fit = np.arange(min(df['price']),400, 0.1)
        print('Doing Fitting')
        popt, pcov = curve_fit(func, df['price'],df['points'])
        plt.plot(x_fit, func(x_fit, *popt), 'r', label='using linear fit  (%5.3f) x + (%5.3f)' % tuple(popt))
    plt.xlabel('price')
    plt.ylabel('points')
    plt.title('price vs points')
    plt.legend(prop={'size': 1})
    plt.show()

def bon3_2():
    df = pd.read_parquet('data/output_pre_numeric.parquet.gzip')
    fg = seaborn.FacetGrid(data=df, hue='country', aspect=1.61)
    fg.map(plt.scatter, 'price', 'points').add_legend()
    plt.show()

def bon3_3():
    df = pd.read_parquet('data/output_pre_numeric.parquet.gzip')
    for c in countries:
        try:
            _df = df[df['country'] == c]
            x_fit = np.arange(min(_df['price']),max(_df['price']), 0.1)
            popt, pcov = curve_fit(func, _df['price'],_df['points'])
            print(c, popt, np.mean(_df['points']), np.mean(_df['price']), np.std(_df['points']), np.std(_df['price']), _df.shape[0])
            plt.plot(x_fit, func(x_fit, *popt), label=c)
        except Exception as e:
            print(c, ' Failed to plot')
    plt.xlabel('price')
    plt.ylabel('points')
    plt.title('linear fit of each country')
    plt.legend()
    plt.show()