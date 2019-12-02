import pandas as pd
import math


# Function to calculate fuel needed per mass
def calc_fuel (mass):
    fuel = math.floor(mass/3) - 2
    return fuel

df = pd.read_csv (r'C:\Users\haley\Dropbox\Code\Advent of Code 2019\input.csv')
mass_list = df.mass
fuel_list = []

# Determine fuel needed per mass (input)
for mass in mass_list:
    fuel = calc_fuel (mass)
    fuel_list.append (fuel)
    
# Check for the tricky bit
#print (calc_fuel (14))    
#print (sum(fuel_list))

# Determine fuel needed per mass + additional fuel for that mass

final_list = []

for fuel in fuel_list:
    total_fuel = fuel
    add_fuel = calc_fuel (fuel)
    if add_fuel > 0:
        total_fuel = fuel + add_fuel
        while add_fuel > 0:
            temp = calc_fuel (add_fuel)
            if temp > 0:
                total_fuel = total_fuel + temp
            add_fuel = temp
    
    final_list.append (total_fuel)
    
print (sum(final_list))
