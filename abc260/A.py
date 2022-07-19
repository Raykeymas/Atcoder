s = input()
s = list(s)
obj = {}
for i in range(len(s)):
    if s[i] in obj.keys():
        obj[s[i]] += 1
    else:
        obj[s[i]] = 1
ok = False
for key in obj.keys():
    if obj[key] == 1:
        print(key)
        ok = True
        break

if not ok:
    print(-1)