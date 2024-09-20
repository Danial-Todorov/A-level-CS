import sqlite3
import time

name1 = input('Enter a username: ')
name1 = name1[0].upper() + name1[1:].lower() # Puts the given name in the correct format

conn = sqlite3.connect('BankAccounts.db')
c = conn.cursor()

c.execute('''
          SELECT CustomerID FROM Customer WHERE FirstName = ?''', (name1,))
customerID = c.fetchone()
customerID = str(customerID[0]) # formatting

c.execute('''
          SELECT Balance FROM Account WHERE CustomerID = ?''', (customerID,))
customerBalance = c.fetchone()

print(name1, 'has a balance of £' + str(customerBalance[0])) # Displays the balance of the user
print()

name2 = input('Enter another username to trasfer money to: ')
name2 = name2[0].upper() + name2[1:].lower() # formatting given name

transferAmount = float(input('Enter the amount to transfer: £'))
print()

if transferAmount > customerBalance[0]: # Checks if the user has enough money
    print('Insufficient funds')

elif transferAmount <= 0:
    print('Invalid amount')

elif name1 == name2:
    print('You cannot transfer money to yourself')

else:
    c.execute('''
              UPDATE Account SET Balance = Balance - ? WHERE CustomerID = ?''', (transferAmount, customerID)) # Removes money from the first account
    
    c.execute('''
              SELECT CustomerID FROM Customer WHERE FirstName = ?''', (name2,))
    customerID2 = c.fetchone()
    customerID2 = str(customerID2[0]) # formatting

    c.execute('''
              UPDATE Account SET Balance = Balance + ? WHERE CustomerID = ?''', (transferAmount, customerID2)) # Adds money to the second account
    
    conn.commit() # This saves the changes to the database

    time.sleep(1)
    print('Transfer complete')
    print()
    time.sleep(1)
    print('New balances:')

    c.execute('''
              SELECT Balance FROM Account''') # Selects all balances
    balances = c.fetchall()
    
    c.execute('''
              SELECT Firstname FROM Customer''') # Selects all first names
    firstNames = c.fetchall()
    
    for i in range(len(balances)):
        print(firstNames[i][0] + ' has a balance of £' + str(balances[i][0])) # Displays all first names with their balances

conn.close() # Closes the database connection