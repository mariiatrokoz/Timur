file = open("hello.txt", "r")

new_line_counter = 0

for char in file.read():
    if char == '\n':
        new_line_counter += 1

print("Total lines: ", new_line_counter)
