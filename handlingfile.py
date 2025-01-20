import csv
import pandas as pd

df = pd.read_csv("book1.csv")
data = pd.DataFrame(df)
print(data)
# #this will store unique values .unique() function
# unique_values = df['Profile'].unique()
# print("Unique values are : ", unique_values)
#
# print("______________________________________")
#
# #data.profile will print all the values in column profile
# # print(data.Profile)
#
# # this prints complete row where profile is Dev
# print(data[data.Profile == "Dev"])
#
# print("*************************************")
#
# x = data[data.Profile == "Dev"]
# print(x.Skills)
# print(len(x))









# if df['Profile'] == "Dev":
#     print(df['skills'])
# else:
#     print("stop")