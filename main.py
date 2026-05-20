# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd
# STEP 1B
# Connect to the database
conn = sqlite3.connect('data.sqlite')

# STEP 2
# Replace None with your code
df_first_five = pd.read_sql("""SELECT employeeNumber,lastName FROM employees limit 23;""", conn)
print("---------------------Employee Data---------------------")
print(df_first_five)
print("-------------------End Employee Data-------------------")

# STEP 3
# Replace None with your code
df_five_reverse = pd.read_sql("""
                              SELECT lastName, employeeNumber 
                              FROM employees  
                              ORDER BY employeeNumber DESC
                              LIMIT 23;
                              """, conn)
print("---------------------Employee Data---------------------")
print(df_five_reverse)
print("-------------------End Employee Data-------------------")


# STEP 4
# Replace None with your code
df_alias = pd.read_sql("""
                        SELECT lastName, employeeNumber AS ID
                        FROM employees  
                        ORDER BY employeeNumber DESC
                        LIMIT 23;
                        """, conn)
print("---------------------Employee Data---------------------")
print(df_alias)
print("-------------------End Employee Data-------------------")



# STEP 5
# Replace None with your code
df_executive = pd.read_sql("""
                        SELECT *, 
                           CASE
                                WHEN jobTitle = "President" OR 
                                jobTitle = "VP Sales" OR 
                                jobTitle = "VP Marketing" 
                                THEN "Executive"
                                else 'Not Executive'
                           END as role
                           FROM employees;
                           """, conn)
print("---------------------Employee Data---------------------")
print(df_executive)
print("-------------------End Employee Data-------------------")



# STEP 6
# Replace None with your code
df_name_length = pd.read_sql("""
                        SELECT lastName,
                           Length(substr(lastName,instr(lastName,' ')+1))AS name_length   
                           
                           FROM employees;
                           """, conn)
print("---------------------Employee Data---------------------")
print(df_name_length)
print("-------------------End Employee Data-------------------")


# STEP 7
# Replace None with your code
df_short_title = pd.read_sql("""
                        SELECT jobTitle,
                           substr(jobTitle,1,2)AS short_title   
                           
                           FROM employees;
                           """, conn)
print("---------------------Employee Data---------------------")
print(df_short_title)
print("-------------------End Employee Data-------------------")

# STEP 8
# Replace None with your code

sum_total_price = pd.read_sql("""SELECT ROUND(priceEach * quantityOrdered) AS total_price
                              from orderdetails;
                           """, conn).sum().values
print("---------------------Order Details Data---------------------")
print(sum_total_price[0])
print("-------------------Order Details Data-------------------")

# STEP 9
# Replace None with your code
df_day_month_year = pd.read_sql("""SELECT 
                                orderDate,
                                strftime('%d',orderDate) as day,
                                strftime('%m',orderDate) as month,
                                strftime('%Y',orderDate) as year
                              from orders;
                           """, conn)
print("---------------------Order Details Data---------------------")
print(df_day_month_year)
print("-------------------Order Details Data-------------------")

conn.close()
