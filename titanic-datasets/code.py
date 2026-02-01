import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df =sns.load_dataset('titanic')

# print(df.head(10))

# print(df.info(verbose=True))

# print(df.shape)

# print(df.isnull().sum())

# print(df.describe())

# we are adding mean as mean data for dataframe here.
df['age']=  df['age'].fillna(df['age'].mean())


# print(df.isnull().sum())

# print(df.tail(10))

print(sns.countplot(x='survived', data=df))

# sns.title("Survival Count")
# plt.show()