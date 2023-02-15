import sqlite3

conn = sqlite3.connect("emobilis.db")
print("open db successfully")

conn.execute("INSERT INTO Students(ID, NAME, AGE, SCHOOL) VALUES (1, 'Erick', 30, 'eMobilis')")
conn.execute("INSERT INTO Students(ID, NAME, AGE, SCHOOL) VALUES (2, 'Purity', 20, 'Moi Girls')")
conn.execute("INSERT INTO Students(ID, NAME, AGE, SCHOOL) VALUES (3, 'Paul', 29, 'Kapsabet Boys')")
conn.execute("INSERT INTO Students(ID, NAME, AGE, SCHOOL) VALUES (4, 'Richard', 40, 'University of Nairobi')")
conn.execute("INSERT INTO Students(ID, NAME, AGE, SCHOOL) VALUES (5, 'Faith', 39, 'Kenya High')")
conn.execute("INSERT INTO Students(ID, NAME, AGE, SCHOOL) VALUES (6, 'Bethuel', 24, 'Starehe Boys')")

conn.commit()
print("Records added successfully")
