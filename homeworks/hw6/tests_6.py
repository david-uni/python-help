import sys


def did_pass(question_number, errors):
    if not errors:
        print(f'question {question_number} passed the tests')
    else:
        print(
            f'question {question_number} failed the tests, with {len(errors)} errors:', errors)


def is_recursive(function, large_case, errors):
    previous_limit = sys.getrecursionlimit()
    sys.setrecursionlimit(50)
    try:
        function(large_case)
        errors.append('not recursive')
    except RecursionError as error:
        if 'maximum recursion depth exceeded' not in error.args[0]:
            errors.append('an unexpected error has occurred')
    except:
        errors.append('an unexpected error has occurred')
    finally:
        sys.setrecursionlimit(previous_limit)


def q1_test():
    errors = []
    is_recursive(reverse_string, 'a' * 200, errors)
    if reverse_string('') != '':
        errors.append('doesn\'t work with an empty string')
    if reverse_string('a') != 'a':
        errors.append('doesn\'t work with a single character')
    if reverse_string('ab') != 'ba':
        errors.append('doesn\'t work with two characters')
    if reverse_string('asd123') != '321dsa':
        errors.append('doesn\'t work with multiple characters')
    if reverse_string('Aba') != 'abA':
        errors.append('shouldn\'t change the the letters')
    return did_pass(1, errors)


def q2_test():
    errors = []
    is_recursive(find_maximum, [1] * 200, errors)
    if find_maximum([]) != -1:
        errors.append('doesn\'t work with an empty list')
    if find_maximum([9]) != 9:
        errors.append('doesn\'t work with a single number')
    if find_maximum([3, 5, 2, 1, 10, 7, 11]) != 11:
        errors.append('doesn\'t work with the biggest as last')
    if find_maximum([11, 3, 5, 2, 1, 10, 7]) != 11:
        errors.append('doesn\'t work with the biggest as first')
    if find_maximum([3, 5, 2, 1, 11, 10, 7]) != 11:
        errors.append('doesn\'t work with multiple numbers')
    if find_maximum([0, 0, 0]) != 0:
        errors.append('doesn\'t work with 0')
    return did_pass(2, errors)


def q3_test():
    errors = []
    is_recursive(is_palindrome, 'a' * 200, errors)
    if is_palindrome('a') != True:
        errors.append('doesn\'t work with a single character')
    if is_palindrome('aba') != True:
        errors.append('doesn\'t work with \'aba\'')
    if is_palindrome('Aba') != False:
        errors.append('\'A\' is not equal to \'a\'')
    if is_palindrome('123321') != True:
        errors.append('doesn\'t work with numbers as string')
    if is_palindrome('abcdcba') != True:
        errors.append('doesn\'t work with odd number of chars')
    if is_palindrome('abccba') != True:
        errors.append('doesn\'t work with even number of chars')
    if is_palindrome('adaa') != False:
        errors.append('doesn\'t check more than the first two ends')
    if is_palindrome('abcdcbd') != False:
        errors.append('doesn\'t work')
    return did_pass(3, errors)


def q4_test():
    errors = []
    is_recursive(climb_combinations, 200, errors)
    cases = [(1, 1), (2, 2), (3, 3), (9, 55), (11, 144)]
    for num, res in cases:
        if climb_combinations(num) != res:
            errors.append(f'doesn\'t work with {num}')
    return did_pass(4, errors)


def q5_test():
    errors = []
    is_recursive(is_valid_paren, '(' * 200, errors)
    case = ''
    if is_valid_paren(case) != True:
        errors.append('doesn\'t work with an empty string')
    cases = [('aaa', True), ('()', True), (')(', False), ('()()', True), ('(', False), (')', False), ('(())', True), ('(()(()))', True), ('(()', False), ('())', False),
             ('aa()', True), ('()aa', True), ('(aa)', True), ('(aa)', True), ('aaa(aaa(aaa)a((aaaa)aaa)aa)aaa', True), ('aaa(aaa(aaa)a((aaaa)aaa)aaaaa', False)]
    for case, res in cases:
        if is_valid_paren(case) != res:
            errors.append(f'doesn\'t work with {case}')
    return did_pass(5, errors)


q1_test()
q2_test()
q3_test()
q4_test()
q5_test()
