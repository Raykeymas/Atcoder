N, T = map(int, input().split(" "))
values = list(map(int, input().split(" ")))

indices = [*range(len(values))]

sorted_indices = sorted(indices, key=lambda i: -values[i])

count = 0
max_difference = 0

for k in range(N):
  min_value_index = sorted_indices[N - k - 1]
  for i in range(N):
    max_value_index = sorted_indices[i]
    if max_value_index > min_value_index:
      difference = values[max_value_index] - values[min_value_index]
      if difference > max_difference:
        max_difference = difference
        count = 1
      elif difference == max_difference:
        count += 1
      elif difference < max_difference:
        break
  else:
    continue


print(count)
