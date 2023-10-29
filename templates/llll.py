

-- Create the 'conductor' table
CREATE TABLE conductor (
    conductor_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    contact_number VARCHAR(40),
    email VARCHAR(100),
    hire_date DATE,
    salary DECIMAL(10, 2)
);

-- Create the 'driver' table
CREATE TABLE driver (
    driver_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    contact_number VARCHAR(50),
    email VARCHAR(100),
    hire_date DATE,
    license_number VARCHAR(20),
    license_expiry_date DATE
);

-- Create the 'platform' table
CREATE TABLE platform (
    platform_id INT AUTO_INCREMENT PRIMARY KEY,
    platform_number VARCHAR(10),
    location VARCHAR(255)
);

-- Create the 'bus_detail' table
CREATE TABLE bus_detail (
    bus_id INT AUTO_INCREMENT PRIMARY KEY,
    driver_id INT,
    conductor_id INT,
    bus_number VARCHAR(20),
    bus_model VARCHAR(50),
    seating_capacity INT,
    route VARCHAR(255),
    departure_time TIME,
    arrival_time TIME,
    FOREIGN KEY (driver_id) REFERENCES driver(driver_id),
    FOREIGN KEY (conductor_id) REFERENCES conductor(conductor_id)
);

-- Create the 'ticket' table
CREATE TABLE ticket (
    ticket_id INT AUTO_INCREMENT PRIMARY KEY,
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
    FOREIGN KEY (bus_id) REFERENCES bus_detail(bus_id),
    FOREIGN KEY (conductor_id) REFERENCES conductor(conductor_id),
    FOREIGN KEY (driver_id) REFERENCES driver(driver_id),
    FOREIGN KEY (platform_id) REFERENCES platform(platform_id)
);

-- Create the 'Queries' table (if needed)
CREATE TABLE Queries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    subject VARCHAR(255),
    message TEXT
);

-- Create the 'bus_pass' table (if needed)
CREATE TABLE bus_pass (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    aadhar VARCHAR(12),
    address TEXT,
    user_type VARCHAR(255)
);
