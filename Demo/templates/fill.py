from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector
app = Flask(__name__,template_folder='templates',static_url_path='/static',static_folder="static")

app.secret_key = 'secrets.token_hex(16)'  # Replace with a secret key for sessions
# PER_PAGE = 10 
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "password",
    "database": "myproject",
}

db = mysql.connector.connect(**db_config)

# Create a cursor to execute SQL queries
cursor = db.cursor()

# Create a table for user registration if it doesn't exist
create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    mobile_number VARCHAR(20) NOT NULL,
    city VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    user_type VARCHAR(50) NOT NULL
)
"""
cursor.execute(create_table_query)
db.commit()


create_table_query_bus_pass="""
CREATE TABLE bus_pass (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(15) NOT NULL,
    aadhar VARCHAR(12) NOT NULL
    address TEXT NOT NULL,
    user_type VARCHAR(10) NOT NULL,
    
);
# """
# cursor.execute(create_table_query_bus_pass)
# db.commit()


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/services', methods=['GET', 'POST'])
def services():
    if request.method == 'POST':
        # Get data from the form
        name = request.form['name']
        email = request.form['email']
        aadhar = request.form['Aadhar-Number'] 
        address = request.form['Address']  
        user_type = request.form['userType']
        try:
            cursor = db.cursor()
            insert_query = "INSERT INTO bus_pass (name, email, aadhar, address, user_type) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(insert_query, (name, email, aadhar, address, user_type))
            db.commit()
            cursor.close()
            return render_template('success.html')  # Return the success.html template
        except mysql.connector.Error as e:
            return f"An error occurred while inserting data: {str(e)}"
        finally:
            if cursor:
                cursor.close()
    return render_template('index.html')
