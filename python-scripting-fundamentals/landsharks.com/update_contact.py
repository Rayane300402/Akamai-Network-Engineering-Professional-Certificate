#!/var/www/landsharks.com/venv/bin/python
import mysql.connector
import cgi, cgitb

cgitb.enable()

print("Content-type:text/html")
print("")
print("<html><head>")
print('<meta http-equiv="content-type" content="text/html; charset=utf-8">')
print('<link rel="stylesheet" type="text/css" href="styles.css">')
print("<title>LAN Sharks App</title>")
print("</head>")

# header
with open("/var/www/landsharks.com/pageStart.htm", "r") as f:
    for line in f:
        print(line.rstrip("\n"))

form = cgi.FieldStorage()
userName = (form.getfirst("userName") or "").strip().lower()

# fields (if POSTed they will be present)
companyName = form.getfirst("companyName")
address     = form.getfirst("address")
city        = form.getfirst("city")
state       = form.getfirst("state")
zipCode     = form.getfirst("zipCode")
email       = form.getfirst("email")
phone       = form.getfirst("phone")

def show_error(msg):
    print('<h2 class="heading">Something Went Wrong</h2>')
    print(f'<p class="description">{msg}</p>')
    print(f'<p class="description">Click <a href="main_return.py?userName={userName}" style="color:#FFD700;">here</a> to go back.</p>')

def show_success(full_name):
    print('<h2 class="heading">Contact Information Updated!</h2>')
    print(f'<p class="description">{full_name}, you have successfully changed your contact information!</p>')
    print(f'<p class="description"><a href="main_return.py?userName={userName}" style="color:#FFD700;">Click here to go back to the main page</a></p>')

def show_form(cust):
    full_name = f"{cust['firstName']} {cust['lastName']}"
    print(f'<h2 class="heading">{full_name}</h2>')
    print(f'<p class="description"><b>User Name:</b> {userName}</p>')

    print('<form class="loginform" action="update_contact.py" method="post">')
    print(f'<input type="hidden" name="userName" value="{userName}">')

    print(f'<p><label>Company Name:</label> '
          f'<input type="text" name="companyName" size="50" value="{cust["companyName"] or ""}"></p>')
    print(f'<p><label>Address:</label> '
          f'<input type="text" name="address" size="50" value="{cust["address"] or ""}"></p>')
    print(f'<p><label>City:</label> '
          f'<input type="text" name="city" size="20" value="{cust["city"] or ""}"> '
          f'<label style="margin-left:20px;">State:</label> '
          f'<input type="text" name="state" size="15" value="{cust["state"] or ""}"> '
          f'<label style="margin-left:20px;">ZIP code:</label> '
          f'<input type="text" name="zipCode" size="10" value="{cust["zipCode"] or ""}"></p>')
    print(f'<p><label>E-mail:</label> '
          f'<input type="text" name="email" size="35" value="{cust["email"] or ""}"> '
          f'<label style="margin-left:20px;">Phone:</label> '
          f'<input type="text" name="phone" size="15" value="{cust["phone"] or ""}"></p>')

    print('<p><input class="button" type="submit" value="Update Contact Information"></p>')
    print('</form>')

# must have username
if not userName:
    show_error("Missing userName.")
else:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="python"
    )
    cur = db.cursor(dictionary=True)

    # Find the customer by email prefix "username@"
    email_pattern = f"{userName}@%"
    cur.execute("SELECT * FROM customers WHERE email LIKE %s LIMIT 1", (email_pattern,))
    cust = cur.fetchone()

    if not cust:
        show_error("Customer record not found.")
    else:
        # If no POST fields present, show the form (GET)
        is_submit = any(v is not None for v in [companyName, address, city, state, zipCode, email, phone])

        if not is_submit:
            show_form(cust)
        else:
            # Update customer row by customerNumber (best key)
            cur.execute("""
                UPDATE customers
                SET companyName=%s, address=%s, city=%s, state=%s, zipCode=%s, email=%s, phone=%s
                WHERE customerNumber=%s
            """, (
                companyName, address, city, state, zipCode, email, phone,
                cust["customerNumber"]
            ))
            db.commit()

            full_name = f"{cust['firstName']} {cust['lastName']}"
            show_success(full_name)

    cur.close()
    db.close()

# footer
with open("/var/www/landsharks.com/pageEnd.htm", "r") as f:
    for line in f:
        print(line.rstrip("\n"))

print("</html>")

