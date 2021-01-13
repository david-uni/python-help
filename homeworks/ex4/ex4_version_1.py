''' Exercise #4. Python for Engineers.'''


#########################################
# Question 1 - do not delete this comment
#########################################
def most_popular_character(my_string):
    chars = {char: my_string.count(char) for char in my_string}
    most_appearances = chars[max(chars, key=chars.get)]
    return min([char for char, count in chars.items() if count == most_appearances])


#########################################
# Question 2 - do not delete this comment
#########################################
def diff_sparse_matrices(lst):
    main_dict = lst[0].copy()
    for current_dict in lst[1:]:
        for key, val in current_dict.items():
            main_dict[key] = main_dict.get(key, 0) - val
            if not main_dict[key]:
                main_dict.pop(key)
    return main_dict


#########################################
# Question 3 - do not delete this comment
#########################################
def find_substring_locations(s, k):
    strings_dict = {}
    for i in range(len(s) - k + 1):
        sub_str = s[i:i + k]
        strings_dict[sub_str] = strings_dict.get(sub_str, []) + [i]
    return strings_dict


#########################################
# Question 4 - do not delete this comment
#########################################
def courses_per_student(tuples_lst):
    students = {}
    for student, course in tuples_lst:
        students[student.lower()] = students.get(
            student.lower(), []) + [course.lower()]
    return students


def num_courses_per_student(stud_dict):
    for student in stud_dict:
        stud_dict[student] = len(stud_dict[student])


#########################
# main code - do not delete this comment
# Tests have been added for your convenience.
# You can add more tests below.
#########################


if __name__ == '__main__':  # Do not delete this line!
    # Q1
    print(most_popular_character('aabbAA') == 'A')

    # Q2
    print(diff_sparse_matrices([{(1, 3): 2, (2, 7): 1}, {(1, 3): 6}]) == {
          (1, 3): -4, (2, 7): 1})

    # Q3
    print(find_substring_locations('TTAATTAGGGGCGC', 2) == {'TT': [0, 4], 'TA': [
          1, 5], 'AA': [2], 'AT': [3], 'AG': [6], 'GG': [7, 8, 9], 'GC': [10, 12], 'CG': [11]})

    # Q4
    stud_dict = courses_per_student([('Tom', 'Math'), ('Oxana', 'Chemistry'), (
        'Scoobydoo', 'python'), ('Tom', 'pYthon'), ('Oxana', 'biology')])

    print(stud_dict == {'tom': ['math', 'python'], 'oxana': [
          'chemistry', 'biology'], 'scoobydoo': ['python']})

    num_courses_per_student(stud_dict)
    print(stud_dict == {'tom': 2, 'oxana': 2, 'scoobydoo': 1})


# ============================== END OF FILE =================================
