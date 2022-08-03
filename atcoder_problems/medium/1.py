N = int(input())
a_buttons = []
has_2 = False
for i in range(N):
  tmp = int(input())
  if tmp == 2:
    has_2 = True
  a_buttons.append(tmp)
if not has_2:
  print(-1)
else:
  two_flug = False
  count = 0
  now_button = 1
  for i in range(N):
    now_button = a_buttons[now_button - 1]
    count += 1
    if now_button == 2:
      two_flug = True
      break
  if two_flug:
    print(count)
  else:
    print(-1)
