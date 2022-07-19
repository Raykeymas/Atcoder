n = int(input())

t, a = map(int, input().split(" "))
for i in range(n - 1):
  rate_t, rate_a = map(int, input().split(" "))
  for i in range(a + i, 10**18):
    t = i * rate_t / rate_a
    if t.is_integer():
      a = i
      t = round(t)
      break
print(t + a)
