import requests
import json

url = r'https://www.joom.com/ru/search/c.1473502942287825617-1-2-118-2647263063'
count = 10

id_link = url[33:]
init_url = r'https://www.joom.com/tokens/init'
products_url = r'https://api.joom.com/1.1/search/products?language=ru-RU&currency=RUB'

access_token = json.loads(requests.post(init_url).text)['accessToken']

headers = {'Authorization': 'Bearer ' + access_token}
data = {
    'count': count,
    'filters': [{
            'id': 'categoryId',
            'value': {
                'type': 'categories',
                'items': [
                    {'id': id_link}
                ]
            }
        }
    ]
}

res = requests.post(products_url, json=data, headers=headers)
for product in json.loads(res.text)['payload']['items']:
    print()
    for i in product.keys():
        print(i, ':', product[i])
