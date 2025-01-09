def compute_the_hypotenuse(length1, length2):

    hypotenuse = (length1**2 + length2**2)**(1/2)

    return round(hypotenuse, 2)


def main():

    shorter_side1 = int(input("shorter_side_1: "))
    shorter_side2 = int(input("shorter_side_2: "))

    result = compute_the_hypotenuse(shorter_side1, shorter_side2)

    print(result)

main()
