#!/var/www/landsharks.com/venv/bin/python
import mysql.connector
import cgi, cgitb
cgitb.enable()

print("Content-type:text/html")
print("")

form = cgi.FieldStorage()
userName = (form.getfirst("userName") or "").strip().lower()

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="python"
)
cur = db.cursor(dictionary=True)

cur.execute("SELECT type FROM users WHERE userName=%s LIMIT 1", (userName,))
row = cur.fetchone()
cur.close()
db.close()

employee_flag = "True" if row and (row["type"] or "").lower() == "e" else "False"

print('<html><body>')
print('<form action="main.py" method="post" id="go">')
print(f'<input type="hidden" name="userName" value="{userName}">')
print(f'<input type="hidden" name="employee" value="{employee_flag}">')
print('</form>')
print('<script>document.getElementById("go").submit();</script>')
print('</body></html>')

