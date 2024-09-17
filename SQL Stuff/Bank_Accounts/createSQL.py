
import sqlite3


conn = sqlite3.connect('BankAccounts.db')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE Account
             (AccountID text, CustomerID int,  Balance real)''')

# Insert data
c.execute("INSERT INTO Account VALUES ('JBLAcc1001',1,35.14)")
c.execute("INSERT INTO Account VALUES ('JBLAcc1002',2,150.0)")
c.execute("INSERT INTO Account VALUES ('JBLAcc1003',3,12.75)")

# Create table
c.execute('''CREATE TABLE Customer
             (CustomerID int,  FirstName text, LastName text)''')

# Insert data
c.execute("INSERT INTO Customer VALUES (1,'Bob','Smith')")
c.execute("INSERT INTO Customer VALUES (2,'Jim','Wilson')")
c.execute("INSERT INTO Customer VALUES (3,'Willie','Johnson')")


# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
