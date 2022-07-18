import time

# 時間計測開始
time_sta = time.time()
# 処理を書く（ここでは1秒停止する）
time.sleep(1)
# 時間計測終了
time_end = time.time()
# 経過時間（秒）
tim = time_end - time_sta

print(tim)
# [結果] 1.0004463195800781
