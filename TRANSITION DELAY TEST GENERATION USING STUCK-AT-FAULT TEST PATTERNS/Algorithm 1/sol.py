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
storing fault table length and
initiating variable for storing result
"""
fault_len = len(fault_val)

res = [[] for resi in range(fault_len)]

# initiate variables for count 0, 1, X
count = 0
countx = 0


# Loop through fault table row
for i in range(1, fault_len):
    fault_row_len = len(fault_val[i])
    # for all patterns in fault table rows
    for j in range (fault_row_len):
        # calculating result if zero or one found in fault table
        if fault_val[i][j] == '0' or fault_val[i][j] == '1':
            if (sim_val[i][var_val[j]] == '1' or sim_val[i][var_val[j]] == 'h' or sim_val[i][var_val[j]] == 'H') and (sim_val[i-1][var_val[j]] == '0' or sim_val[i-1][var_val[j]] == 'l' or sim_val[i-1][var_val[j]] == 'L'):
                res[i].append('1')
                count += 1
            elif (sim_val[i][var_val[j]] == '0' or sim_val[i][var_val[j]] == 'l' or sim_val[i][var_val[j]] == 'L') and (sim_val[i-1][var_val[j]] == '1' or sim_val[i-1][var_val[j]] == 'h' or sim_val[i-1][var_val[j]] == 'H'):
                res[i].append('0')
                count += 1
            else:
                res[i].append('X')
                countx += 1
        else:
            res[i].append('X')
            countx += 1

#------------------------------

# appending X in first row of result
for i in range(fault_row_len):
    res[0].append('X')
    
res_len = len(res)

# output final table as output.txt 
with open("output.txt", "w") as output:
    for i in range(res_len):
        res_row_len = len(res[i])
        for j in range(res_row_len):
            output.write(res[i][j])
        output.write("\n")

fault_text.close()
sim_text.close()
var_text.close()

print('process finished with ---> ', time.time()-start_time, ' seconds...')
