f = open('MyFile2.csv', 'w')

while True:
    name = input('give name: ')
    age = input('Give age: ')
    height = input('give height: ')
    print()

    inputData = (name + ', ' + age + ', ' + height + '\n')

    if name == '':
        break

    f.write(inputData)

f.close()
