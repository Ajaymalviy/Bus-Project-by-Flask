# Bus-Project-by-Flask
#project overview
The Bus Management System is a web application designed to streamline the management of bus-related operations. This system facilitates the efficient handling of bus routes, schedules, and passenger information through a user-friendly interface. The project incorporates essential features such as CRUD operations, pagination, and robust authentication mechanisms to ensure secure access.


## Table of Contents

1. [Introduction](#introduction)
2. [Technology Stack](#technology-stack)
3. [Project Structure](#project-structure)
4. [Prerequisites](#prerequisites)
5. [Installation](#installation)
6. [Database Initialization and Configuration](#database-initialization-and-configuration)
7. [Running the Application](#running-the-application)
8. [Functionalities](#functionalities)

## Introduction

The BMS Application simplifies bus data management by offering an intuitive web-based interface. Users can effortlessly perform CRUD operations on the following key components:

- Bus conductor
- Bus driver
- Bus platform
- Bus time
- Bus route


This application ensures that bus-related data can be easily viewed, added, edited, or deleted, with an added layer of security through user authentication.

## Technology Stack

### Frontend

- HTML
- CSS

### Backend

- Python
- Flask (Web Framework)
- MySQL (Database)

## Project Structure

The project directory includes the following files and directories:

- `init.py`: The main application file that initializes the Flask instance and connects various functionalities ,and containig all the sub files of another tables such as bus-detail,platform,etc.
- `utile.py`: Contains views for login,register and authentication .
-

##### Directory 
- `templates` : This directory contain all the HTML files.
- `static` : This directory contain CSS and image files.

## Prerequisites

Before proceeding with the installation and execution of the application, ensure you have the following dependencies installed on your system:

- Python 3.x
- Git
- MySQL server installed and running.

## Installation

1. Clone the GitHub repository to your desired location:

   ```bash
   git clone https://github.com/Ajaymalviy/Bus-Project-by-Flask.git
   ```

2. Navigate to the "BMS" directory:

   ```bash
   cd Bus-Project-by-Flask
   ```

3. Install the required packages and libraries by executing:

   ```bash
   pip install -r requirements.txt
   ```

## Database Initialization and Configuration

Before running the application, it's essential to initialize the database and configure the connection. Follow these steps:

1. Import the database schema by running the SQL script (`QUERIES.SQL`) provided in the repository. This script will set up the required tables and initial data.
##### (a) Using MySQL Interpreter

1. **Login to MySQL Interpreter**

    ```bash
    mysql -u root -p
    ```
    
4. **Import the SQL script**

    ```sql
    source /path/to/QUERIES.SQL;
    ```


#### After importing the database, update the database configuration as mentioned in the next step.    

3. Update the MySQL database configuration in the `inti.py` file. Open `int.py` and provide your MySQL database connection details as follows:

   ```python
   db_config = {
       "host": "your_database_host",
       "user": "your_database_user",
       "password": "your_database_password",
       "database": "your_database_name"
   }
   ```

   Save the changes.

## Running the Generator file  
   ```bash
   python3 generator.py
   ```

## Running the Application

To launch the application, execute the following command:

   ```bash
   flask --app init.py run
   ```

This command will start the Flask development server, and you can access the BMS Application in your web browser at http://localhost:5000.

## Functionalities

The BMS Application offers the following essential functionalities:

1. Manage Bus-driver
2. Manage Bus-conductor
3. Manage Bus-time
4. Manage Bus-platforms
5. Searching 


Users can easily perform CRUD operations on these components, enabling them to add, view, update, or delete entries as necessary.
