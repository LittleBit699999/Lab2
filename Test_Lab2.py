import Lab2


def test_lab2_avg():
    test_list = [5, 67, 32]
    avg = Lab2.calc_average_temperature(test_list)

    assert (avg == 34.67)


def test_lab2_minmax():
    test_list = [5, 67, 32]
    temp_list = Lab2.calc_min_max_temperature(test_list)

    assert (temp_list == [5, 67])


def test_lab2_sort_temp():
    test_list = [5, 67, 32]
    sort_list = Lab2.sort_temperature(test_list)
    assert (sort_list == [5, 32, 67])


def test_lab2_calc_median():
    test_list = [5, 67, 32]
    cal_m = Lab2.calc_median_temperature(test_list)
    assert (cal_m == 32)

