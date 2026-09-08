# 47. Merge two small DataFrames — one with student names and IDs, another with student IDs and grades — into a single DataFrame using pd.merge().
import pandas as pd
df1=pd.DataFrame({"id":[1,2,3],"name":["Ali","Sara","John"]})
df2=pd.DataFrame({"id":[1,2,3],"grade":["A","B","A"]})
result=pd.merge(df1,df2,on="id")
print(result)