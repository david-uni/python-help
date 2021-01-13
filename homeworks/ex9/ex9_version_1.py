''' Exercise #9. Python for Engineers.'''

import numpy as np
import matplotlib.pyplot as plt
import imageio


#########################################
# Question 1 - do not delete this comment
#########################################

class Roman():

    def get_int_from_roman(self):
        rom_val = {'I': 1, 'V': 5, 'X': 10,
                   'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        roman_string = self.roman_value.strip('-')
        int_val = 0
        for counter in range(len(roman_string)):
            if counter > 0 and rom_val[roman_string[counter]] > rom_val[roman_string[counter - 1]]:
                int_val += rom_val[roman_string[counter]] - \
                    2 * rom_val[roman_string[counter - 1]]
            else:
                int_val += rom_val[roman_string[counter]]
        int_val = -int_val if self.is_neg else int_val
        return int_val

    def get_roman_from_int(self):
        num = self.int_value if not self.is_neg else -self.int_value
        roman_num = '' if not self.is_neg else '-'
        counter = 0

        roman_char = ["M", "CM", "D", "CD", "C", "XC",
                      "L", "XL", "X", "IX", "V", "IV", "I"]
        int_vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        while num > 0:
            for _ in range(num // int_vals[counter]):
                roman_num += roman_char[counter]
                num -= int_vals[counter]
            counter += 1
        return roman_num

    def __init__(self, input_value):
        if type(input_value) == int:
            self.int_value = input_value
            self.is_neg = self.int_value < 0
            self.roman_value = self.get_roman_from_int()
        else:
            self.is_neg = input_value.startswith('-')
            self.roman_value = (input_value)
            self.int_value = self.get_int_from_roman()

    def __str__(self):
        return f'The integer value is {self.int_value} and the Roman Numeral is denoted by \'{self.roman_value}\''

    def __repr__(self):
        return self.roman_value

    def __neg__(self):
        return Roman(-self.int_value)

    def __add__(self, other):
        add = Roman(self.int_value +
                    (other.int_value if isinstance(other, Roman) else other))
        if not add.int_value:
            raise ValueError('can\'t represent 0 as a roman digit')
        return add

    def __lt__(self, other):
        return self.int_value < (other.int_value if isinstance(other, Roman) else other)

    def __gt__(self, other):
        return self.int_value > (other.int_value if isinstance(other, Roman) else other)

    def __floordiv__(self, other):
        div = Roman(self.int_value //
                    (other.int_value if isinstance(other, Roman) else other))
        if not div.int_value:
            raise ValueError('can\'t represent 0 as a roman digit')
        return div


#########################################
# Question 2 - do not delete this comment
#########################################

def load_training_data(filename):
    with open(filename, 'r') as f:
        line = f.readline()
        full_data = np.array(line.strip().split(','))
        line = f.readline()
        while line:
            full_data = np.vstack((full_data, line.strip().split(',')))
            line = f.readline()
    return {
        'data': np.array(full_data[1:, 1:], dtype=float),
        'column_names': np.array(full_data[0, 1:], dtype=str),
        'row_names': np.array(full_data[1:, 0], dtype=str)
    }


def get_highest_weight_loss_trainee(data_dict):
    total_diff = data_dict['data'][:, 0] - data_dict['data'][:, -1]
    return data_dict['row_names'][np.argmax(total_diff, axis=0)]


def get_diff_data(data_dict):
    return data_dict['data'][:, 1:] - data_dict['data'][:, :-1]


def get_highest_loss_month(data_dict):
    diff_data = get_diff_data(data_dict)
    sums = diff_data.sum(axis=0)
    return data_dict['column_names'][1:][sums == sums.min()][0]


def get_relative_diff_table(data_dict):
    diff_data = get_diff_data(data_dict)
    return diff_data / data_dict['data'][:, :-1]


#########################################
# Question 3 - do not delete this comment
#########################################

def compute_entropy(img):
    im = imageio.imread(img)
    histogram = {}
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            histogram[im[i, j]] = histogram.get(im[i, j], 0) + 1
    entropy = 0
    for color, count in histogram.items():
        entropy += -(count / im.size) * np.log2(count / im.size)
    return entropy


def nearest_enlarge(img, a):
    im = imageio.imread(img)
    enlarged_im = np.zeros((int(im.shape[0]*a), int(im.shape[1]*a)))
    for i in range(enlarged_im.shape[0]):
        for j in range(enlarged_im.shape[1]):
            enlarged_im[i, j] = im[i // a, j // a]
    return enlarged_im


if __name__ == '__main__':
    print(Roman(2))
    print(repr(Roman(2)))
    print(-Roman("IV"))
    r = Roman(2) + 3
    print(repr(r))

    # data_dict = load_training_data('weight_input.csv')
    # most_weight_lost = get_highest_loss_month(data_dict)
    # diff_data = get_diff_data(data_dict)
    # largest_weight = get_highest_weight_loss_trainee(data_dict)
    # percentage = get_relative_diff_table(data_dict)
    # print(data_dict)
    # print('----------------------------------')
    # print(most_weight_lost)
    # print('----------------------------------')
    # print(diff_data)
    # print('----------------------------------')
    # print(largest_weight)
    # print('----------------------------------')
    # print(percentage)

    # entropy = compute_entropy('cameraman.tif')
    # print(f'entropy: {entropy}')

    # im = imageio.imread('cameraman.tif')
    # enlarged_im = nearest_enlarge('cameraman.tif', 2)
    # print(im.size, enlarged_im.size, enlarged_im.size / im.size)
    # plt.figure()
    # plt.imshow(enlarged_im, cmap=plt.cm.gray)
    # plt.show()
