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
old_pw   = form.getfirst("oldPassword") or ""
new_pw   = form.getfirst("newPassword") or ""
conf_pw  = form.getfirst("confirmPassword") or ""

def show_error():
    
    print('<h2 class="heading">Something Went Wrong</h2>')
    print('<p class="description">Uh oh, something went wrong. Your password was not changed.</p>')
    print('<p class="description">Click <a href="main_return.py?userName=%s" style="color:#FFD700;">here</a> to return to the main page.</p>' % userName)

def show_success(full_name):
  
    print('<h2 class="heading">Password Changed!</h2>')
    print(f'<p class="description">{full_name}, you have successfully changed your password!</p>')
    print('<p class="description"><a href="main_return.py?userName=%s" style="color:#FFD700;">Click here to go back to the main page</a></p>' % userName)

def show_form(full_name):
    
    print(f'<h2 class="heading">{full_name}</h2>')
    print(f'<p class="description"><b>User Name:</b> {userName}</p>')

    print('<form class="loginform" action="change_password.py" method="post">')
    print(f'<input type="hidden" name="userName" value="{userName}">')

    print('<p><label for="oldPassword">Old Password:</label> '
          '<input type="password" id="oldPassword" name="oldPassword" required></p>')

    print('<p><label for="newPassword">New Password:</label> '
          '<input type="password" id="newPassword" name="newPassword" required></p>')

    print('<p><label for="confirmPassword">Confirm New Password:</label> '
          '<input type="password" id="confirmPassword" name="confirmPassword" required></p>')

    print('<p><input class="button" type="submit" value="Change Password"></p>')
    print('</form>')

# no username -> cannot proceed
if not userName:
    show_error()
else:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="python"
    )
    cur = db.cursor(dictionary=True)

    # get display name (employee or customer)
    email_pattern = f"{userName}@%"
    cur.execute("SELECT firstName, lastName FROM employees WHERE email LIKE %s LIMIT 1", (email_pattern,))
    person = cur.fetchone()
    if not person:
        cur.execute("SELECT firstName, lastName FROM customers WHERE email LIKE %s LIMIT 1", (email_pattern,))
        person = cur.fetchone()

    full_name = f"{person['firstName']} {person['lastName']}" if person else userName

    # If no POST fields yet, show the form
    if old_pw == "" and new_pw == "" and conf_pw == "":
        show_form(full_name)
    else:
        # Validate old password
        cur.execute("SELECT password FROM users WHERE userName = %s LIMIT 1", (userName,))
        u = cur.fetchone()

        if not u:
            show_error()
        elif old_pw != u["password"]:
            show_error()
        elif new_pw != conf_pw:
            show_error()
        else:
            # Update password
            cur.execute("UPDATE users SET password = %s WHERE userName = %s", (new_pw, userName))
            db.commit()
            show_success(full_name)

    cur.close()
    db.close()

# footer
with open("/var/www/landsharks.com/pageEnd.htm", "r") as f:
    for line in f:
        print(line.rstrip("\n"))

print("</html>")

