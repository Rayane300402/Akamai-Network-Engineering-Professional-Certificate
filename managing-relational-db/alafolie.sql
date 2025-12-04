/*Company Name: A la Folie*/

/*Create db*/
CREATE DATABASE alafolie;
USE alafolie;

/*1-a- Customers table*/
CREATE TABLE customers(
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
    first_name TEXT,
    last_name TEXT,
    company_name TEXT,
    address TEXT,
    email TEXT,
    phone_number TEXT
);

/*1-b- Employees Table*/
CREATE TABLE employees (
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    company_position TEXT
);

/*1-c- Login Table*/
CREATE TABLE loginInfo (
	login_id INTEGER PRIMARY KEY auto_increment,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    customer_id INTEGER,
    employee_id INTEGER,
    user_type ENUM('customer', 'employee') NOT NULL,
    foreign key(customer_id) REFERENCES customers(id),
    foreign key(employee_id) REFERENCES employees(id)
);

/*1-d-e- Create packet data*/
CREATE TABLE packet_data (
	packet_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    foreign key(customer_id) REFERENCES customers(id),
    event_time DATETIME,
    src_ip varchar(45),
    dst_ip varchar(45),
    host_ip varchar(45),
    server_ip varchar(45),
    src_mac varchar(17),
    dst_mac varchar(17),
    src_port INTEGER,
    dst_port INTEGER,
    protocol varchar(10),
    info TEXT
);

/*2-a- add 3 customers*/
INSERT INTO customers(id, first_name, last_name, company_name, address,email, phone_number)
VALUES (DEFAULT, 'John', 'Wick', 'WickCorp', 'US, Cali', 'jphhmWich12@gmail.com', '00000000');

INSERT INTO customers(id, first_name, last_name, company_name, address,email, phone_number)
VALUES (DEFAULT, 'Veronica', 'Speedwell', 'Belvedere', 'UK, London', 'veroniqueArcadia@gmail.com', '00000000');

INSERT INTO customers(id, first_name, last_name, company_name, address,email, phone_number)
VALUES (DEFAULT, 'Roman', 'Kitt', 'Inkridden', 'not sure', 'roman_c_kitt@inkriddent.com', '00000000');

/*2-a- add 3 employees*/
INSERT INTO employees (id, first_name, last_name,email, company_position) 
VALUES (DEFAULT, 'Revelstoke', 'Tempelton-Vane', 'stoker_vane@alafolie.com', 'technician');

INSERT INTO employees (id, first_name, last_name,email, company_position) 
VALUES (DEFAULT, 'Stevie', 'Bells', 'stevie_bells@alafolie.com', 'management');

/*2-c- login records*/
INSERT INTO loginInfo (login_id, username, password, customer_id, employee_id, user_type)
VALUE (default, 'john_wick', '123', 1, NULL, 'customer');

INSERT INTO loginInfo (login_id, username, password, customer_id, employee_id, user_type)
VALUE (default, 'veronicaL', '123', 2, NULL, 'customer');

INSERT INTO loginInfo (login_id, username, password, customer_id, employee_id, user_type)
VALUE (default, 'romanC', '123', 3, NULL, 'customer');

INSERT INTO loginInfo (login_id, username, password, customer_id, employee_id, user_type)
VALUE (default, 'revelstOke', '123', NULL, 1, 'employee');

INSERT INTO loginInfo (login_id, username, password, customer_id, employee_id, user_type)
VALUE (default, 'dStevie', '123', NULL, 2, 'employee');

/*2-d incidents*/
INSERT INTO packet_data(packet_id,customer_id, event_time ,src_ip ,dst_ip ,host_ip ,server_ip ,
    src_mac ,dst_mac ,src_port ,dst_port,protocol, info)
VALUE (DEFAULT, 1 ,'2023-02-08 03:20:00','172.16.137.40','172.16.137.40','DHCP','68',
'67','172.16.137.40','172.16.137.1','08:00:2b:ef:ab:7c','00:1d:7e:7c:c4:8d',
'DHCP Request  - Transaction ID 0xfe9ceb09');

INSERT INTO packet_data(packet_id,customer_id, event_time ,src_ip ,dst_ip ,host_ip ,server_ip ,
    src_mac ,dst_mac ,src_port ,dst_port,protocol, info)
VALUE (DEFAULT, 1 ,'2023-03-08 13:20:15','172.16.137.1','172.16.137.1','DHCP','67','68',
'172.16.137.1','255.255.255.255','00:1d:7e:7c:c4:8d','ff:ff:ff:ff:ff:ff',
'DHCP ACK - Transaction ID 0xfe9ceb09');

INSERT INTO packet_data(packet_id,customer_id, event_time ,src_ip ,dst_ip ,host_ip ,server_ip ,
    src_mac ,dst_mac ,src_port ,dst_port,protocol, info)
VALUE (DEFAULT, 2 ,'2023-04-08 13:20:15','172.16.137.1','172.16.137.1','DHCP','67','68',
'172.16.137.1','255.255.255.255','00:1d:7e:7c:c4:8d','ff:ff:ff:ff:ff:ff',
'DHCP ACK - Transaction ID 0xfe9ceb09');

INSERT INTO packet_data(packet_id,customer_id, event_time ,src_ip ,dst_ip ,host_ip ,server_ip ,
    src_mac ,dst_mac ,src_port ,dst_port,protocol, info)
