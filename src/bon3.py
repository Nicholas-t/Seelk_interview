import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

import numpy as np


def func(x, a, b, c):
    return a*np.exp(b*x)/c

#Bonus 3
def bon3(fit = False):
    df = pd.read_parquet('data/output_numeric.parquet.gzip')
    plt.plot(df['points'], df['price'], 'bo', label='data')
    if fit:
        x_fit = np.arange(min(df['points']), max(df['points']), 0.1)
        print('Doing Fitting')
        popt, pcov = curve_fit(func, df['points'],df['price'])
        plt.plot(x_fit, func(x_fit, *popt), 'r', label='curve fit constants a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))
    plt.xlabel('points')
    plt.ylabel('price')
    plt.title('points vs price')
    plt.legend()
    plt.show()