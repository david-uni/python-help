''' Exercise #10., Python for Engineers.'''

import numpy as np
import pandas as pd
import imageio
import matplotlib.pyplot as plt


#########################################
# Question 1 helper functions - do not delete
# this comment or change these functions
#########################################

# helper1----------------------------------------------------------------------
def np_array_to_ascii(darr):
    return ''.join([chr(item) for item in darr])


# helper2----------------------------------------------------------------------
def ascii_to_np_array(s):
    return np.frombuffer(s.encode(), dtype=np.uint8)


#########################################
# Question 1 - do not delete this comment
#########################################

# 1----------------------------------------------------------------------------
def arr_dist(a1, a2):
    return abs(np.array(a1, dtype=np.int) - np.array(a2, dtype=np.int)).sum()


# 2----------------------------------------------------------------------------
def find_best_place(im, np_msg):
    # flat_im = im.flatten()
    # starts at the 3rd place - index 2
    # to find the original row -> (i + 2) // im.shape[1]
    # to find the original column -> (i + 2) % im.shape[1]
    index_mat = [
        list(range(3, min(256, im.shape[1]) - len(np_msg) + 1)),
        *[list(range(im.shape[1]-len(np_msg) + 1)) for i in range(min(255, im.shape[0]-1))]
    ]
    best = [None, (0, 3)]
    for row_index, row in enumerate(index_mat):
        for col_index in row:
            current_dist = arr_dist(
                np_msg, im[row_index, col_index:col_index + len(np_msg)])
            if best[0] == None or current_dist < best[0]:
                best[0], best[1] = current_dist, (row_index, col_index)
    return best[1]


# 3----------------------------------------------------------------------------
def create_image_with_msg(im, img_idx, np_msg):
    new_im = im.copy()
    new_im[0, :3] = [img_idx[0], img_idx[1], len(np_msg)]
    new_im[img_idx[0], img_idx[1]: img_idx[1] + len(np_msg)] = np_msg
    return np.array(new_im, dtype=np.uint8)


# 4----------------------------------------------------------------------------
def put_message(im, msg):
    np_msg = ascii_to_np_array(msg)
    img_idx = find_best_place(im, np_msg)
    return create_image_with_msg(im, img_idx, np_msg)


# 5----------------------------------------------------------------------------
def get_message(im):
    return np_array_to_ascii(im[im[0, 0], im[0, 1]:im[0, 1] + im[0, 2]])


##############################################################################
##############################################################################


#########################################
# Question 2 - do not delete this comment
#########################################

# A----------------------------------------------------------------------------
def read_missions_file(file_name):
    try:
        return pd.read_csv(file_name, index_col=0)
    except IOError:
        raise IOError('An IO error occurred')


# B----------------------------------------------------------------------------
def add_daily_gain_col(bounties):
    bounties['Daily gain'] = (
        bounties.Bounty - bounties.Expenses) / bounties.Duration


# C----------------------------------------------------------------------------
def sum_rewards(bounties):
    return bounties['Bounty'].sum() - bounties['Expenses'].sum()


# D----------------------------------------------------------------------------
def find_best_kingdom(bounties):
    add_daily_gain_col(bounties)
    return bounties['Daily gain'].idxmax()


# E----------------------------------------------------------------------------
def find_best_duration(bounties):
    add_daily_gain_col(bounties)
    groups = bounties.groupby(['Duration'])
    best = [None, 0]
    for name, group in groups:
        current_average = group['Daily gain'].mean()
        if best[0] == None or best[0] < current_average:
            best[:] = [current_average, name]
    return best[1]


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
