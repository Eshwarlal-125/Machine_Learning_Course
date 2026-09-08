# 32. Given a DataFrame of exam scores across 3 subjects for 10 students, use groupby-style aggregation to find each student's average and identify the top performer.
import pandas as pd
df=pd.DataFrame({"student":["Ali","Sara","John","Ahmed","Maria","Zain","Hina","Usman","Ayesha","Bilal"],"Math":[80,90,70,85,88,75,92,78,95,82],"Physics":[75,85,80,90,82,88,90,80,92,85],"CS":[90,88,75,85,95,80,94,85,96,89]})
df["average"]=df[["Math","Physics","CS"]].mean(axis=1)
print(df)
print(df.loc[df["average"].idxmax()])