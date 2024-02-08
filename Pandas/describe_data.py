import pandas as pd
import sys

# Get CSV file path from first script parameter 
csv_path = sys.argv[1]

# Load CSV file into DataFrame
df = pd.read_csv(csv_path)  

# Print summary statistics
print(df.info())
print()
print(df.describe())  
print()
print(df.isnull().sum())