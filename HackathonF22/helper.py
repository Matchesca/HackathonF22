import pandas as pd

items = pd.read_csv('items.csv')
# print(items)


def get_price(prod_id):
    list_of_ids = items.loc[:, 'Product ID']
    for i in list_of_ids:
        temp = i[:-1]
        temp = temp[:5]
        # print(temp)
        if prod_id == temp:

            temp = items.loc[items['Product ID'] == i]
            # print(temp)
            price = temp.loc[:, 'Pirce']
            for x in price:
                return x


def get_name(prod_id):
    list_of_ids = items.loc[:, 'Product ID']
    for i in list_of_ids:
        temp = i[:-1]
        temp = temp[:5]
        if prod_id == temp:

            temp = items.loc[items['Product ID'] == i]
            price = temp.loc[:, 'Product Name']
            for x in price:
                return x
