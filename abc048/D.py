s = list(input())

is_three_last = False
if s[0] == s[-1]:
  is_three_last = True

if is_three_last:
  if len(s) % 2 == 0:
    print("First")
  else:
    print("Second")
else:
  if len(s) % 2 == 0:
    print("Second")
  else:
    print("First")
