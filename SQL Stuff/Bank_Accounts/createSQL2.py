import sqlite3

conn = sqlite3.connect('BankAccounts.db')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE Account
             (AccountID text, CustomerID int,  Balance real)''')

# Insert data
c.execute("INSERT INTO Account VALUES ('JBLAcc1001',1,35.25)")
c.execute("INSERT INTO Account VALUES ('JBLAcc1002',2,265.00)")
c.execute("INSERT INTO Account VALUES ('JBLAcc1003',3,9.75)")
c.execute("INSERT INTO Account VALUES ('JBLAcc1004',4,90.00)")
c.execute("INSERT INTO Account VALUES ('JBLAcc1005',5,100.00)")
c.execute("INSERT INTO Account VALUES ('JBLAcc1006',6,6.45)")
c.execute("INSERT INTO Account VALUES ('JBLAcc1007',7,3.55)")
c.execute("INSERT INTO Account VALUES ('JBLAcc1008',8,1000.00)")
c.execute("INSERT INTO Account VALUES ('JBLAcc1009',9,90.00)")

# Create table
c.execute('''CREATE TABLE Customer
             (CustomerID int,  FirstName text, LastName text)''')

# Insert data
c.execute("INSERT INTO Customer VALUES (1,'Danial','Todorov')")
c.execute("INSERT INTO Customer VALUES (2,'Alex','Johnson')")
c.execute("INSERT INTO Customer VALUES (3,'Tommy','Henderson-Thynne')")
c.execute("INSERT INTO Customer VALUES (4,'Sofia','Zablocka')")
c.execute("INSERT INTO Customer VALUES (5,'Praveet','Khambhaita')")
c.execute("INSERT INTO Customer VALUES (6,'David','Zablocki')")
c.execute("INSERT INTO Customer VALUES (7,'Jeremy','Bell')")
c.execute("INSERT INTO Customer VALUES (8,'Muhammad','Ali')")
c.execute("INSERT INTO Customer VALUES (9,'Ashton','Khan')")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
