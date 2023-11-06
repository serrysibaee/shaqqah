code = "++++++...=,="
# , . - = +
e = 0


for chr in code:

    if chr == ".":
    # to power 2 
        e = e ** 2 
    if chr == ",":
    # make the number reversed
        e = int("".join([str(e)[-i] for i in range(1,len(str(e))+1)]))
    if chr == "+":
    # add one  
        e += 1 
    if chr == "-":
    # sub one  
        e -= 1 
    if chr == "=":
    # print  
        print(e)


