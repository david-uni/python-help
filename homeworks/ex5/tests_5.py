import os


def get_file_name():
    i = 0
    while True:
        name = f'test_file_{i}.txt'
        if not os.path.exists(name):
            return name
        i += 1


def remove_files(*files_name):
    for file_name in files_name:
        if os.path.exists(file_name):
            os.remove(file_name)


def check_file_content(file_name, content):
    try:
        with open(file_name, 'r') as f:
            return content == f.readlines()
    except:
        return False


def exercise_1_test():
    errors = []
    file_name = get_file_name()
    with open(file_name, 'w') as f:
        f.write('22 55 111 99999 2')
    try:
        if sum_nums(file_name) != (22 + 55 + 111 + 99999 + 2):
            errors.append("doesn't work :(")
        with open(file_name, 'w') as f:
            f.write(' 22 55 111 99999 2')
        if sum_nums(file_name) != (22 + 55 + 111 + 99999 + 2):
            errors.append("doesn't work when the line starts with a space")
        with open(file_name, 'w') as f:
            f.write(' 22 55 111 99999 2 \n')
        if sum_nums(file_name) != (22 + 55 + 111 + 99999 + 2):
            errors.append("doesn't work when the line ends with a spaces")
    except:
        errors.append('your code raise an unexpected error')
    finally:
        remove_files(file_name)
    if errors:
        print('questions 1 failed the tests, with the following errors', errors)
    else:
        print('questions 1 passed the tests')


def exercise_2_test():
    errors = []
    target_str = 'bla bla'

    in_file_name = get_file_name()
    with open(in_file_name, 'w') as f:
        f.writelines([f'correct {target_str}\n',
                      'not correct\n', f'{target_str} correct\n'])
    out_file_name = get_file_name()
    try:
        copy_lines_with_str(in_file_name, out_file_name, target_str)
        if not check_file_content(out_file_name, [f'correct {target_str}\n', f'{target_str} correct\n']):
            errors.append(
                "doesn't copy the matching lines")
    except:
        errors.append(
            'the code raised an unexpected error')
    finally:
        remove_files(in_file_name, out_file_name)

    in_file_name = get_file_name()
    with open(in_file_name, 'w') as f:
        pass
    out_file_name = get_file_name()
    try:
        copy_lines_with_str(in_file_name, out_file_name, target_str)
        if not check_file_content(out_file_name, []):
            errors.append("doesn't work when given an empty file")
    except:
        errors.append(
            'the code raised an unexpected error when given an empty file')
    finally:
        remove_files(in_file_name, out_file_name)

    in_file_name = get_file_name()
    with open(in_file_name, 'w') as f:
        f.writelines(['not correct\n', 'not correct\n'])
    out_file_name = get_file_name()
    try:
        copy_lines_with_str(in_file_name, out_file_name, target_str)
        if not check_file_content(out_file_name, []):
            errors.append(
                "doesn't work when given a file without the target_str")
    except:
        errors.append(
            'the code raised an unexpected error')
    finally:
        remove_files(in_file_name, out_file_name)

    in_file_name = get_file_name()
    with open(in_file_name, 'w') as f:
        f.writelines(
            [f'not correct {target_str.upper()}\n', f'{target_str} correct\n'])
    out_file_name = get_file_name()
    try:
        copy_lines_with_str(in_file_name, out_file_name, target_str)
        if not check_file_content(out_file_name, [f'{target_str} correct\n']):
            errors.append(
                "isn't case sensitive")
    except:
        errors.append(
            'the code raised an unexpected error')
    finally:
        remove_files(in_file_name, out_file_name)

    in_file_name = get_file_name()
    out_file_name = get_file_name()
    try:
        copy_lines_with_str(in_file_name, out_file_name, target_str)
    except:
        errors.append("doesn't handle IOError")
    finally:
        remove_files(out_file_name)

    in_file_name = get_file_name()
    with open(in_file_name, 'w') as f:
        pass
    out_file_name = get_file_name()
    with open(out_file_name, 'w') as f:
        try:
            copy_lines_with_str(in_file_name, out_file_name, target_str)
        except:
            errors.append("the code raised an unexpected error")
    remove_files(in_file_name, out_file_name)

    in_file_name = get_file_name()
    with open(in_file_name, 'w') as f:
        f.writelines([f'{target_str} correct\n'])
    out_file_name = get_file_name()
    with open(out_file_name, 'w') as f:
        f.write('needs to be erased')
    try:
        copy_lines_with_str(in_file_name, out_file_name, target_str)
        if not check_file_content(out_file_name, [f'{target_str} correct\n']):
            errors.append("doesn't erase the previous file")
    except:
        errors.append("the code raised an unexpected error")
    finally:
        remove_files(in_file_name, out_file_name)

    if errors:
        print('questions 2 failed the tests, with the following errors', errors)
    else:
        print('questions 2 passed the tests')


