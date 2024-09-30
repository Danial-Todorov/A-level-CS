import time
import sqlite3

conn = sqlite3.connect('BankAccounts.db')
c = conn.cursor()
cache = {}

for count in range(10):
    customer = input('Enter a username: ')
    customer = customer[0].upper() + customer[1:].lower()
    startTime = time.time() * 1000

    if customer in cache:
        print('Cache hit')
        
    else:
        c.execute('''
                  SELECT * FROM Customer WHERE FirstName = ?''', (customer,))
        data = c.fetchall()

        if data:
            print('Cache miss')
            cache[customer] = data
    
    endTime = time.time() * 1000

    if data:
        totalTime = endTime - startTime
        totalTime = round(totalTime, 3)
        print('Time taken:', totalTime, 'ms')
    
    else:
        print('User not found')

    print()

conn.close()