with open("fault.txt") as fault_text:
    fault_val = list(fault_val.strip() for fault_val in fault_text)

# print(fault_val)

#------------------------------

fault_len = len(fault_val)

count = [[] for i in range(3)]

for i in fault_val[0]:
    count[0].append(0)
    count[1].append(0)
    count[2].append(0)

# print(count)

for i in range(fault_len):
    index = 0
    for j in fault_val[i]:
        if j == '0':
            count[0][index] = 1
        elif j == '1':
            count[1][index] = 1
        elif j == 'X':
            count[2][index] = 1
        index += 1

# print(count)

res = []
count_len = len(count[0])

and_count = 0
zero_count = 0
one_count = 0

for i in range(count_len):
    if count[0][i] == 1 and count[1][i] == 1 and count[2][i] == 1:
        res.append('&')
        and_count += 1
    elif count[0][i] == 1 and count[1][i] == 1 and count[2][i] == 0:
        res.append('&')
        and_count += 1
    elif count[0][i] == 1 and count[1][i] == 0 and count[2][i] == 0:
        res.append('0')
        zero_count += 1
    elif count[0][i] == 0 and count[1][i] == 0 and count[2][i] == 1:
        res.append('X')
    elif count[0][i] == 0 and count[1][i] == 1 and count[2][i] == 0:
        res.append('1')
        one_count += 1
    elif count[0][i] == 0 and count[1][i] == 1 and count[2][i] == 1:
        res.append('1')
        one_count += 1
    elif count[0][i] == 1 and count[1][i] == 0 and count[2][i] == 1:
        res.append('0')
        zero_count += 1

# print(res)
    
print('number of & counted: ', and_count)
print('number of one counted: ', one_count)
print('number of zero counted: ', zero_count)

total_num_of_fault = int(input('input total number of fault : '))

fault_coverage = (((and_count * 2) + one_count + zero_count) / total_num_of_fault)*100

print(fault_coverage)

with open("output_1.txt", "w") as output:
    for i in res:
        output.write(i)