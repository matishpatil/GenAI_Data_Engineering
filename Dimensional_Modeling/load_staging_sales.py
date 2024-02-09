import csv
import psycopg2
import os

# Get the password from the environment variable
db_password = os.environ.get('DB_PASS') 

# Connect to the database 
conn = psycopg2.connect(dbname="postgres", user="postgres", password=db_password)
cur = conn.cursor()

# Open the CSV file 
with open('sales.csv','r') as f:
    reader = csv.reader(f)
    next(reader)  

    # Insert each row into the staging.sales table
    for row in reader:
        date_of_sale = row[0]  
        product = row[1]
        location = row[2]
        quantity = row[3]  
        unit_price = row[4]
        total_price = row[5]
        
        insert_query = "INSERT INTO staging.sales (date_of_sale, product, location, quantity, unit_price, total_price) VALUES (%s, %s, %s, %s, %s, %s)"
        cur.execute(insert_query, (date_of_sale, product, location, quantity, unit_price, total_price))

conn.commit()
cur.close() 
conn.close()