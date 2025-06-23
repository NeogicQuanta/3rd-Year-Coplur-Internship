import sqlite3

conn = sqlite3.connect("Question3.db")

conn.execute("""
Create table Customer(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(20),
age INTEGER
);""")
conn.execute("""
Create table Product(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name varchar(20),
price INTEGER
);
""")
conn.execute("""
Create table Company(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name varchar(20),
quantity INTEGER
)
""")


conn.execute("""INSERT INTO Customer VALUES 
             (1,'a',25),
             (2,'b',30),
             (3,'c',35),
             (4,'d',40)
""")
conn.execute("""INSERT INTO Product VALUES 
             (1,'a',1000),
             (2,'b',2000),
             (3,'c',3000),
             (4,'d',4000)
""")
conn.execute("""INSERT INTO Company VALUES 
             (1,'c1',12),
             (2,'c2',20),
             (3,'c3',13),
             (4,'c4',40)
""")
conn.commit()

print()

u_data = conn.execute("SELECT * FROM Customer")
p_data = conn.execute("SELECT * FROM Product")
q_data = conn.execute("SELECT * FROM Company")

print("Customer Data:")
print("ID | Name | Age")
for i in u_data:
    print(f"{i[0]} | {i[1]} | {i[2]}")
print()
print("Product Data:")
print("ID | Name | Price")
for i in p_data:
    print(f"{i[0]} | {i[1]} | {i[2]}")
print()
print("Company Data:")
print("ID | Name | Quantity")
for i in q_data:
    print(f"{i[0]} | {i[1]} | {i[2]}")

print()

print("Enter the ID of the record you want to delete:")
id = int(input("Enter no: "))
conn.execute(f"DELETE FROM Customer WHERE id = {id}")
conn.execute(f"DELETE FROM Product WHERE id = {id}")
conn.execute(f"DELETE FROM Company WHERE id = {id}")
conn.commit()

conn.execute("UPDATE Customer SET name = 'X' WHERE id = 1")
conn.execute("UPDATE Product SET name = 'Y' WHERE id = 1")
conn.execute("UPDATE Company SET name = 'Z' WHERE id = 1")

conn.commit()

u_data = conn.execute("SELECT * FROM Customer")
p_data = conn.execute("SELECT * FROM Product")
q_data = conn.execute("SELECT * FROM Company")
for i in u_data:
    print(i)
print()
for i in p_data:
    print(i)
print()
for i in q_data:
    print(i)


conn.close()
