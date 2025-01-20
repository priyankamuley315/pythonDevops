import csv
import pandas as pd

data = pd.read_csv("book1.csv")
#this will give us list
data_dict = data.to_dict()
print(data_dict)

#this will get unique values from column "Profile"
unique_values = data['Profile'].unique()
print("Unique values are : ", unique_values)

#this will print all values in Profile column
print(data.Profile)

# this prints complete row where profile is Dev
print(data[data.Profile == "Dev"])

#x variable will store list of skills that are associated with dev profile
x = data[data.Profile == "Dev"]

#now we want only skills associated so we will use x.Skills
print("list of skills that are for dev profile ","\n", x.Skills)

#now we will print number of list that obtained above
print("The number of skills will be : ", len(x))
