# 45. Using groupby(), compute the average marks per subject from a DataFrame of student records.
import pandas as pd
df=pd.DataFrame({"name":["Ali","Sara","John","Ahmed"],"subject":["Math","Math","CS","CS"],"marks":[80,90,70,90]})
print(df.groupby("subject")["marks"].mean())