from functools import wraps
from flask import Flask, abort, render_template, render_template_string, request, redirect, url_for, session, flash 
from flask_login import LoginManager, login_required, logout_user
# from flask_paginate import Pagination, get_page_args
import mysql.connector
import bcrypt
from datetime import datetime ,timedelta
import time
from utile import requires_role
app = Flask(__name__,template_folder='templates',static_url_path='/static',static_folder="static")
#this is our flask application instance for class Flask or we can say that is our object of class .


app.secret_key = 'secrets.token_hex(16)'  # Replace with a secret key for sessions as our need ,we can fix any secrete key
# PER_PAGE = 10 
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "password",
    "database": "myproject",
}#here we connect our database for transfer data with UI or for performing operation on data 

db = mysql.connector.connect(**db_config)
#I pass db_config dict in connection

# Create a cursor to execute SQL queries , without it we face difficulty to execute our query
cursor = db.cursor()

# Create a table for user registration if it doesn't exist,this was done after creating my database we can make
#change our database form here also ,or create any attribute's as we need after creating database
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
#always remeber to commit ,after execute any query

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
#--------------------------------------authorization on tables------------------------------------

# # the login_required function
def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if session.get('username'):
            # User is authenticated, execute the original view function
            return view(*args, **kwargs)
        else:
            # User is not authenticated, redirect to the login page
            flash("You are not logged in..! Login to perform action")
            return redirect(url_for('login'))

    return wrapped_view



#----------------------------------------------------------------

@app.route('/logout')
def logout():
    # Clear the session to log the user out
    session.pop('username', None)
    # flash('You have been logged out.', 'info')
    return render_template('new_index.html')

#---------------------------------------------------------------------

# cursor.execute(create_table_query_bus_pass)
# db.commit()

# #-----------------------------this is our pages for auth----------------------require----------------

# i am creating root directory which is denoted by '/' slash this is our first page open when we run our file .
@app.route('/')
def home():
    if 'username' in session:
        return render_template('index1.html')
    return render_template('new_index.html')
# on this root directry one fuction is wrote and this tell us to render/ change direction on given page which is index.html


# @app.route('/signin')
# def signin():
#     return render_template('login_page.html')



@app.route('/registerbutton')
def registerbutton():
    return render_template('registerbutton.html')


@app.route('/username')
def username():
    if username in session:
        return render_template('user.html')


# @app.route('/userinfo')
# def userinfo():
#     return render_template ('user_info.html')

#---------------------authorisation for particular page by different users----------------------------
    
   



#
@app.route('/usertype')
def usertype():
    return render_template('user_type.html')    

#----------------this is our main page of login which work under authentication.----------------------------

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = db.cursor()

        # Fetch user data based on the provided username
        cursor.execute("SELECT name, password FROM users WHERE BINARY name=%s", (username,))
        user_data = cursor.fetchone()
        cursor.fetchall()
        cursor.close()

        if user_data:
            stored_password = user_data[1]
            if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                # Passwords match, you can log in
                # Add  login logic here
                session['username'] = username 
                flash('You are now logged in!', 'success')
                return redirect('home')
            else:
                return "Incorrect password. Please try again."
        else:
            return "Username not found. Please register."

    return render_template('login_page.html')


#--------------------------------------------admin authentication and authorisation-----------------------s

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/admin_register', methods=['GET', 'POST'])
def admin_register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        mobile_number = request.form['mobile_number']
        email = request.form['email']

        # Check if both username and password already exist
        cursor.execute("SELECT username, password FROM admin_registration WHERE username=%s", (username,))
        admin_data = cursor.fetchone()

        if admin_data:
            stored_password = admin_data[1].encode('utf-8')
            if bcrypt.checkpw(password.encode('utf-8'), stored_password):
                return "Username and password already exist. You can log in now."

        # Commit any pending changes from previous queries
        db.commit()

        # Hash the password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Insert the new admin into the database
        insert_query = "INSERT INTO admin_registration (username, password, mobile_number, email) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (username, hashed_password, mobile_number, email))

        # Commit the transaction after the INSERT query
        db.commit()
        return render_template('admin.html')  # Adjust the template accordingly

    return render_template('admin_registration.html')

