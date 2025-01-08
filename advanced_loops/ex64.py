'''
Певний роздрібний продавець проводить розпродаж зі знижкою 60% на різноманітні зняті з виробництва товари.
Продавець хотів би допомогти своїм клієнтам визначити знижені ціни на товари,
використовуючи надруковану таблицю знижок на полиці, яка показує початкові ціни
та ціни після застосування знижки.

Напишіть програму, яка використовує цикл для створення таблиці,
показуючи початкову ціну, розмір знижки
та нову ціну для покупок за $4.95, $9.95, $14.95, $19.95 і $24.95.
Переконайтеся, що розміри знижок і нові ціни округлені до 2 десяткових знаків,
коли вони відображаються.'''

import numpy as np

def create_price_table(some_prices, discount):

    '''this function's arguments are old prices and discount in %.
        It generates discounts, calculates the new price and creates a table
        with three columns: price old, price new, discount'''

    price_table = []

    for price in some_prices:

        price_table.append(price)
        discount = round(price * 0.6, 2)
        price_table.append(discount)
        new_price=price-discount
        price_table.append(new_price)


    return price_table


def prices_with_discount(price_table):

        list_of_lists = []

        for row in range(0,3):

            rowlist = [round(e,2) for e in range(row, row+3)]
            list_of_lists.append(rowlist)

        return list_of_lists
        #print(f"{price}\t{round(price - discount, 2)}\t{discount}")
        #print(f"{price[0]}\t{round(price[1], 2)}\t{round(price[2], 2)}")

#sdef list_to_table():

prices = [4.95, 9.95, 14.95, 19.95, 24.95]

price_table = create_price_table(prices, 0.6)

b = prices_with_discount(price_table)

print(b)




'''
key     price   discount_size
apple   4.96,   3.12
water   9.95,   4.30
...

'''
