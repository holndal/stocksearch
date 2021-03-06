#!pip3 install speedtest-cli
# ※注意；うまく動かなかったら下記githubからインストールすると改善されることがあります。
# https://github.com/sivel/speedtest-cli

import speedtest
def get_speed_test():
  servers = []
  stest = speedtest.Speedtest()
  stest.get_servers(servers)
  stest.get_best_server()
  return stest

# 結果をfloat型で返す(単位はMbps)
def get_speed():
  stest = get_speed_test()
  result = stest.download()
  result = result/1000/1000
  return result

if __name__=="__main__":
  print(str(get_speed())+"Mbps")
