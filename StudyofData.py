import pandas as pd
df = pd.DataFrame("train.csv")

#how big is data
df.shape()

#how does data look like
df.head()

#what is the data type of cols?
df.info()