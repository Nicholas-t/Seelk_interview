# Repo for seelk interview (Python 3.8)

To test : 
1. download data.csv from|here](https://lengow.s3-eu-west-1.amazonaws.com/winemag-data-130k-v2.csv) (you have to rename it as _data.csv_)
2.  to initialize run : 
```
python -m venv env 
cd env/Scripts && activate
cd ../../ && pip3 install -r requirements.txt
```
3. to test, uncomment the script in __main.py__ for the desired task and run:
```
python main.py
```

**WorkFlow**
1. Skim through the questions.
2. Plan.
3. Create prototype.
4. Deploy.
5. Refactor.
6. Do last bonus question. 
7. Prettify. (Docs and Readme)

**Objective** 
1. **_(Trivial)_**
2. **Create a copy of the Dataset in a columnar format (You can choose between Parquet or ORC) and save it.**

I use the built-in function from pandas which enables me to [read](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_parquet.html) and [write](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_parquet.html) panda dataframe to parquet file.

3. **Open the columnar file from (2), and create a new "clean" dataset. i.e. containing only (id, points, price).**

Trivial. (saved under the name output_numeric.parquet.gzip)

4. **Using the columnar copy from 2, create an aggregation.**

The problem with this objective is that some of the data by country is not sufficient enough to compute the standard deviation, hence returnin NaN.
We fill the std that is Nan with 0.

**BONUS**
1. **Bonus ⭐ What are the top 5 best wines below 10 USD?**

The result I got for this can be found in bonus1.csv

2. **Bonus ⭐ What are the top 5 best wines below 30 USD from Chile 🗿?**

The result I got for this can be found in bonus2.csv

3. **Bonus ⭐ ⭐  From the clean dataset (3) create a visualisation of points vs price.**

linear fit, got constants : **a=0.031**, **b=87.330** with ax + b

4. **Bonus ⭐ ⭐ ⭐ Predict the points of a wine taking as input the price and the country (using Machine Learning).**

Because we predicting a value, it can be deduced that the ML tools we have to use is regressor (it doesnt make sense to do classification problem even though our data is somewhat discrete).

Looking at the plot from **Bonus 3** and **mean_std** plot, we know that the data is not super linear, which means it is optimal for us to use [logistic regressor](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)

In order to achieve a consistent result we will manually set the random seed.

First, I preprocessed the data to be this format:

| id | Price | Portugal | Italy | ...... |
|---|:-:|:-:|:-:|:-:|
| 1 | int | 1 | 0 | 0..|

Then just plug it into the regressor form sklearn and voila :grin:.

Summary

| Task | Done | 
|---|:-:|
| obj1 | ✔️ |
| obj2 | ✔️ |
| obj3|✔️ |
| obj4 | ✔️ |
| bon1 | ✔️ |
| bon2| ✔️ |
| bon3 | ✔️ |
| bon4 | ✔️ |

Remark:

For Bonus 4, Ofcourse we can always go one step further to deploy a neural network and it will always be an accurate prediction.

If I run the code in my computer, the output should be at least 3 folders:
original: It contains the original CSV.
cleaned: It contains the columnar files with id, points, price.
aggregated: It contains the columnar files with the aggregations.

# POST CALL

With Bonus 3 fixed, The new graph is as follows :

![Bonus3 Plot](/bonus3.png)

as we can see from the image above that it is indeed a linear relationship with the coefficient **a** to be 0.031, in an economic perspective, this means for every dollar increase in price, the points for that wine **on average** will increase by 0.031.
Although due to the high variance of the data, it is with a high probability that the actual points of the wine will not be as accurate.


![bycountry Plot](/bycountry.png)


Moreover, we can deduce a more interesting insight when we apply colors to the plot by each country.
we can definitely see that there is a trend for each country (in this case a wine that is taken from argentina is likely to be more expensive, and the wine from argentina that costs 200 are not necessarily better than the wine from Cyprus that costs much less) 


![4 countries Plot](/4countries.png)

due to these high variance across countries, I am interested in plotting the linear fit of each country, and calculating the coefficients

![4 countries Plot](/countryfit.png)
with coefficients as below
| country | a | b | 
|---|:-:|:-:|
|Portugal|3.22556817e-02 |8.74710302e+01|
|US|5.21309447e-02 |8.66597780e+01|
|Spain|4.17382009e-02 |8.61130800e+01|
|Italy|3.69249998e-02 |8.71536014e+01|
|France|1.65753342e-02 |8.80529726e+01|
|Germany|1.78297357e-02 |8.90828799e+01|
|Argentina|7.72053919e-02 |8.48180169e+01|
|Chile|5.91463257e-02 |8.52660284e+01|
|Australia|2.84832674e-02 |8.75860860e+01|
|Austria|3.55299233e-02 |8.90977835e+01|
|South Africa|6.0795763e-02| 8.6331630e+01|
|New Zealand|6.89248068e-02 |8.64521499e+01|
|Israel|4.52940177e-02 |8.70579907e+01|
|Hungary|1.32691416e-02 |8.86261495e+01|
|Greece|3.17340570e-02 |8.65787893e+01|
|Romania|5.72014921e-03 |8.63128154e+01|
|Mexico|7.23093342e-02 |8.33202857e+01|
|Canada|3.88113919e-02 |8.79918971e+01|
|Turkey|3.40395739e-02 |8.72503807e+01|
|Czech Republic|7.83669639e-02 |8.53496011e+01|
|Slovenia|5.81494624e-02 |8.65696665e+01|
|Luxembourg|-6.83229814e-02  |9.02608696e+01|
|Croatia|6.31882800e-02 |8.57439265e+01|
|Georgia|1.06590646e-02 |8.74726231e+01|
|Uruguay|5.30350272e-02 |8.53519742e+01|
|England|3.46444045e-02 |8.97602616e+01|
|Lebanon|4.84964775e-02 |8.61975652e+01|
|Serbia| 0.08541846| 85.40724763|
|Brazil|6.39195942e-02 |8.31404641e+01|
|Moldova| 0.14565957 |84.7642092 |
|Morocco|4.25079702e-03 |8.84885380e+01|
|Peru|4.44270891e-02 |8.27600357e+01|
|India| 0.33333333| 85.77777778|
|Bulgaria|7.89846124e-02 |8.67794098e+01|
|Cyprus| 0.16780045 |84.45124717|
|Armenia| 1.| 73.|
|Switzerland|3.62800353e-03 |8.82620117e+01|
|Macedonia| 0.31272727 |81.96      |

The table above is very useful for us because it gives us a direct estimation of each country from which we can deduce that **luxemburg** has the highest intercept.

For Bonus 4, I added MLP Regressor to have a comparison between linear model and neural network. From the table below, the linear regressor performs better than both logistic and MLP regressor, it adds more evidence that the relationship between prices and points is infact linear.

| Regressor | Score | 
|---|:-:|
|Linear | 0.1651652174560685 |
|Logistic | 0.16804498842209725 |
| MLP|0.3982699056516519 |



