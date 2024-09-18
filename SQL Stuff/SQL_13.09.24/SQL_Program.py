import sqlite3


name1 = input('Enter a username: ')
name1 = name1[0].upper() + name1[1:].lower()

conn = sqlite3.connect('BankAccounts.db')
c = conn.cursor()

c.execute('''
          SELECT CustomerID FROM Customer WHERE FirstName = ?''', (name1,))

customerID = c.fetchone()
customerID = str(customerID[0])

c.execute('''
          SELECT Balance FROM Account WHERE CustomerID = ?''', (customerID,))

customerBalance = c.fetchone()
print(name1, 'has a balance of £' + str(customerBalance[0]))

print()

name2 = input('Enter another username to trasfer money to: ')
transferAmount = float(input('Enter the amount to transfer: '))

name2 = name2[0].upper() + name2[1:].lower()

if transferAmount > customerBalance[0]:
    print('Insufficient funds')
else:
    c.execute('''
              UPDATE Account SET Balance = Balance - ? WHERE CustomerID = ?''', (transferAmount, customerID))
    c.execute('''
              SELECT CustomerID FROM Customer WHERE FirstName = ?''', (name2,))
    
    customerID2 = c.fetchone()
    customerID2 = str(customerID2[0])

    c.execute('''
              UPDATE Account SET Balance = Balance + ? WHERE CustomerID = ?''', (transferAmount, customerID2))
    
    conn.commit()
    print()
    print('Transfer complete')

    print()
    print('New balances:')

    c.execute('''
              SELECT Balance FROM Account''')
    data = c.fetchall()
    
    c.execute('''
              SELECT Firstname FROM Customer''')
    data2 = c.fetchall()
    
    for row in range(len(data)):
        print(data2[row][0] + ' has a balance of £' + str(data[row][0]))

conn.close()