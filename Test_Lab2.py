import Lab2

def test_find_min_max():
    output = []
    input_list = [10, 20, 1, 0]
    output = Lab2.find_min_max(input_list)
    assert (output == [0, 20])
def test_calc_average():
    input_list = [10, 20, 1, 0]
    output = Lab2.calc_average(input_list)
    assert (output == 7.75)
def test_calc_median_temperature():
    input_list = [0, 1, 10, 20]
    sort_list  = Lab2.sort_temperature(input_list)
    output = Lab2.calc_median_temperature(sort_list)
    assert (output == 5.5)
