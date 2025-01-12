'''
Певний роздрібний продавець проводить розпродаж зі знижкою 60% на різноманітні зняті з виробництва товари.
Продавець хотів би допомогти своїм клієнтам визначити знижені ціни на товари,
використовуючи надруковану таблицю знижок на полиці, яка показує початкові ціни
та ціни після застосування знижки.

Напишіть програму, яка використовує цикл для створення цієї таблиці,
показуючи початкову ціну, розмір знижки
та нову ціну для покупок за $4.95, $9.95, $14.95, $19.95 і $24.95.
Переконайтеся, що розміри знижок і нові ціни округлені до 2 десяткових знаків,
коли вони відображаються.'''

def create_price_table(prices, discount):

    '''this function's arguments are old prices and discount in %.
        It generates discounts, calculates the new price and creates a table
        with three columns: price old, price new, discount'''

    price_table = []

    row = []
    price = prices[0]
    row.append(price)
    row.append(price*discount)
    row.append(row[0] - row[1]) 

    price_table.append(row)


    return price_table


def print_prices_with_discount(price_table):

    for price in price_table:
        print(f"{price[0]}\t{round(price[1], 2)}\t{round(price[2], 2)}")


def main():
            
    prices = [4.95, 9.95, 14.95, 19.95, 24.95]

    price_table = create_price_table(prices, 0.6)

    print_prices_with_discount(price_table)


if __name__ == "__main__":
    main()




'''
key     price_old   discount_size   price_new
apple   4.96,       3.12            1.84
water   9.95,       4.30            5.65
...

list[0][1]

for element in list:
    print(element[2])

list[1][0] 


'''




