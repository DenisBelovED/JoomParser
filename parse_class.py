import requests
import json


class Parser:
    init_url = r'https://www.joom.com/tokens/init'
    products_url = r'https://api.joom.com/1.1/search/products?language=ru-RU&currency=RUB'

    def __init__(self, links_list):
        self.links = links_list
        self.product_info_dict = {}
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
                self.product_info_dict.update({
                    product['id']:
                        dict(
                            price=product['price'],
                            name=product['name'],
                            image=product['mainImage'],
                            description=self.get_description(product['id'], headers)
                        )
                })
        print(self.product_info_dict)


    def get_description(self, id_str, headers):
        link = 'https://api.joom.com/1.1/products/'+id_str+'?language=ru-RU&currency=RUB'
        res = requests.get(link, headers=headers)
        return json.loads(res.text)['payload']['description']
