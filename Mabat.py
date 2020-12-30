import enum


class BURDEN(enum.Enum):
    Morning = 3
    Noon = 2
    Evening = 1


SPEED_CAR = 160
SPEED_BUS = 150
SPEED_TAXI = 180

DISTANCE = int(input("Enter the distance from your destination:"))

if DISTANCE < 0:
    print("Error")
elif DISTANCE == 0:
    print("No need for traveling - you are at your destination.")
else:
    TIME_OF_DAY = input("What time of the day it is?")
    TRAVELING_OPTION = input("Which traveling option do you prefer?")

    if TRAVELING_OPTION == "Private":
        PRICE_FOR_HOUR = int(input("What is the price of an hour of traveling?"))
        if PRICE_FOR_HOUR <= 0:
            print("Error")
        else:
            speed_car = SPEED_CAR / BURDEN[TIME_OF_DAY].value
            time_car = round((DISTANCE / speed_car), 2)
            total_price_car = round(time_car * PRICE_FOR_HOUR)
            print("You chose to travel in the car.")
            print("It will take", time_car, "hours, and it will cost", total_price_car, "shekels.")
    elif TRAVELING_OPTION == "Public":
        PRICE_FOR_HOUR = int(input("What is the price of an hour of traveling?"))
        if PRICE_FOR_HOUR <= 0:
            print("Error")
        else:
            speed_taxi = SPEED_TAXI / (BURDEN[TIME_OF_DAY].value + 2)
            time_taxi = round((DISTANCE / speed_taxi), 2)
            total_price_taxi = round(time_taxi * PRICE_FOR_HOUR) + 50

            PASSENGERS_ON_BUS = int(input("How many passengers there are on the bus?"))

            if PASSENGERS_ON_BUS < 20:
                PASSENGERS_ON_BUS = 20

            if TIME_OF_DAY == "Evening":
                speed_bus = SPEED_BUS
            else:
                speed_bus = (SPEED_BUS - PASSENGERS_ON_BUS) / BURDEN[TIME_OF_DAY].value
            time_bus = round((DISTANCE / speed_bus), 2)
            total_price_bus = round(time_bus * PRICE_FOR_HOUR)

            if time_taxi > time_bus and total_price_taxi > total_price_bus:
                print("You chose to travel in public transport.")
                print("The best option is the bus.")
                print("It will take", time_bus,  "hours, and it will cost", total_price_bus, "shekels.")
            else:
                print("You chose to travel in public transport.")
                print("The best option is the taxi.")
                print("It will take", time_taxi, "hours, and it will cost", total_price_taxi, "shekels.")
    else:
        print("Error")


