import Lab2


def test_lab2_avg():
    num_list = []
    test_list = [5, 67, 32]
    avg = Lab2.calc_average_temperature(test_list)

    assert (avg == 34.67)


def test_lab2_minmax():
    num_list = []
    test_list = [5, 67, 32]
    temp_list = Lab2.calc_min_max_temperature(test_list)

    assert(temp_list == [5, 67])
