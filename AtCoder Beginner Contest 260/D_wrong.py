import collections
N, K = map(int, input().split(" "))
p_list = list(map(int, input().split(" ")))

field_cards = []
ans = collections.defaultdict(lambda: -1)

for i in range(N):
  num = p_list[i]
  min = None
  index = 0
  for j in range(len(field_cards)):
    if num <= field_cards[j][0]:
      if min is None:
        min = field_cards[j][0]
        index = j
      elif field_cards[j][0] < min:
        min = field_cards[j][0]
        index = j
  if min is None:
    field_cards.append([num])
    if len(field_cards[len(field_cards) - 1]) == K:
      eat_list = field_cards.pop(len(field_cards) - 1)
      for e in eat_list:
        ans[e] = i + 1
  else:
    field_cards[index] = [num] + field_cards[index]
    if len(field_cards[index]) == K:
      eat_list = field_cards.pop(index)
      for e in eat_list:
        ans[e] = i + 1

for i in range(N):
  print(ans[i + 1])
