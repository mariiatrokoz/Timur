def taxi_fares(distance_km):

    dist = float(distance_km)

    fare_add = (dist/0.14)*0.25

    fare_tot = 4+fare_add

    return fare_tot


def main():

    distance = float(input("enter distance travelled in km: "))

    price = taxi_fares(distance)

    print("price: ", price, "$")


if __name__ == "__main__":
    main()
