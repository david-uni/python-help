import matplotlib.pyplot as plt
import numpy as np
import imageio

def squeeze_image(im, factor):
    new_rows = im.shape[0]
    new_cols = im.shape[1] // factor
    new_mat = np.zeros((new_rows, new_cols))

    for c in range(new_cols):
        from_col = c*factor
        to_col = (c+1)*factor
        new_mat[:,c] = im[:,from_col:to_col].mean(axis=1)

    return new_mat

im = imageio.imread("puppy1.jpg")
im = squeeze_image(im, 2)
plt.figure()
plt.imshow(im, cmap=plt.cm.gray)
plt.show()