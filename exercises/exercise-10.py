# 29/12/2020 exercise 10
import numpy as np  # importing the numpy library with the alias 'np'
import matplotlib.pyplot as plt
import imageio as io


# creates an numpy array with zeros as values and the given dimensions (5 * 3)
a = np.zeros((5, 3))
a.ndim  # returns the dimensions of the first row in the array
a.size  # returns the number of values in the array
np.array([[1, 2, 3], [4, 5, 6]])  # creates an numpy array from the given lists
# check # np.array(10)  # creates an numpy array with 1 dimesion and the given length (10)
# creates an numpy array with the dimensions (5*5) conaining random values of type float
np.random.random((5, 5))
# creates an numpy array with the dimensions (5*5) conaining random values between -10 an 10 of type int
np.random.randint(-10, 10, (5, 5))


# masking
m = np.random.randint(-5, 5, (4, 9))
# return an array with the same shame of m, but with the condition result (boolean) instead of the original value
m > 0
m[m > 0]  # an array of 1 dimesion with all the values in m where the masking value is True
m[m > -3 & m < 3]  # combine masks

# slicing
a = np.random.random((10, 10))
a[0, :]  # slice the first row (only the first the rows and all the columns)
# slice the last column (all the rows and and only the last the columns)
a[:, -1]
a[:, :]  # slice the entire array (all the rows and all the columns)
a[::2, ::3]  # slice every 2nd row and every 3rd column
a[[2, 1, 3, 2], :]  # get the selected rows (can contain duplicates)


# image processing
# returns an numpy array with the pixel values of the given image
im = io.imread('file_path.jpg')
height, width = 100, 100
# creates an image matrix with the given dimensions (100* 100)
im = np.zeros((height, width), dtype=np, uint8)
np.uint8(100) + np.uint8(288)  # = np.uint(132)  === (100 + 288) % 256
a = np.array([[1, 2, 3], [4, 5, 6]])
a = np.array([[7, 8, 9], [10, 11, 12]])
np.vstack((a, b))  # vertical stack
np.hstack((a, b))  # horizontal stack
a.T  # returns a transposed matrix
np.min(a)  # returns the minimal value
np.max(a)  # returns the maximal value
np.mean(a)  # returns the average value
np.median(a)  # returns the median value


# binary segmentation
im = io.imread('Koala.jpg')
im.shape  # returns a tuple with the shape of the image (rows, columns)

plt.figure()  # creates a blank canvas
plt.imshow((im, cmap=plt.cm.gray))  # set the canvas wto be the image

trashold = 133
# will create a binary matrix of the image (since False  = 0, and True = 1)
binary_image = (im > trashold) * 255
plt.imshow((binary_image, cmap=plt.cm.gray))

plt.show()  # show the image on the screen
# all the code after this show line will execute only after closing the images
