import pandas as pd
from src.utils import get_top_points

#Bonus 2
def bon2():
    df = pd.read_parquet('data/output.parquet.gzip')
    print(get_top_points(df, 5, 30, 'Chile'))