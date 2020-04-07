from src import *

# Objective 2

print('Doing Objective 2')
obj2(save=True)

# Objective 3

print('Doing Objective 3')
obj3(save=True)

# preprocess

print('preprocess to get numeric and country dataset')
create_pre_numeric()

# Objective 4

print('Doing Objective 4')
obj4(save=True)

# Bonus 1

print('Doing Bonus 1')
df = bon1()
df.to_csv('./bonus1.csv')

# Bonus 2

print('Doing Bonus 2')
df = bon2()
df.to_csv('./bonus2.csv')

# Bonus 3

print('Doing Bonus 3')
bon3()

# plotting mean and std

print('Plotting mean and std')
plot_mean_std()

# Bonus 4

# Comment this for quicker runs
print('Preprocessing...')
preprocess()

print('Doing Bonus 4')
bon4()
