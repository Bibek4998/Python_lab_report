# Write a python program to make the series and display the result.
import pandas as pd
data=[10,12,11,13,15,1,89]
index=["a","b","c","d","e","f","g"]
ser=pd.Series(data,index=index)
print(ser)