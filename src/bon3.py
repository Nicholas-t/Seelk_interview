import pandas as pd
import matplotlib.pyplot as plt

import numpy as np

#Bonus 3
def bon3(lin_fit = False):
    df = pd.read_parquet('data/output_numeric.parquet.gzip')
    plt.scatter(df['points'], df['price'])
    plt.xlabel('points')
    plt.ylabel('price')
    if lin_fit:
        print('Doing Linear Fit')
        F, A = np.polyfit(df['points'],df['price'], 1)
        plt.plot(df['points'], np.log(F*df['points']+A), label = "linear fit")
    plt.show()