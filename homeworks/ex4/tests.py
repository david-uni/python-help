def check_question_1():
    errors = []
    if most_popular_character('daaabb') != 'a':
        errors.append('does\'t return the most popular character')
    if most_popular_character('bcad') != 'a':
        errors.append('does\'t return the smallest character')
    if most_popular_character('a') != 'a':
        errors.append('does\'t work when string length is 1')
    if most_popular_character('baaAABccdd') != 'A':
        errors.append(
            'does\'t work when two or more letters exist the same number of times')
    if len(errors) == 0:
        print('question 1 passed the tests')
    else:
        print('question 1 failed with the following errors:', errors)


def check_question_2():
    errors = []
    mat1 = {(0, 0): 1, (3, 6): 8}
    mat2 = {(0, 0): 2}
    mat3 = {(1, 1): 1}
    if diff_sparse_matrices([mat1.copy(), mat2.copy()]) != {(0, 0): -1, (3, 6): 8}:
        errors.append('does\'t subtract from the first dictionary')
    if diff_sparse_matrices([mat1.copy(), mat2.copy(), mat2.copy()]) != {(0, 0): -3, (3, 6): 8}:
        errors.append(
            'does\'t work if there are multiple matrix to substract')
    if diff_sparse_matrices([mat1.copy(), mat1.copy()]) != {}:
        errors.append('does\'t remove 0 values')
    if diff_sparse_matrices([mat1.copy(), mat3.copy()]) != {(0, 0): 1, (3, 6): 8, (1, 1): -1}:
        errors.append(
            'does\'t work when the index doesn\'t exist in the first matrix')
    if len(errors) == 0:
        print('question 2 passed the tests')
    else:
        print('question 2 failed with the following errors:', errors)


def check_question_3():
    errors = []
    if find_substring_locations('a', 1) != {'a': [0]}:
        errors.append('does\'t work with 1 letter and k=1')
    if find_substring_locations('aAa', 1) != {'a': [0, 2], 'A': [1]}:
        errors.append(
            'does\'t work if k = 1')
    if find_substring_locations('ABCDe', 5) != {'ABCDe': [0]}:
        errors.append('does\'t work if k is the length of the string')
    if find_substring_locations('ATATTAZ', 2) != {'AT': [0, 2], 'TA': [1, 4], 'TT': [3], 'AZ': [5]}:
        errors.append(
            'does\'t work with string=\'ATATTAZ\' and k=2')
    if len(errors) == 0:
        print('question 3 passed the tests')
    else:
        print('question 3 failed with the following errors:', errors)


def check_question_4():
    errors = []
    list1 = [('tom', 'python'), ('tom', 'math')]
    list2 = [('TOM', 'python'), ('tom', 'math')]
    list3 = [('tom', 'pyThoN'), ('tom', 'Math')]
    list4 = [('tom', 'python'), ('oxana', 'math')]
    result1 = {'tom': ['python', 'math']}
    result2 = {'tom': ['math', 'python']}
    result3 = {'tom': ['python'], 'oxana': ['math']}
    if courses_per_student(list1.copy()) != result1 and courses_per_student(list1.copy()) != result2:
        errors.append('does\'t combine courses by name')
    if courses_per_student(list2.copy()) != result1 and courses_per_student(list2.copy()) != result2:
        errors.append(
            'does\'t work when the name isn\'t all in lower case')
    if courses_per_student(list3.copy()) != result1 and courses_per_student(list3.copy()) != result2:
        errors.append(
            'does\'t work when the course isn\'t all in lower case')
    if courses_per_student(list4.copy()) != result3:
        errors.append(
            'does\'t work with multiple students')
    if len(errors) == 0:
        print('question 4 passed the tests')
    else:
        print('question 4 failed with the following errors:', errors)


def check_question_5():
    errors = []
    dict1 = {'tom': ['python']}
    dict2 = {'tom': ['python'], 'oxana': ['python', 'math']}
    if num_courses_per_student(dict1.copy()) != None:
        errors.append('the function isn\'t supposed to return a value')
    num_courses_per_student(dict1)
    if dict1 != {'tom': 1}:
        errors.append('doesn\'t update the original dictionary')
    num_courses_per_student(dict2)
    if dict2 != {'tom': 1, 'oxana': 2}:
        errors.append('doesn\'t work with multiple students')
    if len(errors) == 0:
        print('question 5 passed the tests')
    else:
        print('question 5 failed with the following errors:', errors)


check_question_1()
check_question_2()
check_question_3()
check_question_4()
check_question_5()
