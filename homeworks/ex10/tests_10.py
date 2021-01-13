def test_a_part1():
    phrase1 = 'hello world'
    phrase2 = 'hello david'
    phrase3 = 'aaaaaaaaaaa'
    a1 = ascii_to_np_array(phrase1)
    a2 = ascii_to_np_array(phrase2)
    a3 = ascii_to_np_array(phrase3)
    assert arr_dist(a1, a1) == 0
    assert arr_dist(a3, a3) == 0
    assert arr_dist(a1, a2) == 40
    assert arr_dist(a1, a3) == 179


def test_a_part2():
    phrase1 = 'pass the w'
    phrase2 = 'pass the a'
    phrase3 = 'pass the z'
    phrase4 = 'winner'
    im1 = np.vstack((np.zeros((10, 10)), ascii_to_np_array(
        phrase2), ascii_to_np_array(phrase3), ascii_to_np_array(phrase1)))
    im2 = np.vstack((np.hstack((np.zeros(4), ascii_to_np_array(phrase4))), np.zeros((5, 10)), ascii_to_np_array(
        phrase2), ascii_to_np_array(phrase3), ascii_to_np_array(phrase1)))
    assert find_best_place(im1, ascii_to_np_array(phrase1)) == (12, 0)
    assert find_best_place(im2, ascii_to_np_array(phrase4)) == (0, 4)


def test_a_part3():
    phrase1 = 'pass the w'
    phrase2 = 'pass the a'
    phrase3 = 'pass the z'
    phrase4 = 'winner'
    im1 = np.vstack((np.zeros((10, 10)), ascii_to_np_array(
        phrase2), ascii_to_np_array(phrase3), ascii_to_np_array(phrase1)))
    im2 = np.vstack((np.hstack((np.zeros(4), ascii_to_np_array(phrase4))), np.zeros((5, 10)), ascii_to_np_array(
        phrase2), ascii_to_np_array(phrase3), ascii_to_np_array(phrase1)))
    new_im1 = create_image_with_msg(
        im1, (12, 0), ascii_to_np_array(phrase1))
    new_im2 = create_image_with_msg(
        im1, (0, 4), ascii_to_np_array(phrase4))
    assert (new_im1[0, :3] == np.array([12, 0, 10])).all()
    assert (new_im1[12, :] == ascii_to_np_array(phrase1)).all()
    assert new_im1.dtype == np.uint8
    assert (new_im2[0, :3] == np.array([0, 4, 6])).all()
    assert (new_im2[0, 4:] == ascii_to_np_array(phrase4)).all()
    assert new_im2.dtype == np.uint8


def test_a_part4():
    phrase1 = 'pass the w'
    phrase2 = 'pass the a'
    phrase3 = 'pass the z'
    phrase4 = 'winner'
    im1 = np.vstack((np.zeros((10, 10)), ascii_to_np_array(
        phrase2), ascii_to_np_array(phrase3), ascii_to_np_array(phrase1)))
    new_im1 = put_message(im1, phrase1)
    assert (new_im1[0, :3] == np.array([12, 0, 10])).all()
    assert (new_im1[12, :] == ascii_to_np_array(phrase1)).all()
    assert new_im1.dtype == np.uint8


def test_a_part5():
    phrase1 = 'pass the w'
    phrase2 = 'winner'
    im1 = np.array([[12., 0., 10.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                    [0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                    [0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                    [0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                    [0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                    [0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                    [0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                    [0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                    [0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                    [0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                    [112., 97., 115., 115., 32., 116., 104., 101., 32., 97.],
                    [112., 97., 115., 115., 32., 116., 104., 101., 32., 122.],
                    [112., 97., 115., 115., 32., 116., 104., 101., 32., 119.]], dtype=np.uint8)
    im2 = np.array([[0., 4.,  6.,  0., 119., 105., 110., 110., 101., 114.],
                    [0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                    [0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                    [0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                    [0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                    [0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                    [0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                    [0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                    [0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                    [0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
                    [112., 97., 115., 115., 32., 116., 104., 101., 32., 97.],
                    [112., 97., 115., 115., 32., 116., 104., 101., 32., 122.],
                    [112., 97., 115., 115., 32., 116., 104., 101., 32., 119.]], dtype=np.uint8)
    assert get_message(im1) == phrase1
    assert get_message(im2) == phrase2


test_a_part1()
test_a_part2()
test_a_part3()
test_a_part4()
test_a_part5()


def test_b_part1():
    try:
        read_missions_file('non existing file')
        assert False
    except IOError as error:
        assert error.args[0] == 'An IO error occurred'
    except:
        assert False

    try:
        file_name = 'missions.csv'
        csv = read_missions_file(file_name)
        assert (csv.columns == ['Bounty', 'Expenses', 'Duration']).all()
        assert (csv.index == ['Temeria', 'Redania',
                              'Kaedwen', 'Cintra']).all()
    except:
        assert False


def test_b_part2():
    csv = pd.DataFrame({'Bounty': [1000, 1500, 500, 2500], 'Expenses': [250, 500, 100, 2000], 'Duration': [5, 3, 7, 3]}, index=['Temeria', 'Redania',
                                                                                                                                'Kaedwen', 'Cintra'])
    daily_gain = pd.DataFrame(
        {'Daily gain': [(1000-250)/5, (1500-500)/3, (500-100)/7, (2500-2000)/3]},  index=['Temeria', 'Redania',
                                                                                          'Kaedwen', 'Cintra'])
    add_daily_gain_col(csv)
    assert (csv['Daily gain'] == daily_gain['Daily gain']).all()


def test_b_part3():
    csv = pd.DataFrame({'Bounty': [1000, 1500, 500, 2500], 'Expenses': [250, 500, 100, 2000], 'Duration': [5, 3, 7, 3]}, index=['Temeria', 'Redania',
                                                                                                                                'Kaedwen', 'Cintra'])
    assert sum_rewards(csv) == 2650


def test_b_part4():
    csv = pd.DataFrame({'Bounty': [1000, 1500, 500, 2500], 'Expenses': [250, 500, 100, 2000], 'Duration': [5, 3, 7, 3]}, index=['Temeria', 'Redania',
                                                                                                                                'Kaedwen', 'Cintra'])
    assert find_best_kingdom(csv) == 'Redania'


def test_b_part5():
    csv = pd.DataFrame({'Bounty': [1000, 1500, 500, 2500], 'Expenses': [250, 500, 100, 2000], 'Duration': [5, 3, 7, 3]}, index=['Temeria', 'Redania',
                                                                                                                                'Kaedwen', 'Cintra'])
    assert find_best_duration(csv) == 3


test_b_part1()
test_b_part2()
test_b_part3()
test_b_part4()
test_b_part5()
