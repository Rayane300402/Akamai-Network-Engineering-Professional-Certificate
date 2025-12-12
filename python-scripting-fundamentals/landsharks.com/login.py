#!/var/www/landsharks.com/venv/bin/python
import mysql.connector
import cgi, cgitb

cgitb.enable()

print('Content-type:text/html')
print('')
print('')
print('')
print('<html>')
print('<head>')
print('<meta http-equiv="content-type" content="text/html; charset=utf-8">')
print('<link rel="stylesheet" type="text/css" href="styles.css">')
print('<title>LAN Sharks App</title>')
print('</head>')

with open('/var/www/landsharks.com/pageStart.htm', 'r') as start:
    content = start.readlines()
    
for i in content:
    print(i.rstrip('\n'))
    
form = cgi.FieldStorage()
userName = (form.getfirst('UserName') or '').strip().lower()
password = form.getfirst('Password') or ''
employee_checkbox = form.getfirst('employee') 



if not userName or not password:
    # missing creds -> treat as bad login
    print('<h2 class="heading">Authentication Failed</h2>')
    print('<p class="description">Click '
          '<a href="login.htm" style="color: #FFD700;">here</a> to retry.</p>')
else:
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='python'
    )

    # dictionary=True lets us address columns by name
    cursor = db.cursor(dictionary=True)

    sql = """
        SELECT userName, password, type
        FROM users
        WHERE userName = %s AND password = %s
    """
    cursor.execute(sql, (userName, password))
    row = cursor.fetchone()

    if not row:
        # ---------- WRONG USER/PASS (Image 2) ----------
        print('<h2 class="heading">Authentication Failed</h2>')
        print('<p class="description">Click '
              '<a href="login.htm" style="color: #FFD700;">here</a> to retry.</p>')
    else:
        # your "type" column: 'e' = employee, 'c' = customer
        user_type = (row['type'] or '').lower()
        is_employee = (user_type == 'e')

        if is_employee and not employee_checkbox:
            # ---------- EMPLOYEE DIDN'T CHECK BOX (Image 1) ----------
            print('<h2 class="heading">Something Went Wrong</h2>')
            print('<p class="description">'
                  'Uh oh, something went wrong. If you are an employee, make sure you '
                  'checked the employee box on the login page. If you are not, please '
                  'do not check the box.'
                  '</p>')
            print('<p class="description">Click '
                  '<a href="login.htm" style="color: #FFD700;">here</a> to retry.</p>')
        else:
            # ---------- SUCCESSFUL LOGIN ----------
            # Decide employee flag from DB
            employee_flag = 'True' if is_employee else 'False'

            print('<form class="loginform" action="main.py" method="post">')
            print(f'<input type="hidden" id="userName" name="userName" value="{userName}">')
            print(f'<input type="hidden" id="employee" name="employee" value="{employee_flag}">')
            print('<input type="submit" '
                  'style="background: none; border: none; color: #FFD700; '
                  'text-decoration: underline; cursor: pointer; font-size: 250%;" '
                  'value="Click here to go to main app">')
            print('</form>')

    cursor.close()
    db.close()

with open('/var/www/landsharks.com/pageEnd.htm', 'r') as end:
    for line in end:
        print(line.rstrip('\n'))

print('</html>')
