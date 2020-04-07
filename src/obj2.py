import pandas as pd
from src.utils import mkdir

# objective 2 
# convert csv to parquet
def obj2(save):
    df = pd.read_csv('data/data.csv')
    df.to_parquet('data/output.parquet.gzip', 
        compression = 'gzip')
    if save:
        mkdir('original')
        df.to_parquet('original/output.parquet.gzip', 
            compression = 'gzip')
        print('folder "original" created')

#print(df)