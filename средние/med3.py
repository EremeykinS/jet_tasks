digits = [str(e) for e in range(0,10)]
s, ds, i = list(input("Введите закодированную строку:")), [], 0
while i < len(s):
    if s[i] in digits:
        j = i + 1
        while s[j] in digits:
            j = j + 1
        c = int(''.join(s[i:j]))
        ds[len(ds):len(ds) + c] = [s[j]]*c
        i = j
    i = i + 1
print("Декодированная строка:",''.join(ds))