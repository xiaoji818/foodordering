#This is the commands to create Postgress Database and tables.

# Create Database:
CREATE DATABASE foodordering
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_Canada.1252'
    LC_CTYPE = 'English_Canada.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

# Add Role manager and grants him all permission in DB
CREATE USER manager WITH PASSWORD 'admin';
GRANT ALL PRIVILEGES on database foodordering to manager;  
GRANT ALL PRIVILEGES on TABLE staffs to  manager; 
ALTER manager WITH SUPERUSER;


# Create Table food table to store types of food that serves customer
CREATE TABLE food (
	foodID serial PRIMARY KEY,
	foodName VARCHAR(100),
	quantity VARCHAR(50), 
	picLink VARCHAR(100),
	price DECIMAL(4,2) CHECK(price>=0)
);

#Create Table processingFood that stores the order currently being served
CREATE TABLE processingFood (
	orderID serial PRIMARY KEY,
	foodName VARCHAR(100),
	foodID INT NOT NULL CHECK (foodID>=0), 
	quantity VARCHAR(100),
	customerName VARCHAR(50) NOT NULL
);

#Create Table customers that stores the customer infomation
CREATE TABLE customers (
	customerID serial PRIMARY KEY,
	customerName VARCHAR(100) NOT NULL,
	customerPhone VARCHAR(50) NOT NULL,
	customerAddress VARCHAR(100)
);

#Create Table customers that stores the staff account and passwords 
CREATE TABLE staffs (
	s_ID serial PRIMARY KEY,
	s_name VARCHAR(100) NOT NULL,
	password VARCHAR(250) NOT null
);
