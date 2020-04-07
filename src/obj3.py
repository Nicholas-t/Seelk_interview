import pandas as pd
from src.utils import mkdir
#objective 3 
#pre_numeric is here to avoid index issues


def obj3(save):
    numeric = ['id', 'points', 'price']
    df = pd.read_parquet('data/output.parquet.gzip')
    df_clean = df.filter(numeric, axis=1).dropna().reset_index()
    df_clean.to_parquet('data/output_numeric.parquet.gzip', 
        compression = 'gzip')
    if (save):
        mkdir('clean')
        df_clean.to_parquet('clean/output_numeric.parquet.gzip', 
            compression = 'gzip')
        print('folder "clean" created')
    #print('numeric done')
    #print(df_clean)
