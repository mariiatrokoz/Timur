import sys

if len(sys.argv) == 1:
    print('Enter a digit')
    exit()

if not sys.argv[1].isdigit():
    print('Enter a digit!!!')
    exit()

pyramida_size = int(sys.argv[1])

stars_to_remove = pyramida_size - (2 if pyramida_size % 2 == 0 else 1)

while stars_to_remove >= 0:

    stars_to_print = pyramida_size - stars_to_remove
    spaces = ' ' * int(stars_to_remove / 2)

    print(spaces + ('*' * stars_to_print) + spaces)
    
    stars_to_remove -= 2
