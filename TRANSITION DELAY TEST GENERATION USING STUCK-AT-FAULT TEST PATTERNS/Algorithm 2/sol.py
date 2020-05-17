import time

start_time = time.time()

"""
Open fault table as fault_text
"""
with open("fault.txt") as fault_text:
    fault_val = list(fault_val.strip() for fault_val in fault_text)


#------------------------------


"""
Open simulation table as sim_text
"""
with open("simulation.txt")  as sim_text:
    sim_val = list(sim_val.strip() for sim_val in sim_text)


#------------------------------

"""
Open variable table as var_text
"""
with open("var.txt") as var_text:
    var_val = list(map(int, var_text.readline().split()))


#------------------------------

"""
storing fault table, simulation table length
and then length of fault table row
"""
fault_len = len(fault_val)
sim_len = len(sim_val)
fault_row_len = len(fault_val[0])


res = []
temp_res = ''
res_x = ''

for i in range(fault_row_len):
    res_x += 'X'

for fault in fault_val:
    res.append(fault)

res.append(fault_val[0])

for i in range(sim_len):
    sim_val.append(sim_val[i])


"""
initial variables for count zero and one
"""
count_zero = 0
count_one = 0


# Loop through fault table row
for i in range(1, fault_len):
    index = 0
    # for all patterns in fault table rows
    for j in fault_val[i]:
        # calculating result if zero or one found in fault table
        if j == '0' or j == '1':
            if (sim_val[i][var_val[index]] == '1' or sim_val[i][var_val[index]] == 'h' or sim_val[i][var_val[index]] == 'H') and (sim_val[i-1][var_val[index]] == '0' or sim_val[i-1][var_val[index]] == 'l' or sim_val[i-1][var_val[index]] == 'L'):
                temp_res += '1'
            elif (sim_val[i][var_val[index]] == '0' or sim_val[i][var_val[index]] == 'l' or sim_val[i][var_val[index]] == 'L') and (sim_val[i-1][var_val[index]] == '1' or sim_val[i-1][var_val[index]] == 'h' or sim_val[i-1][var_val[index]] == 'H'):
                temp_res += '0'
            else:
                temp_res += 'X'
        else:
            temp_res += 'X'
        index += 1
    # appending calculated result in result variable
    res.append(temp_res)
    temp_res = ''

res_len = len(res)

# appending X in odd rows of final result
for i in range(res_len):
    if not i & 1:
        res[i] = res_x


# output final fault table as fault_output.txt 
with open("fault_output.txt", "w") as output:
    for i in res:
        output.write(i)
        output.write('\n')

output.close()

# output final simulation table as simulation_output.txt 
with open("simulation_output.txt", "w") as output:
    for i in sim_val:
        output.write(i)
        output.write('\n')


fault_text.close()
sim_text.close()
var_text.close()
output.close()

print('process finished with ---> ', time.time()-start_time, ' seconds...')
