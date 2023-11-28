-- Create the database
CREATE DATABASE myproject;

-- Use the database
USE myproject;

-- Create the 'Queries' table
CREATE TABLE Queries (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255),
    email VARCHAR(255),
    subject VARCHAR(255),
    message TEXT,
    PRIMARY KEY (id)
);

-- Create the 'conductor' table
CREATE TABLE conductor (
    conductor_id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    contact_number VARCHAR(70),
    email VARCHAR(100),
    hire_date DATE,
    salary DECIMAL(10, 2),
    PRIMARY KEY (conductor_id)
);


-- Create the 'driver' table
CREATE TABLE driver (
    driver_id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    contact_number VARCHAR(70),
    email VARCHAR(100),
    hire_date DATE,
    salary DECIMAL(10, 2),
    license_number VARCHAR(20),
    license_expiry_date DATE,
    PRIMARY KEY (driver_id)
);

-- Create the 'users' table
CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    mobile_number VARCHAR(20) NOT NULL,
    city VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    user_type VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);


-- Create the 'bus_detail' table
CREATE TABLE bus_detail (
    bus_id INT NOT NULL AUTO_INCREMENT,
    driver_id INT,
    conductor_id INT,
    bus_number VARCHAR(20),
    bus_model VARCHAR(50),
    seating_capacity INT,
    route VARCHAR(255),
    departure_time TIME,
    arrival_time TIME,
    PRIMARY KEY (bus_id),
    FOREIGN KEY (driver_id) REFERENCES driver(driver_id),
    FOREIGN KEY (conductor_id) REFERENCES conductor(conductor_id)
);

-- Create the 'bus_pass' table
CREATE TABLE bus_pass (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255),
    email VARCHAR(255),
    aadhar VARCHAR(12),
    address TEXT,
    user_type VARCHAR(255),
    PRIMARY KEY (id)
);


-- Create the 'platform' table
CREATE TABLE platform (
    platform_id INT NOT NULL AUTO_INCREMENT,
    platform_number VARCHAR(10),
    location VARCHAR(255),
    PRIMARY KEY (platform_id)
);

-- Create the 'ticket' table
CREATE TABLE ticket (
    ticket_id INT NOT NULL AUTO_INCREMENT,
    passenger_name VARCHAR(100),
    source VARCHAR(255),
    destination VARCHAR(255),
    journey_date DATE,
    bus_id INT,
    conductor_id INT,
    driver_id INT,
    platform_id INT,
    departure_time TIME,
    arrival_time TIME,
    PRIMARY KEY (ticket_id),
    FOREIGN KEY (bus_id) REFERENCES bus_detail(bus_id),
    FOREIGN KEY (conductor_id) REFERENCES conductor(conductor_id),
    FOREIGN KEY (driver_id) REFERENCES driver(driver_id),
    FOREIGN KEY (platform_id) REFERENCES platform(platform_id)
);



