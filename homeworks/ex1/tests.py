###########################################################################
##########################      DISCLAIMER      ##########################
###########################################################################

# this tests aren't official test,
# so you should take any success or error
# with the benefit of the doubt

###########################################################################
##########################      DISCLAIMER      ###########################
###########################################################################

###########################################################################
##########################      INSTRUCTIONS      ##########################
###########################################################################

# copy this file to the same directory where you save your file with the solution
# at the end of this file, you will find a variable named 'file_name', change its's value to your file name (the name of the file containing the solution)
# run this file and watch the output in the shell

###########################################################################
##########################      INSTRUCTIONS      ###########################
###########################################################################

import sys
import os
import platform
import subprocess
from uuid import uuid4

WHITE = '\033[0m'
RED = '\033[31m'
GREEN = '\033[32m'
UNDERLINE = '\033[4m'


def color_in_red(text): return RED + text + WHITE
def color_in_green(text): return GREEN + text + WHITE
def underline_it(text): return UNDERLINE + text + WHITE


def get_code(file_name):
    with open(file_name) as file:
        return file.readlines()


def do_file_exist(file_name):
    return os.path.exists(file_name)


def create_new_file(content):
    new_file_name = f'{uuid4()}.py'
    while do_file_exist(new_file_name):
        new_file_name = f'{uuid4()}.py'

    with open(new_file_name, 'w') as file:
        file.writelines(content)

    return new_file_name


def update_variables_values(question_number, lines, variables):
    values_area_start_text = ['#########################################\n',
                              f'# Question {question_number} - do not delete this comment\n', '#########################################\n']
    values_area_end_text = f'# Write the rest of the code for question {question_number} below here.'
    in_values_area = False
    start_text_count = 0
    for index, line in enumerate(lines):
        if (not in_values_area) and line == values_area_start_text[start_text_count]:
            start_text_count += 1
            if start_text_count == len(values_area_start_text) - 1:
                in_values_area = True
        elif in_values_area and line == values_area_end_text:
            in_values_area = False
            return
        else:
            start_text_count = 0

        if in_values_area:
            for variable in variables:
                variables_assignment_starts = [f'{variable} =', f'{variable}=']
                if any([line.startswith(text) for text in variables_assignment_starts]):
                    new_value = f'"{variables[variable]}"' if isinstance(
                        variables[variable], str) else variables[variable]
                    lines[index] = f'{variable} = {new_value}\n'


def erase_new_file(new_file_name):
    os.remove(new_file_name)


