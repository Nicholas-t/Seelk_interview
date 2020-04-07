import pandas as pd

#objective 4 part 1

def obj4_1():
    df = pd.read_parquet('data/output_pre_numeric.parquet.gzip')
    country = df.filter(['country'], axis=1)
    country.to_parquet('data/output_country.parquet.gzip', 
        compression = 'gzip')
    #print(country)
    #print('output_country done')

#objective 4 part 2
def obj4_2():
    df_country = pd.read_parquet('data/output_country.parquet.gzip')
    countries = df_country.country.unique()

    aggeregate = {}

    for c in countries:
        aggeregate[c] = df_country.index[df_country['country'] == c].tolist()

    df_numeric = pd.read_parquet('data/output_numeric.parquet.gzip')
    new = []

    for (country, indexes) in aggeregate.items():
        rows = df_numeric.iloc[indexes,:]
        temp = {
            'country' : country,
            'avg_points' : rows['points'].mean(axis=0),
            'sd_points' : rows['points'].std(axis=0, ddof = 0),
            'avg_price' : rows['price'].mean(axis=0),
            'sd_price' : rows['price'].std(axis=0, ddof = 0)
        }
        new += [temp]
    #print(str(len(new))+' countries aggeregated')
    df_new = pd.DataFrame(new)
    #print(df_new)
    df_new.to_parquet('data/output_avg_std.parquet.gzip', 
        compression = 'gzip') 

def obj4():
    obj4_1()
    obj4_2()