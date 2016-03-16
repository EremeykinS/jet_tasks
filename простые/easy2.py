try:
    num = int(input("Введите натуральное число: "))
except:
    print('Некорректный ввод!')
    exit()
div, n, i = [], num, 2
while i<n//2+1:
    if n%i==0:
        div.append(i)
        n=n//i
        i=2
    else:
        i=i+1
if not div:
    div = [1,num]
else:
    div.append(n)
print("Разложение на простые множители: ", num,' = ','*'.join(str(el) for el in div),sep='')