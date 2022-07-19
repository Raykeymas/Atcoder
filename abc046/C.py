n = int(input())

t, a = map(int, input().split(" "))
for i in range(n - 1):
  rate_t, rate_a = map(int, input().split(" "))
  # 今回の肝はこれ
  # t <= Ti * n, a <= Ai * n を満たすn(n >= 1)を求めたい
  # このnはどちらかの式で求められるものの高い方を採用する。そうでなければ不等号を満たさない可能性がある
  # 加えて、math.ceil(t/rate_t)のような計算は内部のfloatに誤差が生じてしまい、桁数が多いと16,17桁以降で誤差が発生してしまう
  # そのため//を利用するが、常に切り上げるようにするためさらにマイナスを付加する（切り下げでは不等号を満たさない可能性がある）
  k = max(-(-t // rate_t), -(-a // rate_a))
  t, a = rate_t * k, rate_a * k
print(t + a)
