import sqlite3

create = sqlite3.connect('Farmers.db')
print("Database created successfully")

create.execute("CREATE TABLE Farmers "
               "(ID INT PRIMARY KEY NOT NULL,"
               "FARMER_NAME TEXT NOT NULL,"
               "PHONE_NO INT NOT NULL,"
               "FARMER_TYPE TEXT NOT NULL)")

print("Table created successully")
create.close()
