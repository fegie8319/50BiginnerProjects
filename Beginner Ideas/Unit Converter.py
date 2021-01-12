# Implement a unit converter of your choice.Maybe Celsius to Fahrenheit, Meters to Feet or Euros to Dollars.
from retrying import retry

workflow = True


def leave_program():
    # leave program
    global workflow
    workflow = False
    print("Leaving...")
    return


@retry()
def temperature():
    global workflow
    print("1.c to f")
    print("2.f to c")
    print("0.leave")

    try:
        first_choose = input("Please choose which temperature converter you want or enter 0 to leave :")
        first_option = int(first_choose)
    except ValueError:
        print("Please enter an integer from 0 to 2")
        # return

    if first_option in range(0, 3):
        temp_input = input("temperature = :")
        try:
            temp_cal = float(temp_input)
            if first_option == 1:
                final_temp = float(temp_cal) * 9 / 5 + 32
                return final_temp
            elif first_option == 2:
                final_temp = (float(temp_cal) - 32) * 5 / 9
                return final_temp
            else:
                workflow = False
                print("Leaving...")
                return
        except ValueError:
            print("Please enter a float")
            temperature()

    else:
        print("The range is from 0 to 2")
        temperature()


@retry
def distance():
    pass


@retry
def main():
    try:
        main_choose = input("Please choose what converter you want, or enter 0 to exit :")
        main_option = int(main_choose)
    except ValueError:
        print("Please enter an integer from 0 to 3")

    if main_option not in range(0, 4):
        print("The range is from 0 to 4")

    if main_option == 0:
        leave_program()

    # temperature
    elif main_option == 1:
        print(f"the converted temperature is : {temperature()}")
    # distance
    elif main_option == 2:
        pass
    # money exchanges
    else:
        pass


print("1.temperature")
print("2.distance")
print("3.money exchanges")
print("0.leave")
while workflow:
    main()
