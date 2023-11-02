import statistics

print("ET0735 (DevOps for AIoT) -  Lab 2 - Introduction to Python")

# Exercise 2
def display_main_menu():
    print('Enter some numbers seperated by commas (e.g. 5, 67, 32): ')
    # Exercise 3

def get_user_input():
    print('get user input')
    # Exercise 3
    user_input = input()
    filtered_list = user_input.split(', ')
    test_list =list((filtered_list))
    return [float(ele) for ele in test_list]

def calc_average(List):
    print('calculate average')
    # Exercise 4
    total = 0
    for x in List:
        total += x
    avg = total/ len(List)
    print('Average = ' + str(avg))
    return avg

def find_min_max(List):
    print('find minimum maximum')
    mlist = List
    max_value = max(mlist)
    min_value = min(mlist)
    print('Maximum = ' + str(max_value))
    print('Minimum = ' + str(min_value))

    return [min_value, max_value]

def sort_temperature(List):
    print('sort temperature')
    return sorted(List)

def calc_median_temperature(SortList):
    print('calculate median temperature')
    mid = sort_temperature(SortList)
    mid_value = statistics.median(mid)
    print('median temperature = ' + str(mid_value))
    return mid_value

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    calc_average(num_list)
    find_min_max(num_list)
    sort_list = sort_temperature(num_list)
    calc_median_temperature(sort_list)

if __name__ == "__main__":
    main()


