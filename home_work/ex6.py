valid_num = input('Enter the 6-digit number: ')
first_sum = 0
second_sum = 0
for i in range(0, len(valid_num) // 2):
    first_sum += int(valid_num[i])
for j in range(len(valid_num) // 2, len(valid_num)):
    second_sum += int(valid_num[j])
if first_sum == second_sum:
    print('yes')
else:
    print('no')