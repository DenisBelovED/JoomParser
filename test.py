import requests
import json

product_link = 'https://api.joom.com/1.1/products/1489989856475656191-226-1-26312-3842694476?language=ru-RU&currency=RUB'
count = 1
init_url = r'https://www.joom.com/tokens/init'
products_url = r'https://api.joom.com/1.1/search/products?language=ru-RU&currency=RUB'

access_token = json.loads(requests.post(init_url).text)['accessToken']

headers = {'Authorization': 'Bearer ' + access_token}

res = requests.get(product_link, headers=headers)
print(json.loads(res.text)['payload']['description'])
