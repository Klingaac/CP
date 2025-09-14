code = input()
skip = False
num = ""
for i in range(len(code)):
    if not skip:
        if code[i] == ".":
            num += '0'
        elif code[i+1] == ".":
            num += '1'
            skip = True
        else:
            num += '2'
            skip = True
    else:
        skip = False
print(num)