def my_func(list_of_prices):

    # calculate discount
    # calculate price_new
    # round
    # generate table

    # Заголовок таблиці
    print(f"{'Початкова ціна ($)':<20}{'Розмір знижки ($)':<20}{'Нова ціна ($)':<20}")

    # Генерація таблиці
    for original_price in list_of_prices:

        discount_amount = round(original_price * discount_rate, 2)
        new_price = round(original_price - discount_amount, 2)
        print(f"{original_price:<20.2f}{discount_amount:<20.2f}{new_price:<20.2f}")


original_prices = [4.95, 9.95, 14.95, 19.95, 24.95]
discount_rate = 0.60

print(my_func(original_prices))
