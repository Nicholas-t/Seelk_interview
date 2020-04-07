# Repo for seelk interview


Objective 
1. Open a CSV file and perform some tasks on it.
2. Create a copy of the Dataset in a columnar format (You can choose between Parquet or ORC) and save it.
3. Open the columnar file from 2, and create a new "clean" dataset:
 Remove all the text columns and just leave the numeric ones (id, points, price).
Store the clean dataset in the same columnar format.
4. Using the columnar copy from 2, create an aggregation:
Aggregate the data by country, and calculate the average of points and the standard deviation.
Store the aggregation in the same columnar format.

**BONUS**
Bonus ⭐ What are the top 5 best wines below 10 USD?
Bonus ⭐ What are the top 5 best wines below 30 USD from Chile 🗿?
Bonus ⭐ ⭐  From the clean dataset (3) create a visualisation of points vs price.
Bonus ⭐ ⭐ ⭐ Predict the points of a wine taking as input the price and the country (using Machine Learning).

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




If I run the code in my computer, the output should be at least 3 folders:
original: It contains the original CSV.
cleaned: It contains the columnar files with id, points, price.
aggregated: It contains the columnar files with the aggregations.