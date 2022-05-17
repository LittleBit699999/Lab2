def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by comas(e.g. 5,67,32)")


def get_user_input():
    num_list = []
    strinput = input()
    str_list = strinput.split(",")
    for item in str_list:
        num_list.append(int(item))

    return num_list


def calc_average_temperature(num_list):
    print("calc_average_temperature")
    avg = sum(num_list)/len(num_list)
    return round(avg,2)


def calc_min_max_temperature(num_list):
    print("calc_min_max_temperature")
    max_temp = max(num_list)
    min_temp = min(num_list)
    temp_list = [min_temp, max_temp]
    return temp_list


def main():
    print("ET0735 (DevOps for AloT) - lab2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print(num_list)
    print(str(type(num_list[0])))
    average = calc_average_temperature(num_list)
    print("Average temperature is", average)
    temp_list = calc_min_max_temperature(num_list)
    print("The minimum and maximum temperature in the num_list are", temp_list, "respectively")


if __name__ == "__main__":
    main()
