from link_reader import get_link_list
from parse_class import Parser


def main():
    products = Parser(get_link_list())


if __name__ == '__main__':
    main()