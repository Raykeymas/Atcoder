# B、Wそれぞれの個数は変わらない
# W→Bに並べ替えるための試行回数が答えになる

S = input()
S = list(S)
count = 0
# 計算量が多すぎる(n**2...)
for i in reversed(range(len(S))):
  for j in reversed(range(i)):
    if S[j] == "B" and S[i] == "W":
      S[j], S[i] = "W", "B"
      count += i - j
print(count)
