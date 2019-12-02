import pandas as pd
import math

# Function for Calculating fuel
def calc_fuel (mass):
    fuel = math.floor(mass/3) - 2
    return fuel

df = pd.read_csv (r'C:\Users\haley\Dropbox\Code\Advent of Code 2019\input.csv')
fuel_list = []

# Iterate through the input list and calculate fuel
for mass in df.mass:
    fuel = calc_fuel (mass)
    fuel_list.append (fuel)
    
# Check for the tricky bit    
print (calc_fuel (14))    

# Print the final answer
print (sum(fuel_list))