@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = db.cursor()

        # Fetch admin data based on the provided username
        cursor.execute("SELECT username, password FROM admin_registration WHERE username=%s", (username,))
        admin_data = cursor.fetchone()
       # print(admin_data)
        cursor.fetchall()
        cursor.close()

        if admin_data:
            stored_password = admin_data[1]
            if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                # Passwords match, you can log in as admin
                # Add admin login logic here
                session['role'] = 'Admin'
                flash('You are now logged in as admin!', 'success')
                return redirect('home')
            else:
                return "Incorrect password. Please try again."
        else:
            return "Admin username not found. Please register as admin."

    return render_template('admin.html')


#-----------------for logout-----------------------------------------------------------------------------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        mobile_number = request.form['mobile_number']
        city = request.form['city']
        email = request.form['email']
        user_type = request.form['user_type']

        # Check if both username and password already exist
        cursor.execute("SELECT name, password FROM users WHERE name=%s", (username,))
        user_data = cursor.fetchone()

        if user_data:
            stored_password = user_data[1].encode('utf-8')
            if bcrypt.checkpw(password.encode('utf-8'), stored_password):
                return "Username and password already exist. You can log in now."

        # Commit any pending changes from previous queries
        db.commit()

        # Hash the password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Insert the new user into the database
        insert_query = "INSERT INTO users (name, password, mobile_number, city, email, user_type) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (username, hashed_password, mobile_number, city, email, user_type))

        # Commit the transaction after the INSERT query
        db.commit()
        return render_template('login_page.html')

    return render_template('registerbutton.html')

@app.route('/user', methods=['GET', 'POST'])
def user():
    if 'username' in session:
        name = session['username']

        try:
            # Use context manager for database connection
            with mysql.connector.connect(**db_config) as db, db.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM users WHERE name = %s", (name,))
                user_details = cursor.fetchone()

                if user_details:
                    # Pass user details to the HTML template
                    return render_template('user_details.html', user=user_details)
                else:
                    return "User not found"
        except mysql.connector.Error as err:
            # Handle database errors (log or provide user feedback)
            print(f"Error: {err}")
            return "Database error"
    else:
        return redirect(url_for('login'))  # Redirect to login page if not logged in


    


#-------------------------------bus_detail___________________________________________________________
@app.route('/bus_details', methods=['GET', 'POST'])
@requires_role(['Admin'])
def bus_details():
    msg =None
    bus_data = None
    # Get the current page from the query parameters, default to 1
    page = int(request.args.get('page', 1))

    # Set the number of items per page
    per_page = 10 # You can adjust this based on your preference

    # Calculate the OFFSET based on the current page
    offset = (page - 1) * per_page

    # Execute the SELECT query with LIMIT and OFFSET clauses
    cursor = db.cursor(dictionary=True)
    if page > 0 :
        cursor.execute(f"SELECT * FROM bus_detail LIMIT {per_page} OFFSET {offset}")
        bus_data = cursor.fetchall()
    else :
        msg = flash("Enter a valid page number ")

    # Count the total number of items
    cursor.execute("SELECT COUNT(*) FROM bus_detail")
    total_items = cursor.fetchone()['COUNT(*)']

    # Calculate the total number of pages
    total_pages = (total_items + per_page - 1) // per_page

    cursor.close()

    # print(bus_data)
    # print(page)
    # print(per_page)
    # print(total_pages)

    # Modify the bus_data to be in title case
    if bus_data :
        for bus in bus_data:
            if bus['departure_time']:
                departure_datetime = datetime(1, 1, 1) + bus['departure_time']
                bus['departure_time'] = departure_datetime.strftime('%H:%M')  # Format as HH:MM
            if bus['arrival_time']:
                arrival_datetime = datetime(1, 1, 1) + bus['arrival_time']
                bus['arrival_time'] = arrival_datetime.strftime('%H:%M')  # Format as HH:MM

            for key, value in bus.items():
                if isinstance(value, str):
                    bus[key] = value.title()

    return render_template('bus_detail.html', bus_data=bus_data, page=page, per_page=per_page, total_pages=total_pages , msg=msg)



