import csv
import psycopg2
import os

# Get database password 
db_password = os.environ.get('DB_PASS')

# Connect to the database
conn = psycopg2.connect(dbname="postgres", user="postgres", password=db_password)
cur = conn.cursor()

# Open locations CSV file
with open('locations.csv','r') as f:
    reader = csv.reader(f)
    next(reader)

    row_count = 0
    # Insert into staging.locations table
    for row in reader:
        location_id = row[0]
        city = row[1]
        state_province = row[2] 
        country = row[3]
        postal_code = row[4]
        
        insert_query = """INSERT INTO staging.locations  
                          (location_id, city, state_province, country, postal_code) 
                          VALUES (%s, %s, %s, %s, %s)"""
                          
        cur.execute(insert_query, (location_id, city, state_province, country, postal_code))
        row_count += 1

conn.commit()  
print(f"{row_count} rows loaded") 

cur.close()
conn.close()
