N, x = map(int, input().split(" "))
candy = list(map(int, input().split(" ")))
operation = 0
if candy[0] > x:
  operation += candy[0] - x
  candy[0] -= candy[0] - x
for i in range(N - 1):
  if candy[i + 1] + candy[i] > x:
    operation += abs(x - (candy[i + 1] + candy[i]))
    candy[i + 1] -= abs(x - (candy[i + 1] + candy[i]))
print(operation)
