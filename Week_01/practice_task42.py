# 42. Build a DataFrame of 5 students with columns name, subject, and marks; display it using head() and summarize it with describe().
import pandas as pd
df=pd.DataFrame({"name":["Ali","Ahmed","Sara","John","Maria"],"subject":["Math","Physics","English","CS","Biology"],"marks":[85,78,92,88,75]})
print(df.head())
print(df.describe())