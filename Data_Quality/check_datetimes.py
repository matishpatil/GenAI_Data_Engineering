import re  
import sys

date_regex = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3} [+-]\d{4}"

if len(sys.argv) < 2:
    print("Usage: python script.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

try:
    with open(filename, 'r') as f:
        data = f.readlines()[1:] # Skip first line 
except FileNotFoundError: 
    print(f"File {filename} does not exist")
    sys.exit(1)

for row in data:
    date_time = row.split(",")[0]
    if not re.match(date_regex, date_time):
        print(f"Invalid datetime format:\n{row}")