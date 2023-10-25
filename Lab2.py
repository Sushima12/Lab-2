import statistics

print("ET0735 (DevOps for AIoT) -  Lab 2 - Introduction to Python")

# Exercise 2
def display_main_menu():
    print('display main menu')
    # Exercise 3
    u_input = input('Enter some numbers seperated by commas (e.g. 5, 67, 32): ')
    ulist = get_user_input(u_input)
    calc_average(ulist)
    find_min_max(ulist)
    calc_median_temperature(ulist)


def get_user_input(u):
    print('get user input')
    # Exercise 3
    user_input = u
    filtered_list = user_input.split(', ')
    test_list =list((filtered_list))
    temp_list = [float(ele) for ele in test_list]
    return temp_list

def calc_average(lists):
    print('calculate average')
    # Exercise 4
    total = 0
    for x in lists:
        total += x
    avg = total/ len(lists)
    print('Average = ' + str(avg))

def find_min_max(lists):
    print('find minimum maximum')

    mlist = lists
    max_value = max(mlist)
    min_value = min(mlist)

    print('Maximum = ' + str(max_value))
    print('Minimum = ' + str(min_value))


def sort_temperature(lists):
    print('sort temperature')
    return sorted(lists)


def calc_median_temperature(lists):
    print('calculate median temperature')
    mid = sort_temperature(lists)
    mid_value = statistics.median(mid)
    print('median temperature = ' + str(mid_value))


display_main_menu()

