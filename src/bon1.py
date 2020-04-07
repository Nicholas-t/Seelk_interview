import pandas as pd
from src.utils import get_top_points
#Bonus 1
def bon1():
    df = pd.read_parquet('data/output.parquet.gzip')
    return get_top_points(df, 5, 10)