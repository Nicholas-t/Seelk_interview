import pandas as pd
from src.utils import mkdir


#objective 4 part 1
def obj4_1():
    df = pd.read_parquet('data/output_pre_numeric.parquet.gzip')
    country = df.filter(['country'], axis=1)
    country.to_parquet('data/output_country.parquet.gzip', 
        compression = 'gzip')
    #print(country)
    #print('output_country done')

#objective 4 part 2
def obj4_2(save):
    df_country = pd.read_parquet('data/output_country.parquet.gzip')
    countries = df_country.country.unique()
    country_indexes = {}
    for c in countries:
        country_indexes[c] = df_country.index[df_country['country'] == c].tolist()
    df_numeric = pd.read_parquet('data/output_numeric.parquet.gzip')
    new = []
    for (country, indexes) in country_indexes.items():
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
    if save:
        mkdir('aggeregated')
        df_new.to_parquet('aggeregated/output_avg_std.parquet.gzip', 
        compression = 'gzip') 
        print('folder "aggeregated" created')

def obj4(save):
    obj4_1()
    obj4_2(save)