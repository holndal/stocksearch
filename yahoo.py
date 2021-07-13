# https://developer.yahoo.co.jp/webapi/shopping/shopping/v3/itemsearch.html
import requests
import argparse
def yahoo_search(args):
    url="https://shopping.yahooapis.jp/ShoppingWebService/V3/itemSearch?appid={}&query={}".format(args.api,args.query)
    return requests.get(url)

def parse():
    # 実装が雑ですが一番上のURLを参考にして適宜Parserを追加してください
    parser = argparse.ArgumentParser(description='Yahoo ShoppingのAPI使い方')
    parser.add_argument("--api", type=str,help='yahooのapi idを入力。必須',required=True)
    parser.add_argument("--query",help="検索キーワード", required=True)
    args = parser.parse_args()
    return args
if __name__=="__main__":
    args = parse()
    print(args)
    results=yahoo_search(args)
    print(results)
    print(dir(results))
