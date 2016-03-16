s, palindrom = input("Введите строку: "), True
for i in range(len(s)//2):
    if not s[i]==s[-i-1]:
        palindrom = False
        break
if palindrom:
    print("Палиндром")
else:
    print("Не палиндром")