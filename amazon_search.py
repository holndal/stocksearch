# !pip3 install python-amazon-paapi --upgrade
# https://github.com/sergioteula/python-amazon-paapi

from amazon.paapi import AmazonAPI

# ENTER YOUR INFO
KEY=""
SECRET=""
TAG=""
COUNTRY="JP"

amazon = AmazonAPI(KEY, SECRET, TAG, COUNTRY)

# 注意：入力されたリストと戻るリストの順番は関係ないので注意。
# そのためasinを取り出す際には products[i].asinで取り出すこと。
def searchitems(asins: list):
    products = amazon.get_products(asins , merchant="Amazon")
    return products
 
def searchitem(asins: str):
    product = amazon.get_product(asins , merchant="Amazon")
    return product

if __name__ == "__main__":
    product=searchitem("B07ZHC95FP")
    #searchitems(["B08QYRL8D2","B08LQ7GXNX"])
    price=product.prices.price.value
    asin=product.asin
    # product で使えるもの 'asin', 'images', 'info', 'offers_summary', 'parent_asin', 'prices', 'product', 'raw_info', 'title', 'trade_in', 'url'



