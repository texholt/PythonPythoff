import os

old_file_name = 'C:/Users/RHolton1/Documents/raw_data.csv'
new_file_name1 = 'C:/Users/RHolton1/Documents/new_data' 

def sum1forline(old_file_name):
    with open(old_file_name) as f:
        return sum(1 for line in f)

linesum = str(sum1forline(old_file_name))

new_file_name2 = linesum
new_file_name3 = '.csv'

os.rename(old_file_name, (new_file_name1 + new_file_name2 + new_file_name3))

print("File renamed!")