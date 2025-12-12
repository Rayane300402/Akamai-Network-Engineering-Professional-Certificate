#!/var/www/landsharks.com/venv/bin/python
import mysql.connector
import cgi, cgitb

cgitb.enable()

print('Content-type:text/html')
print('')
print('<html>')
print('<head>')
print('<meta http-equiv="content-type" content="text/html; charset=utf-8">')
print('<link rel="stylesheet" type="text/css" href="styles.css">')
print('<title>LAN Sharks App</title>')
print('</head>')

# common header / banner
with open('/var/www/landsharks.com/pageStart.htm', 'r') as start:
    for line in start:
        print(line.rstrip('\n'))

form = cgi.FieldStorage()
userName = (form.getfirst('userName') or '').strip().lower()
employee_flag = (form.getfirst('employee') == 'True')

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='python'
)
cursor = db.cursor(dictionary=True)

if employee_flag:
    # ================= EMPLOYEE VIEW (like screenshot 3) =================
    email_pattern = f"{userName}@%"
    cursor.execute("""
        SELECT firstName, lastName, email, position
        FROM employees
        WHERE email LIKE %s
        LIMIT 1
    """, (email_pattern,))
    emp = cursor.fetchone()

    if not emp:
        print('<h2 class="heading">Something Went Wrong</h2>')
        print('<p class="description">Employee record not found.</p>')
    else:
        full_name = f"{emp['firstName']} {emp['lastName']}"
        print(f'<h1 class="heading" style="font-size: 250%; color: #FFD700;">{full_name}</h1>')
        print(f'<p class="subheading" style="font-size: 150%; color: #FFD700;">{emp["position"]}</p>')
        print(f'<p class="description"><b>Email:</b> {emp["email"]}</p>')
        print(f'<p class="description"><b>UserName:</b> {userName}</p>')
        print('<p class="description">'
              '<a href="change_password.py?userName=%s" style="color: #FFD700;" >Change Password</a>'
              '</p>' % userName)

else:
    # ================= CUSTOMER VIEW (like screenshot 7) =================
    email_pattern = f"{userName}@%"
    cursor.execute("""
        SELECT *
        FROM customers
        WHERE email LIKE %s
        LIMIT 1
    """, (email_pattern,))
    cust = cursor.fetchone()

    if not cust:
        print('<h2 class="heading" style="font-size: 250%; color: #FFD700;">Something Went Wrong</h2>')
        print('<p class="description">Customer record not found.</p>')
    else:
        full_name = f"{cust['firstName']} {cust['lastName']}"
        
        print(
            f'<h1 class="heading" '
            f'style="font-size: 250%; color: #FFD700;">{full_name}</h1>'
        )

        print(
            f'<p class="subheading" '
            f'style="font-size: 200%; ">{cust["companyName"]}</p>'
        )

        # Links like screenshot 7
        print('<p class="description">'
              '<a href="update_contact.py?userName=%s" style="color: #FFD700;">Update Contact Information</a>'
              '</p>' % userName)
        print('<p class="description">'
              '<a href="change_password.py?userName=%s" style="color: #FFD700;">Change Password</a>'
              '</p>' % userName)

        cursor.execute("""
            SELECT packetDateTime, srcIP, destIP, protocol,
                   srcPort, destPort, info
            FROM incidents
            WHERE customerNumber = %s
            ORDER BY packetDateTime
        """, (cust['customerNumber'],))
        rows = cursor.fetchall()

        if rows:
            print('<table class="attacktable">')
            print('<tr>'
                  '<th>Attack Type</th>'
                  '<th>Info</th>'
                  '<th>Attacks</th>'
                  '<th>Date-Time</th>'
                  '</tr>')
            # For now just show raw records; later we’ll fold them into ARP/SYN counts
            for r in rows:
                # crude detection string for now
                if r['protocol'] == 'ARP':
                    atype = 'ARP Poisoning Attack'
                    attacks = 'n/a'
                elif '[SYN]' in (r['info'] or ''):
                    atype = 'SYN Flood'
                    attacks = 'n/a'
                else:
                    atype = r['protocol']
                    attacks = ''

                print('<tr>')
                print(f"<td>{atype}</td>")
                print(f"<td>{r['info']}</td>")
                print(f"<td>{attacks}</td>")
                print(f"<td>{r['packetDateTime']}</td>")
                print('</tr>')
            print('</table>')
        else:
            print('<p class="description">No attacks detected for this customer.</p>')

cursor.close()
db.close()

# footer
with open('/var/www/landsharks.com/pageEnd.htm', 'r') as end:
    for line in end:
        print(line.rstrip('\n'))

print('</html>')

