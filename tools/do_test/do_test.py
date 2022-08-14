# Atcoderのテストを自動化するツール
# 複数の入力値に対して操作を実行し、結果と実行時間を出力する
import argparse
import time
import subprocess
import os


def do(input_text, file):
  time_sta = time.perf_counter()
  cp = subprocess.run(["python", file], input=input_text, encoding="UTF-8", stdout=subprocess.PIPE)
  print(cp.stdout)
  time_end = time.perf_counter()
  tim = time_end - time_sta
  print(f"time: {round(tim*1000,3)}ms")
  print("")


if __name__ == "__main__":

  parser = argparse.ArgumentParser(description="このプログラムはコードのテストを自動的に実行するためのものです")
  parser.add_argument("file", help="テストしたいコードのパスを指定してください")

  args = parser.parse_args()
  file = args.file
  if file is None:
    print("テストしたいコードのファイルを指定してください")
    exit(0)

  testcases = []
  with open(os.path.join(os.path.dirname(file), os.path.splitext(os.path.basename(file))[0].upper() + "_test.txt"), "r", encoding="utf-8") as f:
    data = f.read()
    testcases = data.split("test_case\n")
    # TODO 改善
    if "" in testcases:
      testcases.remove("")
  for case in testcases:
    do(case, file)