#----------------------------------for adding bus-------------------------------------------------------------------   

@app.route('/add_bus',methods=['GET','POST'])

def add_bus_form():
    if request.method == 'POST':
        # bus_id = request.form['bus_id']
        # driver_id = request.form['driver_id']
        # conductor_id = request.form['conductor_id']
        bus_number = request.form['bus_number']
        bus_model = request.form['bus_model']
        seating_capacity = request.form['seating_capacity']
        route = request.form['route']
        departure_time = request.form['departure_time']
        arrival_time = request.form['arrival_time']
        cursor = db.cursor(dictionary=True)
        query = "SELECT * FROM bus_detail WHERE bus_number=%s"
        cursor.execute(query, (bus_number,))
        existing_bus = cursor.fetchall()

        if existing_bus:
            error_message = f"Bus number '{bus_number}' already exists with model '{existing_bus['bus_model']}' and route '{existing_bus['route']}'. change number."
            flash(error_message, 'error') 
            return render_template('add_bus_form.html')  
        else:         
            if arrival_time <= departure_time:
                flash('Departure time must be before  than Arrival time', 'error')
            else:
                query = 'INSERT INTO bus_detail ( bus_number, bus_model, seating_capacity, route, departure_time, arrival_time) VALUES ( %s, %s, %s, %s, %s, %s)'
                cursor.execute(query,(bus_number,bus_model,seating_capacity,route,departure_time,arrival_time)) 
                db.commit()
                # flash('bus-detail added successfully', 'success')
                # return redirect(url_for('bus_details'))
                return redirect(url_for('bus_details'))
    return render_template('add_bus_form.html')    

#-------------------------------------------------for editing bus ---------------------------------------------------------------------------------
 
@app.route('/update_bus/<int:bus_id>', methods=['GET', 'POST'])

def update_bus(bus_id):
    cursor = db.cursor(dictionary=True)
    if request.method == 'POST':
        route = request.form['route']
        departure_time = request.form['departure_time']
        arrival_time = request.form['arrival_time']
        if arrival_time >= departure_time:
            flash(' Departure  time must be before than Arrival time', 'error')
        else:
            query = 'UPDATE bus_detail SET route=%s, departure_time=%s, arrival_time=%s WHERE bus_id = %s'
            cursor.execute(query, (route, departure_time, arrival_time, bus_id))
            db.commit()
            # flash('Bus details updated successfully', 'success')
            # return redirect(url_for('bus_details'))
            return redirect(url_for('bus_details'))
    query1 = 'SELECT * FROM bus_detail WHERE bus_id = %s'
    cursor.execute(query1, (bus_id,))
    bus = cursor.fetchone()
    return render_template('edit_bus_form.html', bus=bus)

  
#---------------------------------------for deleting bus----------------------------------------------------------------------------------
@app.route('/success')
def success_page():
    return render_template('success.html')


@app.route('/delete_bus/<int:bus_id>', methods=['GET','POST'])

def delete_bus(bus_id):
    try:
        # Delete the bus record from the database
        cursor = db.cursor()
        query = "DELETE FROM bus_detail WHERE bus_id = %s"
        cursor.execute(query, (bus_id,))
        db.commit()
        cursor.close()
        
        # flash("platform deleted successfully.", "success")
        # return redirect(url_for('platform_details'))
        return redirect(url_for('bus_details'))
    except Exception as e:
        db.rollback()
        flash(f"An error occurred while deleting the bus.:{e}", "error")
        return redirect(url_for('bus_details'))
    
    
   
