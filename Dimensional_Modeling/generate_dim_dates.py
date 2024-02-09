import datetime
import math

def generate_time_table(start_date, end_date):
    statements = []
    time_id = 1
    
    current_date = start_date  
    while current_date <= end_date:
        month = current_date.month
        quarter = math.ceil(month / 3)
        
        query = f"""INSERT INTO dm.dim_dates VALUES ({time_id}, '{current_date}', {current_date.day}, {month},  {quarter}, {current_date.year});"""
        
        time_id += 1
        statements.append(query)
        current_date += datetime.timedelta(days=1)

    return statements

start_date = datetime.date(2024, 1, 1)
end_date = datetime.date(2024,12,31)  

queries = generate_time_table(start_date, end_date)

for query in queries:
    print(query)