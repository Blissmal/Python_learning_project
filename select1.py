import sqlite3

select = sqlite3.connect("Farmers.db")
data = select.execute("select * from Farmers")
for row in data:
    print("ID = ", row[0])
    print("FARMER NAME = ", row[1])
    print("PHONE NO = ", row[2])
    print("FARMERTYPE = ", row[3], "\n")
select.close()
