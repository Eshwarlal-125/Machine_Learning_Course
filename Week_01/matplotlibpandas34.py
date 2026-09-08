# 34. Given a DataFrame with missing values in a 'score' column, fill the missing values with the column mean and confirm no NaNs remain.
import pandas as pd
df=pd.DataFrame({"score":[80,90,None,70,None]})
df["score"]=df["score"].fillna(df["score"].mean())
print(df)
print(df["score"].isna().sum())