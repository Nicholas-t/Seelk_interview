import pandas as pd

#objective 3 
#pre_numeric is here to avoid index issues


def obj3():
    numeric = ['id', 'points', 'price']
    df = pd.read_parquet('data/output.parquet.gzip')
    df_clean = df.filter(numeric, axis=1).dropna().reset_index()
    df_clean.to_parquet('data/output_numeric.parquet.gzip', 
        compression = 'gzip')

    #print('numeric done')
    #print(df_clean)
