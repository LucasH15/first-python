import sqlite3

conn = sqlite3.connect('db.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        firstname TEXT,
        lastname TEXT
    )
''')
d = {
    'firstname': 'Joe',
    'lastname': 'Doe'
}
c.execute('''
    INSERT INTO users VALUES (:firstname, :lastname)
''', d)

conn.commit()

c.execute("SELECT * FROM users")
datas = c.fetchall()
print(datas)

conn.close()
