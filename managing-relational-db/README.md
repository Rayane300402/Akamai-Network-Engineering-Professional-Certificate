# Capstone Database Project – README

## Overview
This project implements a relational database for a fictitious company.  
It stores customer information, employee records, login authentication data, and network-incident logs derived from packet captures.

The database is designed to support a future security-monitoring application.

---

# 1. Database Schema Requirements

## 1.a – Customers Table
A table to store information on customers.

### Required Fields
- **id** – Primary key, INTEGER, AUTO_INCREMENT  
- **first_name**  
- **last_name**  
- **company_name**  
- **address**  
- **email**  
- **phone_number**

### Optional Fields
- Preferred method of contact  
- Facilities information (physical location info)  
- Customer devices  
- Feedback  

---

## 1.b – Employees Table
A table to store employee information.

### Required Fields
- **id** – Primary key, INTEGER, AUTO_INCREMENT  
- **first_name**  
- **last_name**  
- **email**  
- **company_position** (ex: management, technician)

### Optional Fields
- Supervisor employee number (FK)  
- Hire date  

---

## 1.c – Login Table
A table to store login credentials for customers and employees.

### Required Fields
- **username**  
- **password**  
- **customer_id** or **employee_id** – Foreign key referencing either the customers or employees table  
- **user_type** – Identifies whether the login belongs to a *customer* or an *employee*

---

## 1.d – Packet Log Fields
The application processes packet captures. Each logged packet must include:

- **event_time** – Date and time of event  
- **src_ip** – Source IP address  
- **dst_ip** – Destination IP address  
- **host_ip** – Host (local machine) IP  
- **server_ip** – Server or local-router IP  
- **src_mac** – Source MAC address  
- **dst_mac** – Destination MAC address  
- **src_port** – Source port  
- **dst_port** – Destination port  
- **protocol** – Protocol used (TCP/UDP/etc.)  
- **info** – Additional information about the packet  

---

## 1.e – Packet Data (Incidents) Table
A table to record data extracted from packet captures.

### Required Fields
- **packet_id** – Primary key, INTEGER, AUTO_INCREMENT  
- **customer_id** – Foreign key referencing customers(id)  
- All packet-capture fields listed in section **1.d**

---

# 2. Sample Records Requirements

## 2.a – Customers
At least **3 sample customers**.

## 2.b – Employees
At least **2 sample employees**.

## 2.c – Login Table
A login record for **each customer and each employee**.

## 2.d – Incidents / Packet Data
At least:
- 1 customer with **2** incident records  
- 1 customer with **3** incident records  
- 1 customer with **4** incident records  

(If you have exactly 3 customers, this results in **9 total incident rows**.)

---

# 3. Query Requirements

## 3.a
Retrieve:
- first name  
- last name  
- company name  
- email  
- username  
for **all customers**.

## 3.b
Retrieve **all employee data**, including their username.

## 3.c
Retrieve for all incident records:
- customer first name  
- customer last name  
- company name  
- source IP  
- destination IP  
- info  

## 3.d
Create a mailing list displaying:
1. First + last name (line 1)  
2. Company name (line 2)  
3. Address (next line(s))  

## 3.e
List each company name and the **count of incident records** for that customer.

## 3.f
Show the customer(s) with the **highest and lowest incident counts**, and sort by count ascending.

## 3.g
List:
- customer number  
- date of most recent incident  
- number of days since that incident (compared to current date)

