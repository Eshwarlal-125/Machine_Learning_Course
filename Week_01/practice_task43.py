# 43. Given a DataFrame of employees (name, department, salary), use boolean filtering to select all employees in the 'Sales' department earning above 50,000.
import pandas as pd
df=pd.DataFrame({"name":["Ali","Ahmed","Sara","John"],"department":["Sales","HR","Sales","IT"],"salary":[60000,45000,55000,70000]})
result=df[(df["department"]=="Sales")&(df["salary"]>50000)]
print(result)