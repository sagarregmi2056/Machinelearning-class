import pandas as pd

# data=[
#     100,200,300,400,500
# ]

# # series =pd.Series(data, index=["a","b","c","d","e"])
# series= pd.Series(data, index=["firstman in line","secondman in line","thirdman in line","fourthman in line","fifthman in line"], dtype=int)

# print(series)   
# print(type(series))
# print(series.loc["fifthman in line"])
# print(series.iloc[0])

# # arithmetic operations

# # return the value that is greater than 200
# print(series[series>200])

calories={"day1":420,"day2":3800,"day3":3900 ,"day4":3080 ,"day5":390 ,"day6":380}

print(calories)
series=pd.Series(calories)
print(series)
#
print("************************************************")
print("max value: ", series.max())
print("min value: ", series.min())
print("mean value: ", series.mean())
print("sum value: ", series.sum())
print("************************************************")
print(series.loc["day2"])
print(series.iloc[1])
print("************************************************")
print(series[series>2000])
