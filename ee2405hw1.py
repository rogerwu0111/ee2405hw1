# Part. 1

#=======================================

# Import module

#  csv -- fileIO operation

import csv


#=======================================


# Part. 2

#=======================================

# Read cwb weather data

cwb_filename = '105022201.csv'

# cwb_filename = 'sample_input.csv'

data = []

header = []

with open(cwb_filename) as csvfile:

   mycsv = csv.DictReader(csvfile)

   header = mycsv.fieldnames

   for row in mycsv:

      data.append(row)

#=======================================


# Part. 3

#=======================================

# Analyze data depend on your group and store it to target_data like:

# Retrive all data points which station id is "C0X260" as a list.

def func(str):

   temp_data = list(filter(lambda item: item['station_id'] == str, data))

   temp_data = list(filter(lambda item: item['HUMD'] != '-99.000', temp_data))

   temp_data = list(filter(lambda item: item['HUMD'] != '-999.000', temp_data))

   sum = 0

   if (temp_data == []): return [str, 'None']

   for row in temp_data:
      sum += float(row['HUMD'])

   # return [str, round(sum, 5)]
   return [str, sum]

target_data = []

target_data.append(func('C0A880'))

target_data.append(func('C0F9A0'))

target_data.append(func('C0G640'))

target_data.append(func('C0R190'))

target_data.append(func('C0X260'))

# Retrive ten data points from the beginning.

# target_data = data[:10]


#=======================================


# Part. 4

#=======================================

# Print result

print(target_data)

#========================================