VALUE (DEFAULT, 2 ,'2023-03-08 13:20:15','172.16.137.1','172.16.137.1','DHCP','67','68',
'172.16.137.1','255.255.255.255','00:1d:7e:7c:c4:8d','ff:ff:ff:ff:ff:ff',
'DHCP ACK - Transaction ID 0xfe9ceb09');

INSERT INTO packet_data(packet_id,customer_id, event_time ,src_ip ,dst_ip ,host_ip ,server_ip ,
    src_mac ,dst_mac ,src_port ,dst_port,protocol, info)
VALUE (DEFAULT, 2 ,'2022-08-24 10:35:30','10.100.25.14','10.100.25.14','TCP','1065','139','10.100.25.14','10.100.18.12','00:15:c5:3c:4f:9e','00:03:ff:6c:8b:24','1065  >  139 [SYN] Seq=0 Win=8 Len=0');

INSERT INTO packet_data(packet_id,customer_id, event_time ,src_ip ,dst_ip ,host_ip ,server_ip ,
    src_mac ,dst_mac ,src_port ,dst_port,protocol, info)
VALUE (DEFAULT, 3 ,'2023-09-08 13:20:15','172.16.137.1','172.16.137.1','DHCP','67','68',
'172.16.137.1','255.255.255.255','00:1d:7e:7c:c4:8d','ff:ff:ff:ff:ff:ff',
'DHCP ACK - Transaction ID 0xfe9ceb09');

INSERT INTO packet_data(packet_id,customer_id, event_time ,src_ip ,dst_ip ,host_ip ,server_ip ,
    src_mac ,dst_mac ,src_port ,dst_port,protocol, info)
VALUE (DEFAULT, 3 ,'2023-12-08 13:20:15','172.16.137.1','172.16.137.1','DHCP','67','68',
'172.16.137.1','255.255.255.255','00:1d:7e:7c:c4:8d','ff:ff:ff:ff:ff:ff',
'DHCP ACK - Transaction ID 0xfe9ceb09');

INSERT INTO packet_data(packet_id,customer_id, event_time ,src_ip ,dst_ip ,host_ip ,server_ip ,
    src_mac ,dst_mac ,src_port ,dst_port,protocol, info)
VALUE (DEFAULT, 3 ,'2022-09-10 11:32:21','192.168.137.83','192.168.137.83','HTTP','49163','80','192.168.137.83','54.10.120.45','00:21:9b:5b:d1:7a','a8:b1:d4:ac:fe:7d','HEAD /v9/windowsupdate/redir/muv4wuredir.cab?1507101531 HTTP/1.1');

INSERT INTO packet_data(packet_id,customer_id, event_time ,src_ip ,dst_ip ,host_ip ,server_ip ,
    src_mac ,dst_mac ,src_port ,dst_port,protocol, info)
VALUE (DEFAULT, 3 ,'2022-10-10 11:32:38','23.67.253.43','23.67.253.43','TCP','80','49163','54.10.120.45,192','168.137.83','a8:b1:d4:ac:fe:7d','00:21:9b:5b:d1:7a','80  >  49163 [ACK] Seq=1 Ack=174 Win=15680 Len=0');


/*3-a retrieve data from customers*/
SELECT  c.first_name, c.last_name, c.company_name, c.email, l.username
FROM customers AS c
JOIN login AS l
	ON l.customer_id = c.id
    AND l.user_type = 'customer';
    
/*3-b- all data from employees + login*/
SELECT  e.*, l.username
FROM employees AS e
JOIN login AS l
	ON l.employee_id= c.id
    AND l.user_type = 'employee';

/*3-c- customer data and info from packet_data*/
SELECT  c.first_name, c.last_name, c.company_name, c.email,
	p.src_ip, p.dst_ip, p.info
FROM customers AS c
JOIN packet_data AS p
	ON p.customer_id = c.id;
    
/*3-d- mail list creation for all customer*/
SELECT 
	CONCAt(c.first_name, ' ', c.last_name, '\n',
			c.company_name, '\n',
            c.address
    ) AS mailing_label
FROM customers as c;

/*3-e- list company name and count f incident */
SELECT c.company_name,
COUNT(p.packet_id) AS incident_count
FROM customers AS c
LEFT JOIN packet_data AS p
	ON p.customer_id = c.id
GROUP BY c.id, c.company_name;

/*3-f customer name with highest and lowest incident count*/
WITH customer_counts AS (
	SELECT c.id, c.company_name,
    COUNT(p.packet_id) AS total_incidents
    FROM customers AS c
    LEFT JOIN packet_data AS p
	ON p.customer_id = c.id
	GROUP BY c.id, c.company_name
)
 SELECT company_name, total_incidents 
 FROM customer_counts
 WHERE total_incidents = (SELECT MIN(total_incidents) FROM customer_counts)
	OR
		total_incidents = (SELECT MAX(total_incidents) FROM customer_counts)
ORDER By total_incidents ASC;

/*3-g- customer $ and date of msot recent incident and days since thenn*/
SELECT p.customer_id AS customer_number,
		MAX(p.event_times) AS last_incident_date,
        DATEDIFF(curdate(), max(p.event_time)) AS days_since_last_incident
FROM packet_data as p
group by p.customer_id;







