import pandas as pd
import sys
import matplotlib.pyplot as plt

csv_path = sys.argv[1]

df = pd.read_csv(csv_path, parse_dates=["Formatted Date"])

print(df.head())

# Group small categories into 'Other'  
summary_counts = df["Summary"].value_counts()
small_categories = summary_counts[summary_counts < len(df) * 0.05]
df.loc[df["Summary"].isin(small_categories.index), "Summary"] = "Other"

# Plot
summary_counts = df["Summary"].value_counts()
labels = summary_counts.index
sizes = summary_counts.values  

fig1, ax1 = plt.subplots() 
ax1.pie(sizes, labels=labels, autopct='%1.1f%%')
ax1.axis('equal') 

plt.title("Summary Pie Chart")  
plt.tight_layout()
plt.show()