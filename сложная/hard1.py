from calculator import fmap, sys
if len(sys.argv)<2:
    print("В программу не передан путь к файлу для обработки...")
    exit()
f = open(sys.argv[1])
fres = open("result.txt", mode='w')
for i,line in enumerate(f):
    if line:
        funcname = line[:line.index(' ')]
        args = line[line.index(' ')+1:]
        fres.write(str(i+1)+" "+str(fmap[funcname](args))+'\n')
        fres.flush()
fres.close()
f.close()