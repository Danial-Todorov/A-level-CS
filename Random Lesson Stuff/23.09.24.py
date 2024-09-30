def Iterative(value):
    print('Iterative Function: \n')
    while value > 0:
        value -= 2
        if value >= 0:
            print(value)
            value += 1
            print(value)

def Recursive(value,i):
    if i = 0:
        i += 1
        print('Recursive Function: \n')
    if value > 0:
        value -= 2
        if value >= 0:
            print(value)
            value += 1
            print(value)
            Recursive(value)
        
startValue = int(input('Enter a number: '))
i = 0
Iterative(startValue)
Recursive(startValue,i)
