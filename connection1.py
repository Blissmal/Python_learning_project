import sqlite3

conn = sqlite3.connect("Farmers.db")
print("success")

conn.execute("INSERT INTO Farmers(ID, FARMER_NAME, PHONE_NO, FARMER_TYPE) VALUES (1, 'Erick', 25434675674, 'Paultry')")
conn.execute("INSERT INTO Farmers(ID, FARMER_NAME, PHONE_NO, FARMER_TYPE) VALUES (2, 'Joash', 234567875676, 'Cattle Keeping')")
conn.execute("INSERT INTO Farmers(ID, FARMER_NAME, PHONE_NO, FARMER_TYPE) VALUES (3, 'John', 235789078567, 'Crop Growing')")
conn.execute("INSERT INTO Farmers(ID, FARMER_NAME, PHONE_NO, FARMER_TYPE) VALUES (4, 'Enock', 274267777345, 'Plantation')")
conn.execute("INSERT INTO Farmers(ID, FARMER_NAME, PHONE_NO, FARMER_TYPE) VALUES (5, 'Mary', 13245677898, 'Paultry')")
conn.execute("INSERT INTO Farmers(ID, FARMER_NAME, PHONE_NO, FARMER_TYPE) VALUES (6, 'Ruth', 3456567867853, 'Maize growing')")


conn.commit()
print("Records added successfully")
