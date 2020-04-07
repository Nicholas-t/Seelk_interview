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

due to these high variance across countries, I am interested in plotting the linear fit of each country, and calculate their respective coefficients

![4 countries Plot](/countryfit.png)
with coefficients as below

| country | a | b | mean(points) | mean(price) | std(points) | std(price)| count|
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|all|X|X|88.42172251811175| 35.36864434814251 |3.0449292865354667| 41.03088269256777| 120916|
|Portugal |3.22556817e-02| 8.74710302e+01 |88.31671794871795 |26.21825641025641| 3.0165692004261886 |41.171017376689754 |4875|
|US |5.21309447e-02| 8.66597780e+01 |88.56638717405326 |36.5734635584631| 3.1167966950633086 |27.08860780408873 |54265|
|Spain |4.17382009e-02| 8.61130800e+01 |87.29073482428115 |28.215274608245853| 3.070682264757081 |34.65976066047531| 6573|
|Italy |3.69249998e-02| 8.71536014e+01 |88.61818611800875 |39.663769658271256| 2.6607061276429067 |38.05135441456322 |16914|
|France |1.65753342e-02| 8.80529726e+01 |88.73486723672367 |41.139120162016205| 3.012887011852634 |73.76732925660606 |17776|
|Germany |1.78297357e-02| 8.90828799e+01 |89.83632075471698 |42.25754716981132| 2.4728910685145538 |62.84548053895604| 2120|
|Argentina |7.72053919e-02| 8.48180169e+01 |86.71033013844516 |24.510117145899894| 3.183374977729781 |23.427002476505614| 3756|
|Chile |5.91463257e-02| 8.52660284e+01 |86.49547101449275 |20.786458333333332| 2.7001370998257648 |21.926887892214815| 4416|
|Australia |2.84832674e-02| 8.75860860e+01 |88.59546643417612 |35.43766346992153| 2.996117281874334 |49.038766339813876| 2294|
|Austria |3.55299233e-02|**8.90977835e+01**|**90.19078242229368** |30.76277241872097| 2.4618650715990227 |27.21993364688152| 2799|
|South Africa |6.0795763e-02| 8.6331630e+01 |87.83139984532096 |24.668986852281517| 2.344506202167755 |21.8346157686354| 1293|
|New Zealand |**6.89248068e-02**| 8.64521499e+01 |88.30841799709724 |26.93178519593614| 2.4346200341366413 |17.094877134514157| 1378|
|Israel |4.52940177e-02| 8.70579907e+01 |88.49693251533742 |31.768916155419223| 2.47533658398909 |18.8789539677192 |489|
|Hungary |1.32691416e-02| 8.86261495e+01 |89.1655172413793 |40.648275862068964| 2.6678515005549093 |69.21117420589238 |145|
|Greece |3.17340570e-02| 8.65787893e+01 |87.2885032537961 |22.364425162689805| 2.1908056082439304 |10.599264961690995 |461|
|Romania |5.72014921e-03| 8.63128154e+01 |86.4 |15.241666666666667| 1.709775813764288 |30.160403355319296 |120|
|Mexico |7.23093342e-02| 8.33202857e+01 |85.25714285714285 |26.785714285714285| 2.702832980864519 |17.62781313488339| 70|
|Canada |3.88113919e-02| 8.79918971e+01 |89.37795275590551 |35.71259842519685| 2.390694340738452 |19.61941225782961 |254|
|Turkey |3.40395739e-02| 8.72503807e+01 |88.08888888888889 |24.633333333333333| 1.964374056054184 |13.723013922280746| 90|
|Czech Republic |7.83669639e-02| 8.53496011e+01 |87.25 |24.25| 1.6393596310755 |11.54068888758379| 12|
|Slovenia |5.81494624e-02| 8.65696665e+01 |88.0125 |24.8125| 1.7712548517929316 |13.895227373094691| 80|
|Luxembourg |-6.83229814e-02 | 9.02608696e+01 |88.66666666666667 |23.333333333333332| 0.7453559924999299| 4.2295258468165065| 6|
|Croatia |6.31882800e-02| 8.57439265e+01 |87.35211267605634 |25.450704225352112| 2.2772518126658765 |12.901346946160057 |71|
|Georgia |1.06590646e-02| 8.74726231e+01 |87.67857142857143 |19.321428571428573| 2.093986368524071| 7.597243726832644 |84|
|Uruguay |5.30350272e-02| 8.53519742e+01 |86.75229357798165 |26.40366972477064| 2.6755980667374915 |18.39880294573189 |109|
|England |3.46444045e-02| 8.97602616e+01 |91.55072463768116 |51.68115942028985| 1.8220567442448263 |14.750576263489505| 69|
|Lebanon |4.84964775e-02| 8.61975652e+01 |87.68571428571428 |30.685714285714287| 2.7440473608098213 |17.7792357678781| 35|
|Serbia | 0.08541846 |85.40724763 |87.5 |24.5| 1.2583057392117916| 9.827681991870378| 12|
|Brazil |6.39195942e-02| 8.31404641e+01 |84.65957446808511 |23.76595744680851| 2.4257185445183995 |10.935425092589497| 47|
|Moldova | 0.14565957 |84.7642092  |87.20338983050847 |16.74576271186441| 2.399008700763142| 9.441332174636687| 59|
|Morocco |4.25079702e-03| 8.84885380e+01 |88.57142857142857 |19.5| 1.6567733578204575| 5.797166795697952| 28|
|Peru |4.44270891e-02| 8.27600357e+01 |83.5625 |18.0625| 1.8016919131749467 |13.230971005561157| 16|
|India | 0.33333333 |85.77777778 |90.22222222222223 |13.333333333333334| 1.617802197617893| 3.4318767136623336| 9|
|Bulgaria |7.89846124e-02| 8.67794098e+01 |87.93617021276596 |14.645390070921986| 2.070436161803988| 9.474964961310276 |141|
|Cyprus | 0.16780045 |84.45124717 |87.18181818181819 |16.272727272727273| 1.526623238522424| 2.699862255439545 |11|
|Armenia |**1.** |73. |87.5 |14.5| 0.5| 0.5| 2|
|Switzerland |3.62800353e-03| 8.82620117e+01 |88.57142857142857 |85.28571428571429| 2.3211538298959886 |64.86626745128183| 7|
|Bosnia and Herzegovina  |-3. |**124.** |86.5 |12.5| 1.5| 0.5| 2|
|Ukraine |-0.16380299 |85.5807561  |84.07142857142857| 9.214285714285714| 1.5336364681131347| 2.1104695289563082 |14|
|Macedonia | 0.31272727 |81.96       |86.83333333333333 |15.583333333333334| 1.674979270186815| 1.3819269959814167 |12|
|China | Failed to plot|

