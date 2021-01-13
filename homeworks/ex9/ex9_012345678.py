''' Exercise #9. Python for Engineers.'''

import numpy as np
import matplotlib.pyplot as plt


#########################################
# Question 1 - do not delete this comment
#########################################

class Roman():
    
    def get_int_from_roman(self):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        roman_string = self.roman_value.strip('-')
        int_val = 0
        for counter in range(len(roman_string)):
            if counter > 0 and rom_val[roman_string[counter]] > rom_val[roman_string[counter - 1]]:
                int_val += rom_val[roman_string[counter]] - 2 * rom_val[roman_string[counter - 1]]
            else:
                int_val += rom_val[roman_string[counter]]
        int_val = -int_val if self.is_neg else int_val
        return int_val
    
    def get_roman_from_int(self):
        num = self.int_value if not self.is_neg else -self.int_value
        roman_num = '' if not self.is_neg else '-'
        counter = 0
        
        roman_char = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        int_vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        
        while num > 0:
            for _ in range(num // int_vals[counter]):
                roman_num += roman_char[counter]
                num -= int_vals[counter]
            counter += 1
        return roman_num
    
    def __init__(self, input_value):
        pass
    
    
    def __str__(self):
        pass


    def __repr__(self):
        pass


    def __neg__(self):
        pass


    def __add__(self, other):
        pass


    def __lt__(self, other):
        pass
    
    
    def __gt__(self, other):
        pass
    

    def __floordiv__(self, other):
        pass



#########################################
# Question 2 - do not delete this comment
#########################################

def load_training_data(filename):
    pass


def get_highest_weight_loss_trainee(data_dict):
    pass


def get_diff_data(data_dict):
    pass


def get_highest_loss_month(data_dict):
    pass


def get_relative_diff_table(data_dict):
    pass



#########################################
# Question 3 - do not delete this comment
#########################################

def compute_entropy(img):
    pass


def nearest_enlarge(img, a):
    pass



if __name__ == '__main__':
    print(Roman(2))
    print(repr(Roman(2)))
    print(-Roman("IV"))
    r = Roman(2) + 3
    print(repr(r))

    
