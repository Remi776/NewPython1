number = input('Enter the 3-digit number: ')
result = 0
i = 0
while i < len(number):
    result += int(number[i])
    i += 1
print(result)