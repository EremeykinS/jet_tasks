s, sub, index = input("Введите строку:"), input("Введите подстроку для поиска:"), -1
for i in range(len(s)-len(sub)+1):
    if (s[i:i+len(sub)]==sub):
        index = i+1
        break
if index>0:
    print("Данная подстрока входит во введенную подстроку начиная с позиции ", index, ".",sep='')
else:
    print("Данная подстрока не встречается в введенной строке.")
