# Write a program to make the data frame and display the result.
import pandas as pd
data={
    "Name":["Bibek Joshi","Nabin Dhami","Ankit Saud"],
    "Age":[13,12,21],
    "Address":["Dadeldhura","Bajhang","Darchula"],
    "Current Address":["Kathmandu","Kathmandu","Dhangadhi"]
}
a=pd.DataFrame(data)
print("Dataframe:")
print(a)