import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host='db-mysql-tor1-59654-do-user-14245628-0.b.db.ondigitalocean.com',
    port= 25060,
    user='heri2',
    password='AVNS__EO7b3yqnmDshkXmeTZ',
    database='pets_images'
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute a select query to fetch all rows from a table
cursor.execute('SELECT * FROM Pets')  # Replace 'your_table' with the name of your actual table

# Fetch all the rows returned by the query
rows = cursor.fetchall()

# Display the content of the database
for row in rows:
    print(row)  # Modify this line to format and print the content as desired

# Close the cursor and the database connection
cursor.close()
conn.close()
