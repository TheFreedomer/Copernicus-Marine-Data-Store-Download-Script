import netCDF4 as nc
import pandas as pd

"""
Check the integrity of the nc file
"""

# Read data
dataset_test = nc.Dataset(r'Your nc filepath', mode='r')

# Display information
print(dataset_test.variables.keys())
print(">>>" * 3)
print(dataset_test['time'])
print(">>>" * 3)

print(pd.to_datetime(dataset_test['time'][:], unit='h', origin='1950-01-01'))
