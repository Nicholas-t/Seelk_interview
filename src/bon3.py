import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import seaborn
seaborn.set(style='ticks')

import numpy as np


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
    plt.legend()
    plt.show()

def bon3_2():
    df = pd.read_parquet('data/output_pre_numeric.parquet.gzip')
    fg = seaborn.FacetGrid(data=df, hue='country', aspect=1.61)
    fg.map(plt.scatter, 'price', 'points').add_legend()
    plt.show()