The table above is very useful for us because it gives us a direct estimation of each country from which we can initially deduce that **Bosnia and Herzegovina** has the highest intercept. But interestingly, the **a** coefficient is negative which means unlike most countries, points of a wine will infact decreases with price. These irregularities can then be explained after realising that bosnia only have 2 data points thus any sort of characteristics that we found will not be super relevant due to lack of sample size. 

and for the country that has the most points increase per price, is **Armenia**, but unlike most countries, intercept for Armenian wine are much lower than most countries in this data sets. just like before, Armenia only have 2 data points, which means we cannot conclude any useful information from it.

Thus, for the sake of simplicity we will arbitrarily decide the threshold of number of datasets to be able to take any conclusion accountable is 200.

Among countries that has a sample size of more than 200, **Austria** has the highest intercept and the highest mean points.

Among countries that has a sample size of more than 200, **New Zealand** has the increase in points for each price increase.

For Bonus 4, I added MLP Regressor to have a comparison between linear model and neural network. From the table below, the linear regressor performs better than both logistic and MLP regressor, it adds more evidence that the relationship between prices and points is infact linear.

| Regressor | Score | 
|---|:-:|
|Linear | 0.1651652174560685 |
|Logistic | 0.16804498842209725 |
| MLP|0.3982699056516519 |



