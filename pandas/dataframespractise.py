import pandas as pd

employees_data={"Name":["John Doe","Jane Smith","Jim Beam","Jill Johnson"],
                "Age":[25,30,35,40],
                "Department":["HR","IT","Marketing","Sales"],
                "Salary":[50000,60000,70000,80000]}

df=pd.DataFrame(employees_data, index=["Employee 1","Employee 2","Employee 3","Employee 4"])
print(df)
# this will return the index in list format
print(df.index)
# this will return the columns in list format
print(df.columns)
# this will return the values all in list format
print(df.values)

print(df.loc["Employee 1"])

# this will
# df.loc["Employee 1"]["Age"]=26
print(df)

# lets add new column to the dataframe called locations
df["locations"]=["New York","Los Angeles","N/A","N/A"]
print(df)
# lets add new row to the dataframe called Employee 5
# [{},{}] we can add multiple rows to the dataframe by using this format
new_row = pd.DataFrame([{"Name":"John Doe","Age":26,"Department":"HR","Salary":50000,"locations":"New York"}], index=["Employee 5"])
# we will concatenate the new row to the dataframe [df,new_row] means df is the dataframe and new_row is the new row we want to add to the dataframe
df=pd.concat([df,new_row])
print("************************************************")
print(df)


# lets add new rows employees 6,7,8,9,10
new_rows = pd.DataFrame([{"Name":"Employee 6","Age":27,"Department":"IT","Salary":60000,"locations":"Los Angeles"},
                         {"Name":"Employee 7","Age":28,"Department":"Marketing","Salary":70000,"locations":"Chicago"},
                         {"Name":"Employee 8","Age":29,"Department":"Sales","Salary":80000,"locations":"Houston"},
                         {"Name":"Employee 9","Age":30,"Department":"HR","Salary":90000,"locations":"New York"},
                         {"Name":"Employee 10","Age":31,"Department":"IT","Salary":100000,"locations":"Los Angeles"}], index=["Employee 6","Employee 7","Employee 8","Employee 9","Employee 10"])
df=pd.concat([df,new_rows])
print("************************************************")
print(df)