def exercise_3_test():
    errors = []

    result_1 = ['3,5\n']
    result_2 = ['3,5\n', '5,7\n', '11,13\n']
    for result in [result_1, result_2]:
        file_name = get_file_name()
        try:
            num = len(result)
            write_twin_primes(num, file_name)
            if not check_file_content(file_name, result):
                errors.append(f"doesn't work for num = {num}")
        except:
            errors.append('the code raised an unexpected error')
        finally:
            remove_files(file_name)

    for num in [0, -1, -10]:
        file_name = get_file_name()
        try:
            write_twin_primes(num, file_name)
            errors.append(f"didn't raise an error for num = {num}")
        except ValueError as error:
            if error.args[0] != f'Illegal value num={num}':
                errors.append(f'wrong error message for num = {num}')
        except:
            errors.append('the code raised an unexpected error')
        finally:
            remove_files(file_name)

    file_name = get_file_name()
    with open(file_name, 'w') as f:
        try:
            write_twin_primes(3, file_name)
        except:
            errors.append("doesn't handle IOError")
    remove_files(file_name)

    if errors:
        print('questions 3 failed the tests, with the following errors', errors)
    else:
        print('questions 3 passed the tests')


def exercise_4_test():
    errors = []
    round_test = [
        'The winner takes it all,ABBA,8\n',
        'While my guitar gently weeps,The Beatles,8\n',
        'The winner takes it all,ABBA,9\n',
        'While my guitar gently weeps,The Beatles,9\n',
        'While my guitar gently weeps,The Beatles,9\n',
        'Fake plastic trees,Radiohead,1\n',
        'Fake plastic trees,Radiohead,1\n',
        'Fake plastic trees,Radiohead,11\n'
    ]
    result = {'ABBA': 8, 'Radiohead': 4, 'The Beatles': 9}
    without_radiohead = ['The winner takes it all,ABBA,8\n',
                         'While my guitar gently weeps,The Beatles,63\n', 'The winner takes it all,ABBA,8\n']
    without_beatles = ['The winner takes it all,ABBA,8\n',
                       'Fake plastic trees,Radiohead,11\n', 'The winner takes it all,ABBA,8\n']
    without_abba = ['Here comes the sun,The Beatles,8\n',
                    'Fake plastic trees,Radiohead,11\n', 'Here comes the sun,The Beatles,8\n']
    special_without = ['ABBA,The Beatles,8\n',
                       'Fake plastic trees,Radiohead,11\n', 'Here comes the sun,The Beatles,8\n']

    file_name = get_file_name()
    with open(file_name, 'w') as f:
        f.writelines(round_test)
    try:
        if calc_avg_position_per_band(file_name) != result:
            errors.append(
                "doesn't work (maybe you forgot to round the numbers)")
    except:
        errors.append('the code raised an unexpected error')
    finally:
        remove_files(file_name)

    for i, case in enumerate([without_abba, without_beatles, without_radiohead]):
        file_name = get_file_name()
        with open(file_name, 'w') as f:
            f.writelines(case)
        try:
            calc_avg_position_per_band(file_name)
            errors.append(
                f"didn't raise as error for missing band ({'ABBA' if i == 0 else 'The Beatles' if i == 1 else 'Radiohead'})")
        except ValueError as error:
            if error.args[0] != f'At least one of the bands does not appear in the file {file_name}':
                errors.append('wrong error message in case of a missing band')
        except:
            errors.append('the code raised an unexpected error')
        finally:
            remove_files(file_name)

    file_name = get_file_name()
    with open(file_name, 'w') as f:
        pass
    try:
        calc_avg_position_per_band(file_name)
        errors.append(f"didn't raise as error for missing band")
    except ValueError as error:
        if error.args[0] != f'At least one of the bands does not appear in the file {file_name}':
            errors.append('wrong error message in case of a missing band')
    except:
        errors.append(
            'the code raised an unexpected error when given an empty file')
    finally:
        remove_files(file_name)

    file_name = get_file_name()
    with open(file_name, 'w') as f:
        f.writelines(special_without)
    try:
        calc_avg_position_per_band(file_name)
        errors.append(
            f"didn't raise as error for missing band (I put the name of the missing band as a *song* of another one)")
    except ValueError as error:
        if error.args[0] != f'At least one of the bands does not appear in the file {file_name}':
            errors.append('wrong error message in case of a missing band')
    except:
        errors.append(
            'the code raised an unexpected error')
    finally:
        remove_files(file_name)

    if errors:
        print('questions 4 failed the tests, with the following errors', errors)
    else:
        print('questions 4 passed the tests')


exercise_1_test()
exercise_2_test()
exercise_3_test()
exercise_4_test()
