import json
import sys
from jsonschema import validate, ValidationError

def validate_json(json_file, schema_file):

  with open(schema_file) as f:
    schema = json.load(f)

  with open(json_file) as f:
    data = json.load(f)
  
  errors = []
  
  for record in data:
    try:
      validate(instance=record, schema=schema)
    except ValidationError as ve:
      errors.append({
        "record": record,
        "error": ve.message
      })

  if errors:
    print(f"Invalid records found in {json_file}:")
    for e in errors:
      print(f"- {e['error']}")
      print(f"  Record: {e['record']}")
  else:
    print(f"All records in {json_file} are valid")  

if __name__ == "__main__":

  if len(sys.argv) != 3:
    print("Usage: python validate.py <json_data_file> <json_schema_file>")
    sys.exit(1)

  json_file = sys.argv[1]
  schema_file = sys.argv[2]
  
  validate_json(json_file, schema_file)