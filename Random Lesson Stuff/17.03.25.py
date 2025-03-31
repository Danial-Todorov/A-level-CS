num = 8
done = False

def read_numbers():
    with open('MyFile.txt', 'r') as file:
        return [int(line.strip()) for line in file.readlines()]


#print(read_numbers())
numbers = read_numbers()
tempFile = open("MyFileTemp.txt", "w")

for i in range(len(numbers)):
    if num > numbers[i]:
        tempFile.write(str(numbers[i]) + "\n")

    elif num < numbers[i] and done:
        tempFile.write(str(numbers[i]) + "\n")
        done = True

    elif num < numbers[i]:
        tempFile.write(str(numbers[i]) + "\n")

print(tempFile.read())

'''
for i in range(len(numbers)):
    if num < numbers[i]:
        temp = numbers[i]
        numbers[i] = num
        print(numbers)
        for x in range(len(numbers)-i):
            print(numbers)
            temp2 = numbers[i+x]
            numbers[i+x+1] = temp
            temp = temp2
        break
'''

