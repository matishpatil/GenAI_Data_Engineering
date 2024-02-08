import json

# Open the JSON file and load the data
with open('hotels_sample.json') as f:
  data = json.load(f)

# Print out some data to verify it loaded properly  
print(data[0]['title'])
print(data[1]['subtitles'][0]) 
print(data[2]['price']['value'])