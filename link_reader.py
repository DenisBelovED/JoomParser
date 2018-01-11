def get_link_list():
    with open('links.txt', 'r', encoding='utf-8') as links:
        return [str[:-1] for str in links.readlines()]