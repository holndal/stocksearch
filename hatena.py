# https://qiita.com/virtual_techX/items/5179b73576d86a89868e
# このURLの記事のコードをほとんどそのまま使っています。
import requests
from datetime import datetime
import hashlib
import base64
from xml.sax.saxutils import escape
from chardet.universaldetector import UniversalDetector
import random

def create_hatena_text(title, name, body, updated, categories, is_draft):
    is_draft = 'yes' if is_draft else 'no'
    categories_text = ''
    for category in categories:
        categories_text = categories_text + '<category term="{}" />\n'.format(category)
    template = """<?xml version="1.0" encoding="utf-8"?>
    <entry xmlns="http://www.w3.org/2005/Atom"
           xmlns:app="http://www.w3.org/2007/app">
      <title>{0}</title>
      <author><name>{1}</name></author>
      <content type="text/x-markdown">{2}</content>
      <updated>{3}</updated>
      {4}
      <app:control>
        <app:draft>{5}</app:draft>
      </app:control>
    </entry>"""
    text = template.format(title, name, body, updated, categories_text, is_draft).encode()
    return text
def post_hatena_blog(user_name, password, entry_id, blog_name, data):
    headers = {'X-WSSE': create_wsse_auth_text(user_name, password), 'content-type': 'application/xml'}
    if entry_id is None:
        url = 'https://blog.hatena.ne.jp/{0}/{1}/atom/entry'.format(user_name, blog_name)
    else:
        url = 'https://blog.hatena.ne.jp/{0}/{1}/atom/entry/{2}'.format(user_name, blog_name, entry_id)
    request = requests.post(url, data=data, headers=headers)
    if request.status_code == 201:
        print('POST SUCCESS!!\n' + 'message: ' + request.text)
    else:
        print('Error!\n' + 'status_code: ' + str(request.status_code) + '\n' + 'message: ' + request.text)

def get_hatena_blog(user_name, password, entry_id, blog_name, data):
    headers = {'X-WSSE': create_wsse_auth_text(user_name, password), 'content-type': 'application/xml'}
    if entry_id is None:
        url = 'https://blog.hatena.ne.jp/{0}/{1}/atom/entry'.format(user_name, blog_name)
    else:
        url = 'https://blog.hatena.ne.jp/{0}/{1}/atom/entry/{2}'.format(user_name, blog_name, entry_id)
    request = requests.get(url, headers=headers)
    if request.status_code == 200:
        print('GET SUCCESS!!\n' + 'message: ' + request.text)
    else:
        print('Error!\n' + 'status_code: ' + str(request.status_code) + '\n' + 'message: ' + request.text)

def put_hatena_blog(user_name, password, entry_id, blog_name, data):
    headers = {'X-WSSE': create_wsse_auth_text(user_name, password), 'content-type': 'application/xml'}
    if entry_id is None:
        url = 'https://blog.hatena.ne.jp/{0}/{1}/atom/entry'.format(user_name, blog_name)
    else:
        url = 'https://blog.hatena.ne.jp/{0}/{1}/atom/entry/{2}'.format(user_name, blog_name, entry_id)
    request = requests.put(url, data=data, headers=headers)
    if request.status_code == 200:
        print('PUT SUCCESS!!\n' + 'message: ' + request.text)
    else:
        print('Error!\n' + 'status_code: ' + str(request.status_code) + '\n' + 'message: ' + request.text)
def create_wsse_auth_text(user_name, password):
    created = datetime.datetime.now().isoformat() + "Z"
    b_nonce = hashlib.sha1(str(random.random()).encode()).digest()
    b_digest = hashlib.sha1(b_nonce + created.encode() + password.encode()).digest()
    c = 'UsernameToken Username="{0}", PasswordDigest="{1}", Nonce="{2}", Created="{3}"'
    return c.format(user_name, base64.b64encode(b_digest).decode(), base64.b64encode(b_nonce).decode(), created)

def new_post(title,text):
  USER_NAME = 'ユーザーネーム'
  BLOG_NAME = '**.hatenablog.com等'
  PASSWORD = 'API KEY(設定->詳細設定にある)'
  JST = datetime.timezone(datetime.timedelta(hours=+9), 'JST')

  # 更新日時の設定 現在日時を設定
  now=datetime.datetime.now(JST)

  # entry_idがNoneのときは自動でentry_idが生成されます。
  entry_id=None
  body = escape(text)
  categories = []
  # is_draftをFalseにすると公開になります。Trueで下書き投稿
  article = create_hatena_text(title, USER_NAME, body, now, categories, is_draft=False)

  # entry_idが既存の記事の場合記事を更新する。
  # 該当記事がないとputしてもnot found404で記事が投稿できなかったかもしれません。
  # put_hatena_blog(USER_NAME, PASSWORD, entry_id=entry_id, blog_name=BLOG_NAME, data=article)
  # 新規記事の投稿を行う
  post_hatena_blog(USER_NAME, PASSWORD, entry_id=entry_id, blog_name=BLOG_NAME, data=article)
  # 記事の取得を行う
  # get_hatena_blog(USER_NAME, PASSWORD, entry_id=entry_id, blog_name=BLOG_NAME, data=article)

if __name__=="__main__":
  new_post("title","text")
