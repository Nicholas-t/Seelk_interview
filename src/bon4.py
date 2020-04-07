import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor

countries = ['Portugal', 'US', 'Spain', 'Italy', 'France', 'Germany', 'Argentina', 'Chile',
    'Australia', 'Austria', 'South Africa', 'New Zealand', 'Israel', 'Hungary',
    'Greece', 'Romania', 'Mexico', 'Canada', 'Turkey', 'Czech Republic', 'Slovenia',
    'Luxembourg', 'Croatia', 'Georgia', 'Uruguay', 'England', 'Lebanon', 'Serbia',
    'Brazil', 'Moldova', 'Morocco', 'Peru', 'India', 'Bulgaria', 'Cyprus', 'Armenia',
    'Switzerland', 'Bosnia and Herzegovina', 'Ukraine', 'Slovakia', 'Macedonia',
    'China']



def parse(df):
    """
    pre preprocess data to be put into the linear_model.SGDRegressor
    """
    countries = df['country'].unique()
    print(countries)
    df_out = df[['points', 'price']].copy()
    print(df_out.shape)
    for index, row in df.iterrows():
        if row['country'] not in df_out.columns:
            print('new country', row['country'])
            df_out[row['country']] = 0
        df_out.loc[index,row['country']] = 1
        if index % 100 == 0:
            print(str(index)+'th row is done')
    return df_out

def preprocess():
    df = pd.read_parquet('data/output_pre_numeric.parquet.gzip')

    df = parse(df)
    df.to_parquet('data/processed_for_ML.parquet.gzip',
        compression = 'gzip')

def get_regr(simple):
    df = pd.read_parquet('data/processed_for_ML.parquet.gzip')
    global X, y
    X, y = df.drop('points', axis=1), df['points']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 2)

    print('X_train\n', X_train)
    print('y_train\n', y_train)


    print('Linear regressor ................')

    regr_lin = linear_model.LinearRegression()
    regr_lin.fit(X_train,y_train)

    print('Score', regr_lin.score(X_test, y_test))
    #print('Coeff ', regr.coef_)

    if simple :
        print('proceeding with linear regressor ....')
        return regr_lin
    print('Logistic regressor ................')
    regr_log = linear_model.LogisticRegression( random_state = 2)
    regr_log.fit(X_train,y_train)

    print('Score', regr_log.score(X_test, y_test))

    print('MLP regressor ................')
    print('ctrl+c if want to cut training')
    mlp = MLPRegressor( random_state = 2)
    mlp.fit(X_train,y_train)

    print('Score', mlp.score(X_test, y_test))


    #print('Coeff ', regr.coef_)
    print("press (1) for use linear regression, press (2) for logistic regression, and 3 for MLP Regressor")
    t = input()
    if t == "1":
        print('proceeding with linear regressor ....')
        return regr_lin
    elif t == "2":
        print('proceeding with logistic regressor ....')
        return regr_log
    elif t== "3":
        print('proceeding with MLP regressor ....')
        return mlp
    else:
        print('Bad Option. Exiting....')
        exit()

def compute(regr, country, price):
    x = [price]
    if country not in countries:
        return False
    for c in X[1:]:
        if c in countries:
            if c == country:
                x+=[1]
            else:
                x+=[0]
    return regr.predict([x])

def main(regr):
    while True:
        try:
            print('give a country')
            country = input()
            print('give a price')
            price = float(input())
            r = compute(regr, country, price)
            if not r:
                print("[UNKNOWN COUNTRY] select from "+str(countries))
            else:
                print("Predicted points will be ", r[0])
        except Exception as e:
            print('ERROR ', str(e))

def bon4(simple = False):
    regr = get_regr(simple)
    main(regr)