#----------------------------------platform detail manipulation----------------------------------------------


@app.route('/platform_details', methods=['GET', 'POST'])

def platform_details():
    platform_data=None
    msg=None
    # Get the current page from the query parameters, default to 1
    page = int(request.args.get('page', 1))

    # Set the number of items per page
    per_page = 10  # You can adjust this based on your preference

    # Calculate the OFFSET based on the current page
    offset = (page - 1) * per_page

    # Execute the SELECT query with LIMIT and OFFSET clauses
    cursor = db.cursor(dictionary=True)
    if page>0:
        query = f"SELECT * FROM platform LIMIT {per_page} OFFSET {offset}"
        cursor.execute(query)
        platform_data = cursor.fetchall()
    else :
        msg = flash("Enter a valid page number ")    

    # Count the total number of items
    cursor.execute("SELECT COUNT(*) FROM platform")
    total_items = cursor.fetchone()['COUNT(*)']

    # Calculate the total number of pages
    total_pages = (total_items + per_page - 1) // per_page

    cursor.close()
    if platform_data:
        for platform in platform_data:
            for key, value in platform.items():
                if isinstance(value, str):
                    platform[key] = value.title()


    return render_template('platform.html', platform_data=platform_data,page=page, per_page=per_page, total_pages=total_pages ,msg=msg)

#--------------------------------------------------for adding platform------------------------


@app.route('/add_platform', methods=['GET', 'POST'])

def add_platform():
    if request.method == 'POST':
         # platform_id = request.form['platform _id']
        platform_number = request.form['platform_number']
        location = request.form['platform_name']
        cursor = db.cursor(dictionary=True)
        # Assuming platform_id is an auto-increment primary key, you don't need to specify it in the INSERT statement
        query = 'INSERT INTO platform(platform_number, location) VALUES (%s, %s)'
        cursor.execute(query, (platform_number, location))
        db.commit()
        flash('Platform detail added successfully', 'success')
        # return redirect(url_for('platform_details'))
        return redirect(url_for('platform_details'))
    return render_template('add_platform_form.html')   

#--------------------for editing this platform----------------------------------------
from flask import render_template, request, redirect, url_for

@app.route('/update_platform/<int:platform_id>', methods=['GET', 'POST'])
def update_platform(platform_id):
    cursor = db.cursor(dictionary=True)

    if request.method == 'POST':
        platform_number = request.form['platform_number']
        location = request.form['location']

        # Assuming both fields can be updated simultaneously
        query = 'UPDATE platform SET platform_number = %s, location = %s WHERE platform_id = %s'
        cursor.execute(query, (platform_number, location, platform_id))
        db.commit()

        return redirect(url_for('platform_details'))

    query1 = 'SELECT * FROM platform WHERE platform_id = %s'
    cursor.execute(query1, (platform_id,))
    platform_data = cursor.fetchone()

    return render_template('editplatform.html', platform_data=platform_data)



#-------------------------------------delete platform---------------------------

@app.route('/delete_platform/<int:platform_id>', methods=['GET','POST'])

def delete_platform(platform_id):
    try:
        # Delete the bus record from the database
        cursor = db.cursor()
        query = "DELETE FROM platform WHERE platform_id = %s"
        cursor.execute(query, (platform_id,))
        db.commit()
        cursor.close()
        
        # msg = flash("platform deleted successfully.", "success")
        # # return redirect(url_for('platform_details'))
        # print("work")
        return redirect(url_for('platform_details'))
    except Exception as e:
        db.rollback()
        msg = flash(f"An error occurred while deleting the bus.:{e}", "error")
        return render_template('platform.html') 
    
    
#-------------------------------route manipulation--------------------------------------------------------------

# Create a new route for ticket routes

