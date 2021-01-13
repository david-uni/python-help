''' Exercise #10. Python for Engineers.'''

import numpy as np
import pandas as pd
import imageio
import matplotlib.pyplot as plt


#########################################
# Question 1 helper functions - do not delete
# this comment or change these functions
#########################################

#helper1----------------------------------------------------------------------
def np_array_to_ascii(darr):
    return ''.join([chr(item) for item in darr])


#helper2----------------------------------------------------------------------
def ascii_to_np_array(s):
    return np.frombuffer(s.encode(), dtype=np.uint8)


#########################################
# Question 1 - do not delete this comment
#########################################


#1----------------------------------------------------------------------------
def arr_dist(a1, a2):
    pass


#2----------------------------------------------------------------------------
def find_best_place(im, np_msg):
    pass

#3----------------------------------------------------------------------------
def create_image_with_msg(im, img_idx, np_msg):
    pass


#4----------------------------------------------------------------------------
def put_message(im, msg):
    pass


#5----------------------------------------------------------------------------
def get_message(im):
    pass


##############################################################################
##############################################################################


#########################################
# Question 2 - do not delete this comment
#########################################

#A----------------------------------------------------------------------------
def read_missions_file(file_name):
    pass


#B----------------------------------------------------------------------------
def add_daily_gain_col(bounties):
    pass


#C----------------------------------------------------------------------------
def sum_rewards(bounties):
    pass


#D----------------------------------------------------------------------------
def find_best_kingdom(bounties):
    pass


#E----------------------------------------------------------------------------
def find_best_duration(bounties):
    pass


#########################################
# A test for Question 1 - do not delete this comment 
#########################################


def question_A_test():
    msg1 = 'Hello, NUMPY!'
    orig_file_name = 'parrot.png'

    im1 = imageio.imread(orig_file_name)
    im2 = put_message(im1, msg1)

    plot_image = np.concatenate((im1, im2), axis=1)

    plt.figure()
    plt.imshow(plot_image, cmap=plt.cm.gray)
    plt.show()

    msg2 = get_message(im2)
    return msg2

#########################
# main code - do not delete this comment
# Add test cases below
#########################
if __name__ == "__main__":
    # ****write test cases only here****
	
    # Uncomment the following test after implementing Question 1
    #assert(question_A_test() == "Hello, NUMPY!")
    
    pass
