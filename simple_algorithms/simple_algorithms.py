'''Додати тести до реалізованих методів.

1. Обчислення суми усіх елементів списку. Назвати функцію - calculate_sum(list),
функція приймає список, вертає суму усіх значень.

2. Пошук максимального елемента списку. Назвати функцію - find_max(list), функція приймає список,
	повертає одне максимальне значення (якщо це цифра то число, якщо слово, то найдовше)

3. Обчислення факторіала числа. Назвати функцію - factorial(n), функція приймає число і повертає його факторіал.

4. Лінійний пошук індекса елементу. Назвати функцію - find_index(list, val),
функція приймає список, а також елемент (значення) зі списку і повернутає індекст елемента.'''

def calculate_sum(list):

    sum = 0
    for i in list:
        sum += i
    return sum

def find_max(list):

    max_value = list[0]
    for i in list:
        if max_value < i:
            max_value = i

    return max_value


def factorial(n):

    '''funktija kurzja'''

    m = n
    for i in range(n):
        n_factorial = i*(i-m)
        m += 1
    return -n_factorial


def find_index(list, val):
    ###
    return index

#print(calculate_sum([1,2,3,4]))

#print(find_max([56,76,21,34,59,12,16,98]))

#print(factorial(3))

#print('index of hello = ', find_index(['welcome', 'mariia', 'timur', 'hello',
                                                'world', 'sun'], 'hello'))