@app.route('/ticket_routes', methods=['GET', 'POST'])
def ticket_routes():
    # Get the current page from the query parameters, default to 1
    page = int(request.args.get('page', 1))

    # Set the number of items per page
    per_page = 10  # You can adjust this based on your preference

    # Calculate the OFFSET based on the current page
    offset = (page - 1) * per_page

    # Execute the SELECT query with LIMIT and OFFSET clauses
    cursor = db.cursor(dictionary=True)
    query = f"SELECT route FROM bus_detail LIMIT {per_page} OFFSET {offset}"
    cursor.execute(query)
    ticket_data = cursor.fetchall()

    # Count the total number of items
    cursor.execute("SELECT COUNT(*) FROM bus_detail")
    total_items = cursor.fetchone()['COUNT(*)']

    # Calculate the total number of pages
    total_pages = (total_items + per_page - 1) // per_page

    cursor.close()
    for ticket in ticket_data:
        for key,value in ticket.items():
            if isinstance(value,str):
                ticket[key]=value.title()


    return render_template('ticket.html', ticket_data=ticket_data, page=page, per_page=per_page, total_pages=total_pages)



@app.route('/home')
def homee():
    return render_template ('index1.html')


@app.route('/route_details', methods=['POST'])
def route_details():
    if request.method == 'POST':
        selected_route = request.form['selected_route']
 
        # Fetch details for the selected route from the database
        cursor = db.cursor(dictionary=True)
        cursor.execute(f'SELECT  bus_id,bus_number,bus_model,seating_capacity, departure_time, arrival_time FROM bus_detail WHERE route= "{selected_route}";')
        route_details = cursor.fetchall()

        # Close the cursor after fetching results
        cursor.close()
        for bus in route_details:
            if bus['departure_time']:
                departure_datetime = datetime(1, 1, 1) + bus['departure_time']
                bus['departure_time'] = departure_datetime.strftime('%H:%M')  # Format as HH:MM
            if bus['arrival_time']:
                arrival_datetime = datetime(1, 1, 1) + bus['arrival_time']
                bus['arrival_time'] = arrival_datetime.strftime('%H:%M')  # Format as HH:MM

        for key, value in bus.items():
            if isinstance(value, str):
                bus[key] = value.title()

        # Pass the route details to the template and render it
        return render_template('route_details.html', route_details=route_details)

    # Handle the case where the route_details page is directly accessed without a POST request
    return render_template('error_page.html', error_message='Invalid Access')

#-----------------------------this is for open bus detail of particular bus------------------------------------

@app.route("/search") #our first directry which is open

def index():
    return render_template("particular_bus.html")#it will though us to the html page which is open at first
# Change the return statement in getting_data route@app.route("/search", methods=['GET', 'POST'])

@app.route("/search", methods=['GET', 'POST'])
def getting_data():
    result = []

    if request.method == 'POST':
        route = request.form.get('route')

        if not route:
            # Handle the case where no route is provided
            return render_template_string('<p>Invalid route</p>')

        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()

            cursor.execute(f'SELECT bus_id, bus_number, seating_capacity, departure_time, arrival_time FROM bus_detail WHERE route= "{route}";')
            result = cursor.fetchall()

        except mysql.connector.Error as e:
            # Handle the error as needed
            print(f"Error: {e}")

        finally:
            cursor.close()
            connection.close()

        if result:
            # Render the partial_buses.html template if buses were found
            partial_buses_content = render_template('partial_buses.html', result=result)
            return partial_buses_content.replace('<body>', '').replace('</body>', '')
        else:
            # Display a message if no buses match the route
            return render_template_string('<p>No buses found for the selected route</p>')

    # Handle other request methods as needed
    return render_template_string('<p>Invalid request</p>')

#----------------------------serch using time------------------------------------------






from flask import Flask, render_template, request, flash
from datetime import datetime, timedelta, time

