s = list(input("Введите строку:"))
c, ch, es = 0, s[0], []
for i in range(len(s)):
    if (ch!=s[i]):
        es.append(c)
        es.append(ch)
        c, ch = 1, s[i]
    else:
        c = c + 1
es.append(c)
es.append(ch)
print("Закодированная строка:",''.join(str(e) for e in es))