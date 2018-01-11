import requests
import json


class Parser:
    init_url = r'https://www.joom.com/tokens/init'
    products_url = r'https://api.joom.com/1.1/search/products?language=ru-RU&currency=RUB'

    def __init__(self, links_list):
        self.links = links_list
        access_token = json.loads(requests.post(self.init_url).text)['accessToken']
        count = int(links_list[0])
        for url in self.links[1:]:
            print()
            print('link -', url)
            id_link = url[33:]

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

            res = requests.post(self.products_url, json=data, headers=headers)
            for product in json.loads(res.text)['payload']['items']:
                print()
                for i in product.keys():
                    print(i, ':', product[i])
