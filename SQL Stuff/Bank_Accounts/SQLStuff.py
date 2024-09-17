
import sqlite3


conn = sqlite3.connect('BankAccounts.db')

c = conn.cursor()

customerID=int(input("Enter a customerID: "))

cursor = conn.execute ('''\
            SELECT Account.AccountID, Customer.FirstName, Customer.LastName, Account.Balance
            FROM Account
            INNER JOIN Customer
            ON Account.CustomerID = Customer.CustomerID
            WHERE Customer.CustomerID = ?''', (customerID,))

for account in cursor:
    print(account)

conn.close()

