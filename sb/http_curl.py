import requests

headers = {'Content-Type': 'application/json', "User-Agent": "Snowball Android 14.4"}

url = "http://rc.search.query.snowballfinance.com/query/v3/search/all.json?tabId=1&q=中国平安怎么样&uid=&symbol=SH603011&sortId=1&count=10&page=1&access_token=XqTestc8b8b86d90f858449a8b1b58e519829b3ca1f121"
res = requests.get(url=url, headers=headers)

print(res.request.headers)

print(res.text)
