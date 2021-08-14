import requests

def child(url):
    try:
        a=requests.get(url)
        if a.status_code!=200:
            return False
        a.encoding=a.apparent_encoding
        if "在庫ありの条件をここに記入" in a.text:
            return True
def search(urls):
    results = []
    for url in urls:
        if child(url):
            return True

if __name__ == "__name__":
    search(["https://a.com", "https://b.com"])
