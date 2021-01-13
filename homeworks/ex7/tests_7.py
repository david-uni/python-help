import sys
import timeit


def did_pass(question, errors, warnings=None):
    if warnings == None:
        warnings = []
    if not errors:
        message = f'question {question} passed the tests'
        print(message, f'but with warnings: {warnings}' if warnings else '')
    else:
        print(
            f'question {question} failed the tests, with {len(errors)} errors:', errors)


def is_recursive(function, large_case, errors):
    previous_limit = sys.getrecursionlimit()
    sys.setrecursionlimit(50)
    try:
        if type(large_case) == list:
            function(*large_case)
        else:
            function(large_case)
        errors.append('not recursive')
    except RecursionError as error:
        if 'maximum recursion depth exceeded' not in error.args[0]:
            errors.append(f'an unexpected error has occurred: {error}')
    except Exception as err:
        errors.append(f'an unexpected error has occurred: {err}')
    finally:
        sys.setrecursionlimit(previous_limit)


def execution_time(function, arguments):
    start = timeit.default_timer()
    function(*arguments)
    return timeit.default_timer() - start


def is_faster(large_case, fun_rec, fun_memo, warnings):
    min_time_diff = 1
    rec_time = execution_time(fun_rec, large_case)
    memo_time = execution_time(fun_memo, large_case)
    if not memo_time < rec_time - min_time_diff:
        warnings.append(
            f'memo version took: {memo_time} seconds and the simple one took: {rec_time} seconds')


def q1_test(function):
    errors = []
    is_recursive(function, 200, errors)
    cases = {0: 0, 1: 1, 2: 2, 3: 3, 4: 6, 5: 12,
             6: 23, 7: 44, 10: 316, 12: 1174}
    for case, result in cases.items():
        if function(case) != result:
            errors.append(f'doesn\'t work with n = {case}')
    return errors


def q1_part_a_test():
    try:
        return did_pass('1 part a', q1_test(four_bonacci_rec))
    except:
        print('question 1 part a raised an unexpected error')


def q1_part_b_test():
    try:
        warnings = []
        is_faster([26], four_bonacci_rec, four_bonacci_mem, warnings)
        return did_pass('1 part b', q1_test(four_bonacci_mem), warnings)
    except:
        print('question 1 part b raised an unexpected error')


def q2_test():
    try:
        errors = []
        is_recursive(climb_combinations_memo, 200, errors)
        cases = {1: 1, 2: 2, 3: 3, 11: 144, 29: 832040}
        for case, result in cases.items():
            if climb_combinations_memo(case) != result:
                errors.append(f'doesn\'t work with n = {case}')
        warnings = []
        is_faster([31], climb_combinations_rec,
                  climb_combinations_memo, warnings)
        return did_pass(2, errors, warnings)
    except:
        print('question 2 raised an unexpected error')


def climb_combinations_rec(n):
    if n < 2:
        return 1
    return sum(climb_combinations_rec(n-i) for i in range(1, 3))


def q3_test():
    try:
        errors = []
        is_recursive(catalan_rec, 100, errors)
        cases = {0: 1, 1: 1, 2: 2, 11: 58786, 20: 6564120420}
        for n, res in cases.items():
            if catalan_rec(n) != res:
                errors.append(f'doesn\'t work with n = {n}')
        return did_pass(3, errors)
    except:
        print('question 3 raised an unexpected error')


def q4_test(function):
    errors = []
    is_recursive(function, [200, [1, 2, 3, 4, 5]], errors)
    cases = {(0, tuple()): 1, (0, (1,)): 1, (1, tuple()): 0, (1, (1,)): 1, (2, (1, 2)): 2, (1, (2,)): 0, (40, (10, 5, 2, 7, 1)): 438}
    for (num, coins), res in cases.items():
        if function(num, list(coins)) != res:
            errors.append(
                f'doesn\'t work with num = {num} and coins = {list(coins)}')
    return errors


def q4_part_a_test():
    try:
        return did_pass('4 part a', q4_test(find_num_changes_rec))
    except:
        print('question 4 part a raised an unexpected error')


def q4_part_b_test():
    try:
        warnings = []
        is_faster([150, [1, 3, 5, 4, 2]], find_num_changes_rec,
                  find_num_changes_mem, warnings)
        return did_pass('4 part b', q4_test(find_num_changes_mem), warnings)
    except:
        print('question 4 part b raised an unexpected error')


q1_part_a_test()
q1_part_b_test()
q2_test()
q3_test()
q4_part_a_test()
q4_part_b_test()
