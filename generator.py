import mysql.connector
from faker import Faker
import random

# Create a Faker instance
fake = Faker()

# Establish a database connection
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root@123",
    database="myproject"
)

# Create a cursor object to interact with the database
cursor = db_connection.cursor()

# Function to insert random data into platform table
def insert_platform_data():
    for _ in range(50):
        platform_number = fake.unique.random_int(min=1, max=100, step=1)
        location = fake.city()

        sql = "INSERT INTO platform (platform_number, location) VALUES (%s, %s)"
        values = (platform_number, location)

        cursor.execute(sql, values)
        db_connection.commit()

# Function to insert random data into conductor table
def insert_conductor_data():
    for _ in range(80):
        first_name = fake.first_name()
        last_name = fake.last_name()
        contact_number = fake.phone_number()
        email = fake.email()
        hire_date = fake.date_of_birth(minimum_age=18, maximum_age=65)
        salary = round(random.uniform(20000, 50000), 2)

        sql = "INSERT INTO conductor (first_name, last_name, contact_number, email, hire_date, salary) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (first_name, last_name, contact_number, email, hire_date, salary)

        cursor.execute(sql, values)
        db_connection.commit()

# Function to insert random data into driver table
def insert_driver_data():
    for _ in range(80):
        first_name = fake.first_name()
        last_name = fake.last_name()
        contact_number = fake.phone_number()
        email = fake.email()
        hire_date = fake.date_of_birth(minimum_age=21, maximum_age=65)
        salary = round(random.uniform(20000, 50000), 2)
        license_number = fake.unique.random_int(min=10000, max=99999, step=1)
        license_expiry_date = fake.date_of_birth(minimum_age=21, maximum_age=65)
        sql = "INSERT INTO driver (first_name, last_name, contact_number, email, hire_date, salary, license_number, license_expiry_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (first_name, last_name, contact_number, email, hire_date, salary, license_number, license_expiry_date)

        cursor.execute(sql, values)
        db_connection.commit()

# Function to insert random data into bus_detail table
def insert_bus_data():
    for _ in range(150):
        driver_id = fake.random_int(min=1, max=5)
        conductor_id = fake.random_int(min=1, max=5)
        bus_number = fake.unique.random_int(min=1000, max=9999, step=1)
        bus_model = fake.word()
        seating_capacity = random.randint(20, 60)
        route = fake.city() + " to " + fake.city()
        departure_time = fake.time(pattern="%H:%M:%S")
        arrival_time = fake.time(pattern="%H:%M:%S")

        sql = "INSERT INTO bus_detail ( driver_id,conductor_id,bus_number, bus_model, seating_capacity, route, departure_time, arrival_time) VALUES (%s, %s ,%s, %s, %s, %s, %s, %s)"
        values = (driver_id,conductor_id,bus_number, bus_model, seating_capacity, route, departure_time, arrival_time)

        cursor.execute(sql, values)
        db_connection.commit()



# Function to insert random data into ticket table
def insert_ticket_data():
    for _ in range(70):
        passenger_name = fake.name()
        source = fake.city()
        destination = fake.city()
        journey_date = fake.date_between(start_date='-30d', end_date='+30d')
        bus_id = fake.random_int(min=1, max=10)
        conductor_id = fake.random_int(min=1, max=5)
        driver_id = fake.random_int(min=1, max=5)
        platform_id = fake.random_int(min=1, max=3)
        departure_time = fake.time(pattern="%H:%M:%S")
        arrival_time = fake.time(pattern="%H:%M:%S")

        sql = "INSERT INTO ticket (passenger_name, source, destination, journey_date, bus_id, conductor_id, driver_id, platform_id, departure_time, arrival_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (passenger_name, source, destination, journey_date, bus_id, conductor_id, driver_id, platform_id, departure_time, arrival_time)

        cursor.execute(sql, values)
        db_connection.commit()

# Call functions to insert data

insert_platform_data()
insert_conductor_data()
insert_driver_data()
insert_bus_data()
insert_ticket_data()

# Close the cursor and the database connection
cursor.close()
db_connection.close()