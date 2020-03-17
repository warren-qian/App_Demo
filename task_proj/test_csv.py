import csv
import os

#open csv file
path = '/Users/warrenq/Desktop/testdata/test.csv'
mapping_list = []
with open(path, 'r') as f:
   csv_reader = csv.reader(f, delimiter=',')
   line_count = 0
   for line in csv_reader:
       if line_count == 0:
           header = line
       else:
           row_dict = {key:value for key,value in zip(header,line)}
           mapping_list.append(row_dict)
       line_count += 1
print(mapping_list)

with open(path, 'r') as f:
    map_list = list(csv.DictReader(f))
print(map_list[0]['id'])