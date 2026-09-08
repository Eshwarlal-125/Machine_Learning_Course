# 44. Given a DataFrame with some missing values, demonstrate both dropna() and fillna() and explain when each is appropriate.
import pandas as pd
df=pd.DataFrame({"name":["Ali","Sara","John"],"marks":[80,None,90]})
print(df.dropna())
print(df.fillna(0))