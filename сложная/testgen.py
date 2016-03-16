import random
fg = open("asd_gen.txt", mode='wt')
fnl = ['ACK','F','FIB']
for i in range(10**6):
    funcname = random.choice(fnl)
    if funcname == "ACK":
        args = str(random.randint(0,3))+' '+str(random.randint(0,13))
    elif funcname == "FIB":
        args = str(random.randint(1,10**3))
    else:
        args = str(random.randint(0,10**2))
    line = funcname + ' ' + args + "\n"
    fg.write(line)
fg.close()
