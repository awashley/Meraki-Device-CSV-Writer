#!/usr/local/bin/python3
#
import json
import csv
import sys

JSON_filename = sys.argv[1]
CSV_filename = sys.argv[2]

file_input = open(JSON_filename, 'r')
DEV_JSON0 = file_input.read()
DEV_JSON = ('{"DEV_details":' + DEV_JSON0 + '}')
DEV_parsed = json.loads(DEV_JSON)
DEV_data = DEV_parsed['DEV_details']

# open a file for writing
New_DEV_data = open(CSV_filename, 'w')
# create the csv writer object
csvwriter = csv.writer(New_DEV_data)
count = 0
for DEV in DEV_data:
  if count == 0:
    header = DEV.keys()
    csvwriter.writerow(header)
    count += 1
  csvwriter.writerow(DEV.values())
New_DEV_data.close()
