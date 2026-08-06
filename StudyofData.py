import pandas as pd
df = pd.DataFrame("train.csv")

#how big is data
df.shape()

#how does data look like
df.head()

#what is the data type of cols?
df.info()

#are there any missing values
df.isnull().sum()

#how does the data look mathematically
df.describe()

#are there duplicate values
df.duplicated().sum()

#how is the correlation between cols
df.corr()