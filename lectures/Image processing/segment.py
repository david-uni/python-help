import matplotlib.pyplot as plt
import numpy as np
import imageio

def segment_image(im_mat, th):
    new_mat = np.zeros(im_mat.shape, dtype=np.uint8)
    mask = im_mat >= th
    print(mask)
    new_mat[im_mat >= th] = 255
    return new_mat

im = imageio.imread("puppy1.jpg")
new_image = segment_image(im, 150)
plt.figure()
plt.imshow(new_image, cmap=plt.cm.gray)
plt.show()
