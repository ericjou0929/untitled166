import _sqlite3

conn = _sqlite3.connect('demo.db')
print(conn)
conn.close()