@app.route('/time_buses', methods=['GET', 'POST'])
def bus_search():
    messages =None
    if request.method == 'POST':
        start_time = request.form['start_time']
        end_time = request.form['end_time'] if request.form['end_time'] else None

        try:
            start_time_obj = datetime.strptime(start_time, '%H:%M').time()
            end_time_obj = datetime.strptime(end_time, '%H:%M').time() if end_time else None
        except ValueError:
            messages="Invalid time format. Please enter time in HH:MM format."
            return render_template('time_search.html',messages=messages)

        # Construct query based on input times
        query = "SELECT * FROM bus_detail"
        if not end_time_obj:
            query += f" WHERE departure_time BETWEEN '{start_time}' AND '{(datetime.min + timedelta(hours=1)).time()}'"
        else:
            query += f" WHERE departure_time BETWEEN '{start_time}' AND '{end_time}'"

        cursor.execute(query)
        result = cursor.fetchall()
    

        if not result:
            return render_template_string('<p>No buses found within the specified time range.</p>')
        else:
            return render_template('time_slot.html', result=result)

    return render_template('time_search.html' ,messages=messages)

#-----------------------------------time_slot---------------------------------------------


#--------------------for bus-pass from services------------------------------------------

@app.route('/services', methods=['GET', 'POST'])

def services():
    if request.method == 'POST':
        # Process the form data and insert it into the database
        name = request.form['name']
        email = request.form['email']
        aadhar = request.form['aadhar-number']
        address = request.form['address']
        user_type = request.form['userType']

        cursor = db.cursor()
        insert_query = "INSERT INTO bus_pass (name, email, aadhar, address, user_type) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (name, email, aadhar, address, user_type))
        db.commit()
        cursor.close() 
        return render_template('success1.html')  # Return the success.html template
    
    if request.method == 'GET' and request.args.get('refresh'):
        return redirect(url_for('services'))  # Re-render the services page


    return redirect('home')  # Render the form for data submission


                

#----------------------THIS IS FOR CONTACT DETAIL-----------------------
@app.route('/contact', methods=['GET', 'POST'])

def contact():
    if request.method == 'POST':
        # Get data from the form using correct keys
        name = request.form['name']  # Use 'name' instead of 'Name'
        email = request.form['email']  # Use 'email' instead of 'Email'
        subject = request.form['subject']  # Use 'subject' instead of 'Subject'
        message = request.form['message']  # Use 'message' instead of 'Message'
        try:
            cursor = db.cursor()
            insert_query = "INSERT INTO Queries (name, email, subject, message) VALUES (%s, %s, %s, %s)"
            cursor.execute(insert_query, (name, email, subject, message))    
            flash('Contact details submitted successfully !!', 'success')
            db.commit()
            cursor.close()
            return redirect(url_for('contact'))  # Return the success.html template
        except mysql.connector.Error as e:
            return f"An error occurred while inserting data: {str(e)}"
        finally:
            if cursor:
                cursor.close()
    return render_template('index1.html')

@app.route('/query', methods=['GET', 'POST'])

def query():
    if request.method == 'POST':
        email = request.form['email']
        message = request.form['message']
        cursor = db.cursor()

        # Email doesn't exist, proceed with insertion
        insert_query = "INSERT INTO contact(email, message) VALUES (%s, %s)"
        cursor.execute(insert_query, (email, message))

        # Commit the changes and close the cursor
        db.commit()
        cursor.close()  

        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return 'Thank you for leaving the message we will try our best to go through your comment.'
        else:
            return render_template_string('<p>Thank you for leaving the message we will try our best to go through your comment.</p>')
        

    return redirect(url_for('home'))
@app.route('/thank_you' ,methods=['GET', 'POST'])
def thank_you():
    return 'Thank you for leaving the message we will try our best to go through your comment.'


@app.route('/thanks' )
def thanks():
    return 'Thank you for coming on my website .'



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)