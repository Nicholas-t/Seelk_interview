import pandas as pd

# objective 2 
# convert csv to parquet
def obj2():
    df = pd.read_csv('data/data.csv')
    df.to_parquet('data/output.parquet.gzip', 
        compression = 'gzip')

#print(df)