#!/var/www/landsharks.com/venv/bin/python
#!/usr/bin/env python3
import mysql.connector
import cgi, cgitb

print('Content-type:text/html')
print('')
print('')
print('')
print('<html>')
print('<head>')
print('<meta http-equiv="content-type" content="text/html; charset=utf-8">')
print('<link rel="stylesheet" type="text/css" href="styles.css">')
print('<title>Success</title>')
print('</head>')

with open('/var/www/landsharks.com/pageStart.htm', 'r') as start:
    content = start.readlines()
    
for i in content:
    print(i.rstrip('\n'))
    
form = cgi.FieldStorage()
firstName = form.getvalue('FirstName')
lastName = form.getvalue('LastName')
companyName = form.getvalue('CompanyName')
address = form.getvalue('Street')
city = form.getvalue('City')
state = form.getvalue('State')
zipCode = form.getvalue('ZIP')
email = form.getvalue('Email')
phone = form.getvalue('Phone')
comments = form.getvalue('Comments')

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'python'
)

cursor = db.cursor()

sql = 'INSERT INTO customers (firstName, lastName, companyName, address, city, state, zipCode, email, phone, comments) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

value = (str(firstName), str(lastName), str(companyName), str(address), str(city), str(state), str(zipCode), str(email), str(phone), str(comments))

cursor.execute(sql, value)
db.commit()

sql = "SELECT customerNumber FROM customers WHERE firstName = '"+str(firstName)+"' AND lastName = '"+str(lastName)+"' AND companyName = '"+str(companyName)+"'"

cursor.execute(sql)
customerNumber = cursor.fetchone()

customerNumber = customerNumber[0]

firstName = str(firstName)
lastName = str(lastName)

userName = firstName[0].lower()+lastName.lower()

sql = 'INSERT INTO users (userID, userName, password, type) VALUES (%s, %s, %s, %s)'
value = (customerNumber, userName, 'P@ssw0rd', 'c')

cursor.execute(sql, value)
db.commit()

print('<h2 class="heading">Application Successful!</h2>')
print('<p class="description">Your user name is: &quot;'+userName+'&quot; and your temporary password is: &quot;P@ssw0rd&quot;. You can click <a href="http://www.lansharks.com/login.htm" style="color: #FFD700;">here</a> to login.</p>')

with open('/var/www/landsharks.com/pageEnd.htm', 'r') as end:
    content = end.readlines()

for i in content:
    print(i.rstrip('\n'))

cursor.close()
db.close()
