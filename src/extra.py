import pandas as pd
import matplotlib.pyplot as plt

def extra():
    df = pd.read_parquet('data/output_numeric.parquet.gzip')
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    print(df.describe())
    plt.boxplot(df["points"])
    plt.show()
    df = df[(df < (Q1 - 1.5 * IQR)) |(df > (Q3 + 1.5 * IQR))]
    print(df.shape)