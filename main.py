from link_reader import get_link_list
from parse_class import Parser
import xlwt
from PIL import Image



def main():
    products = Parser(get_link_list())

    font0 = xlwt.Font()
    font0.name = 'Times New Roman'
    font0.colour_index = 2
    font0.bold = True

    style0 = xlwt.XFStyle()
    style0.font = font0

    wb = xlwt.Workbook()
    ws = wb.add_sheet('A Test Sheet')

    count = 0
    for id in products.product_info_dict.keys():
        ws.write(count, 0, id)
        ws.write(count, 1, products.product_info_dict[id]['price'])
        ws.write(count, 2, products.product_info_dict[id]['name'])

        out = open("img.jpeg", "wb")
        out.write(products.product_info_dict[id]['image'])
        out.close()
        Image.open('img.jpeg').save('img.bmp')
        ws.insert_bitmap('img.bmp', count+1, 3)

        ws.write(count, 4, products.product_info_dict[id]['description'])
        count+=1

    wb.save('products.xls')


if __name__ == '__main__':
    main()