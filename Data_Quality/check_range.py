import csv
import sys

input_file = sys.argv[1]

with open(input_file) as f:
    reader = csv.reader(f)
    next(reader) 
    
    for row in reader:
        temperature = float(row[3])
        if temperature > 38 or temperature < -16:
            print(row)