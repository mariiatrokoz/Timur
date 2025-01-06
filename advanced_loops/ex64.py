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


def print_prices_with_discount(price_tablet):
    
    for price in price_tablet:
        print(f"{price[0]}\t{round(price[1], 2)}\t{round(price[2], 2)}")


def create_price_table(prices, discount):
    price_table = []
    
    #...
    #...
    
    return price_table


prices = [4.95, 9.95, 14.95, 19.95, 24.95]

#for price in prices:
#    discount = round(price * 0.6, 2)
#    print(f"{price}\t{round(price - discount, 2)}\t{discount}")

price_table = create_price_table(prices, 0.6)

print_prices_with_discount(price_table)




'''
key     price   discount_size
apple   4.96,   3.12
water   9.95,   4.30
...

'''
