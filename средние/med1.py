try:
    s = [float(item) for item in input("Введите набор действительных чисел через пробел: ").split(sep=' ')]
except:
    print('Некорректный ввод!')
    exit()
try:
    n = int(input("Какой по величине элемент введенного набора получить: "))
except:
    print('Некорректный ввод!')
    exit()
if (n<1):
    print('Некорректный ввод!')
    exit()
us = []
for el in s:
    if not (el in us):
        us.append(el)
for i in range(len(us)):
    for j in range(len(us)):
        if (us[i]>us[j]):
            us[i],us[j] = us[j],us[i]
if (len(s)<n):
    print("Невозможно получить ",n,"-й по величине элемент данного набора, так как его длина меньше ",n,".", sep='')
elif (len(us)<n):
    print("Невозможно получить ",n,"-й по величине элемент данного набора, так как  в нем менее ",n," различных чисел.", sep='')
else:
    print(n,"-й по величине элемент набора чисел: ",us[n-1],".", sep='')