# Write a python program to create a simple series using dictionary.
import pandas as pd
calories={
    "day-1":200,
    "day-2":320,
    "day-3":230,
    "day-4":240,
    "day-5":400,
}
series_dict=pd.Series(calories)
print(series_dict)