import sqlite3
conn = sqlite3.connect("users.db")
x = conn.execute('''
select * from users

''')
for i in x:
    print(i[0],i[1],i[2])