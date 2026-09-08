# 8. Given a list of dictionaries representing employees (name, department, salary), write code to find the employee with the highest salary.
employees=[{"name":"Ali","department":"IT","salary":50000},{"name":"Sara","department":"HR","salary":60000},{"name":"John","department":"Sales","salary":55000}]
highest=max(employees,key=lambda x:x["salary"])
print(highest)