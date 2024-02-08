import json  
import sys
from jsonschema import validate
   
def validate_json(json_file, schema_file):

  with open(schema_file) as f:
    schema = json.load(f)  

  with open(json_file) as f:
    data = json.load(f)
  
  validate(instance=data, schema=schema)
  
  print(f"{json_file} is valid")

if __name__ == "__main__":
  
  if len(sys.argv) != 3:
    print("Usage: python validate.py <json_data_file> <json_schema_file>")
    sys.exit(1)

  json_file = sys.argv[1]
  schema_file = sys.argv[2]
  
  validate_json(json_file, schema_file)