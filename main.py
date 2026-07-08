# STEP 1A
# Import SQL Library and Pandas
import pandas as pd  
import sqlite3
# Test that it works
print(pd.__version__)
# STEP 1B
# Connect to the database

conn = sqlite3.connect('data.sqlite')
employee_data = pd.read_sql("""SELECT * FROM employees""", conn)
print("---------------------Employee Data---------------------")
print(employee_data)
print("-------------------End Employee Data-------------------")


# STEP 2
# Replace None with your code
query_2 = "SELECT employeeNumber ,lastName FROM employees;"
df_first_five = pd.read_sql_query(query_2,conn)


# STEP 3
# Replace None with your code
query_3 ="SELECT lastName,employeeNumber FROM employees;"
df_five_reverse = pd.read_sql_query(query_3 ,conn)

# STEP 4
# Replace None with your code
query_4 = "SELECT employeeNumber AS ID FROM employees;"
df_alias = pd.read_sql_query(query_4, conn)

# STEP 5
# Replace None with your code
query_5 = """
SELECT *,
    CASE 
        WHEN jobTitle IN ('President', 'VP Sales', 'VP Marketing') THEN 'Executive'
        ELSE 'Not Executive'
    END AS role
FROM employees;
"""
df_executive = pd.read_sql_query(query_5, conn)


# STEP 6
# Replace None with your code
query_6="SELECT LENGTH(LastName AS name_length FROM employees;)"
df_name_length = pd.read_sql_query(query_6,conn)

# STEP 7
# Replace None with your code
query_7 ="SELECT SUBSTR(jobTitle,1,2) AS short_title FROM employees;"
df_short_title = pd.read_sql_query(query_7,conn)

order_details = pd.read_sql("""SELECT * FROM orderDetails;""", conn) 
print("------------------Order Details Data------------------")
print(order_details)
print("----------------End Order Details Data----------------")
# STEP 8
# Replace None with your code
query_8 ="""
SELECT ROUND(priceEach *quantityOrdered) AS total_price
FROM orderDetails;
"""
sum_total_price = pd.read_sql_query(query_8,conn).sum()


# STEP 9
# Replace None with your code
query_9 ="""
orderDate,
strftime(%d,orderdate) AS day
strftime(%m,orderdate) AS month
strftime(%Y,orderdate) AS year
FROM orderDetails;
"""

df_day_month_year = pd.read_sql_query(query_9,conn)

conn.close()