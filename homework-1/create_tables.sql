CREATE TABLE customers_data
(
    customer_id varchar(10) PRIMARY KEY,
    company_name varchar(50) NOT NULL,
    contact_name varchar(50) NOT NULL
);

CREATE TABLE employees_data
(
    employee_id int PRIMARY KEY,
    first_name varchar(10) NOT NULL,
    last_name varchar(20) NOT NULL,
    title text NOT NULL,
    birth_date date NOT NULL,
    note text
);

CREATE TABLE orders_data
(
    order_id int PRIMARY KEY,
    customer_id varchar(10) REFERENCES customers_data(customer_id) NOT NULL,
    employee_id int REFERENCES employees_data(employee_id) NOT NULL,
    order_date date NOT NULL,
    ship_city varchar(50) NOT NULL
);

-- SQL-команды для создания таблиц
