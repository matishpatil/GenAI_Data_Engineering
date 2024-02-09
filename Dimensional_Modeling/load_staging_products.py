import csv 
import psycopg2
import os

# Get database password  
db_password = os.environ.get('DB_PASS')  

# Connect to the database
conn = psycopg2.connect(dbname="postgres", user="postgres", password=db_password) 
cur = conn.cursor()

# Open products CSV file
with open('products.csv','r') as f:
    reader = csv.reader(f)
    next(reader)  

    # Insert rows into staging.products
    for row in reader:
        product_id = row[0]
        product_name = row[1]
        product_category = row[2]
        
        insert_query = """INSERT INTO staging.products  
                          (product_id, product_name, product_category) 
                          VALUES (%s, %s, %s)"""
        cur.execute(insert_query, (product_id, product_name, product_category))  

conn.commit()
cur.close()
conn.close()