def run_file_and_get_output(file_name):
    p = subprocess.run([sys.executable, file_name],
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return p.stdout.decode()


def get_platform_break_line_characters():
    platform_name = platform.system()
    if platform_name == 'Windows':
        return '\r\n'

    if platform_name not in ['Linux', 'Darwin']:
        print(color_in_red('***Warning - you are using an unsupported operating system,\nthis can break the tests, so in case of failed tests read the full error message**'))

    return '\n'


def print_decorated_line(text, color=None):
    line_length = len(text)
    decorator = '#' * line_length
    decorated_text = '\n' + decorator + '\n' + text + '\n' + decorator
    if color == 'RED':
        decorated_text = color_in_red(decorated_text)
    elif color == 'GREEN':
        decorated_text = color_in_green(decorated_text)

    print(decorated_text)


class SoftAssert():
    def __init__(self, question_name=None):
        self.errors = []
        self.question_name = (question_name + ' ') if question_name else ''

    def assert_(self, condition, error_message):
        if not condition:
            self.errors.append(error_message)

    def assert_equals(self, got, expected, error_message):
        if got != expected:
            self.errors.append(
                f'{error_message.rstrip()}\n\t{underline_it("Expected:")} {expected.rstrip()}\n\t{underline_it("Got     :")} {got.rstrip()}')

    def assert_all(self):
        if not self.errors:
            print(color_in_green(f'{self.question_name}passed the tests'))
            return True

        print(self.__enumerate_errors())
        return False

    def __enumerate_errors(self):
        errors = color_in_red(
            f'{self.question_name}failed with the following errors:\n')
        for index, error in enumerate(self.errors):
            errors += f'{index + 1}. {error}\n'
        return errors

############################################################################################################################


def test_question_structure(question_num, code, cases, output_start_line, output_end_line):
    soft_assert = SoftAssert(f'Question {question_num}')
    for variables, expected in cases:
        update_variables_values(question_num, code, variables)
        temp_file = create_new_file(code)
        output = run_file_and_get_output(temp_file)
        erase_new_file(temp_file)
        relevant_output = ''.join(
            [line + '\n' for line in output.split('\n')][output_start_line:output_end_line])
        soft_assert.assert_equals(relevant_output, expected,
                                  f'printed the wrong output for the following input: {variables}')
    return soft_assert.assert_all()


def test_question_1(code, line_break):
    cases = [({'S': 220.0, 'AB': 20.0, 'BC': 10.0, 'AD': 15.0,
               'DC': 35.0}, f'Diameter is: 80.0{line_break}Midsegment is: 27.5{line_break}Height is: 8.0{line_break}'), ({'S': 236.2, 'AB': 46.0, 'BC': 9.8, 'AD': 13.99,
                                                                                                                          'DC': 43.0}, f'Diameter is: 112.78999999999999{line_break}Midsegment is: 44.5{line_break}Height is: 5.307865168539325{line_break}'), ({'S': 325.0, 'AB': 51.1, 'BC': 11.1, 'AD': 12.0,
                                                                                                                                                                                                                                                                 'DC': 26.7}, f'Diameter is: 100.9{line_break}Midsegment is: 38.9{line_break}Height is: 8.354755784061696{line_break}')]
    return test_question_structure(1, code, cases, 0, 0 + 3)


def test_question_2(code, line_break):
    cases = [({'my_name': 'oxana'}, f'Hello Oxana!{line_break}'), ({'my_name': 'OXANA'}, f'Hello Oxana!{line_break}'), ({
        'my_name': 'oxAnA'}, f'Hello Oxana!{line_break}'), ({'my_name': 'mIchaEl'}, f'Hello Michael!{line_break}')]
    return test_question_structure(2, code, cases, 3, 3 + 1)


def test_question_3(code, line_break):
    cases = [({'number': '0'}, f'I am 0 and I am divisible by 7{line_break}'), ({'number': '7'}, f'I am 7 and I am divisible by 7{line_break}'), ({
        'number': '343'}, f'I am 343 and I am divisible by 7{line_break}'), ({'number': '48'}, f'I am 48 and I am not divisible by 7{line_break}')]
    return test_question_structure(3, code, cases, 4, 4 + 1)


def test_question_4(code, line_break):
    soft_assert = SoftAssert('Question 4')
    cases = [({'text': 'tom', 'copies': 3}, f'otmotmotm{line_break}'), ({'text': 'oxana', 'copies': 3}, f'xnoaaxnoaaxnoaa{line_break}'), ({
        'text': 'oxana', 'copies': 2}, f'xnoaaxnoaa{line_break}'), ({'text': 'file', 'copies': 1}, f'iefl{line_break}')]
    return test_question_structure(4, code, cases, 5, 5 + 1)


def test_question_5(code, line_break):
    cases = [({'name': 'droLtromedloV', 'q': 4}, f'Lord Voldemort{line_break}'), ({'name': 'dessaPtseT', 'q': 6}, f'Passed Test{line_break}'), ({'name': 'droLtromedloV',
                                                                                                                                                 'q': -1}, f'Error: illegal input!{line_break}'), ({'name': 'test', 'q': 4}, f'Error: illegal input!{line_break}'), ({'name': '', 'q': 4}, f'Error: illegal input!{line_break}')]
    return test_question_structure(5, code, cases, 6, 6 + 1)


def main():
    file_name = 'ex1_012345678.py' # TODO - change the name to your code file name
    line_break_characters = get_platform_break_line_characters()
    code = get_code(file_name)
    questions = []
    questions.append(test_question_1(code, line_break_characters))
    questions.append(test_question_2(code, line_break_characters))
    questions.append(test_question_3(code, line_break_characters))
    questions.append(test_question_4(code, line_break_characters))
    questions.append(test_question_5(code, line_break_characters))
    if all(questions):
        print_decorated_line('You Passed All The Tests!!!', 'GREEN')
    else:
        print_decorated_line('You Failed At Least One Test, Try Again', 'RED')


if __name__ == '__main__':
    main()
