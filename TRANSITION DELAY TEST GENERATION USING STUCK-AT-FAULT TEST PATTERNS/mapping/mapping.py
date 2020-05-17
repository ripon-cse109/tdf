var = []

with open("pre_var.txt") as pre_var:
    for i in pre_var:
        got = i.split()
        # if i[0] == 'V' and i[1] == ' ':
        temp = len(got)
        if temp > 6:
            # print('`', got[6], '`')
            if got[6] == 'V' and got[7] == '=':
                # print(got[8])
                var.append(i.split()[8])

var_len = len(var)
print(var, 'len: ', var_len)

with open("var.txt", "w") as output:
    for i in range(var_len):
            output.write(var[i])
            output.write(" ")