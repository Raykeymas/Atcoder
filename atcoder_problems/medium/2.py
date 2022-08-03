S = input()
S = list(S)
count = 0
left = 0
for i, s in enumerate(S):
  if s == "W":
    count += i - left
    left += 1
print(count)
