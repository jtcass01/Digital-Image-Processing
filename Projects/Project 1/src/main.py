'''
The purpose of this project is to practice the following adaptive enhancement algorithms:
1.	Histogram Equalization Applied to neighborhood sub-images with size = 5 x 5
2.	Statistical Enhancement using neighborhood sub-images with size = 5 x 5
Apply the two methods to enhance the attached image Fig0326.tif.
Algorithm #1: the transformation of the intensity levels; g(x,y) =T[f(x,y)]will be adapted according to the cumulative distribution of the 5 x 5 pixel neighbors.
Algorithm #2: the transformation of the intensity levels is the following equation:
g(x,y) = E*f(x,y); if [mean(x,y) < k0*global mean] and k1*global std < std(x,y) < k2*global std]
             = f(x,y);      otherwise

Where k0, k1, k2 are constants < 1, and E is a constant >  1. For example here are possible values k0 = 0.4, k1=0.02, k2 = 0.4, and E = 4.
'''
import sys
import cv2
from copy import deepcopy
import numpy as np
import matplotlib.pyplot as plt
from skimage import exposure
from scipy.stats import norm

from FileManager import FileManager

def display_image(image):
    # Display image:
    plt.imshow(image, cmap='gray')
    plt.show()

def adaptive_histogram_equalization(image, neighborhood_shape = (5, 5)):
    g = np.zeros(image.shape)

    for row_index, row in enumerate(image):
        for column_index, pixel in enumerate(row):
            relevant_neighborhood = get_neighborhood(image, (row_index, column_index), neighborhood_shape)
            image_cdf, bins = exposure.cumulative_distribution(relevant_neighborhood, 256)
            image_cdf *= 255
            g[row_index, column_index] = image_cdf[pixel]

    return g

def adaptive_statistical_enhancement(image, neighborhood_shape = (5,5), k0=0.4, k1=0.02, k2=0.4, E=4):
    assert 0 <= k0 <= 1, "k0 must be a constant < 1"
    assert 0 <= k1 <= 1, "k1 must be a constant < 1"
    assert 0 <= k2 <= 1, "k2 must be a constant < 1"
    assert 1 <= E, "E must be a constant > 1"
    g = np.zeros(image.shape)

    global_mean = np.mean(image)
    global_std = np.std(image)

    for row_index, row in enumerate(image):
        for column_index, pixel in enumerate(row):
            relevant_neighborhood = get_neighborhood(image, (row_index, column_index), neighborhood_shape)
            neighborhood_mean = np.mean(relevant_neighborhood)
            neighborhood_std = np.std(relevant_neighborhood)

            if neighborhood_mean <= k0 * global_mean and k1*global_std <= neighborhood_std <= k2*global_std:
                g[row_index, column_index] = E * pixel
            else:
                g[row_index, column_index] = pixel

    return g

def get_neighborhood(image, pixel_location, neighborhood_shape):
    # Retrieve data from inputs
    rows = len(image[:, 0])
    columns = len(image[0, :])
    pixel_row, pixel_column = pixel_location

    # Initialize variables dependent on if statements
    left_pad = 0
    right_pad = 0
    top_pad = 0
    bottom_pad = 0

    # Compute image_frame WRT neighborhood_shape and pixel location
    mid_to_right = neighborhood_shape[0] // 2
    mid_to_top = neighborhood_shape[1] // 2
    y_start = int(pixel_row-mid_to_right-1)
    if y_start < 0:
        top_pad = y_start * -1 -1
        y_start = 0

    y_stop = int(pixel_row+mid_to_right+1)
    if y_stop > columns - 1:
        bottom_pad = -(y_stop - columns - 1)
        y_stop = columns

    x_start = int(pixel_column-mid_to_top-1)
    if x_start < 0:
        left_pad = x_start * -1 -1
        x_start = 0

    x_stop = int(pixel_column+mid_to_top+1)
    if x_stop > rows:
        right_pad = x_stop - rows - 1
        x_stop = rows

    # Retrieve relevant frame from image.  Initailize array of zeros to store result.
    frame = deepcopy(image[y_start:y_stop, x_start:x_stop])
    result = np.zeros(shape=neighborhood_shape)

    # Transfer image frame to resultant array taking into account the amount of padding.
    for row_index, row in enumerate(frame):
        for column_index, pixel in enumerate(row):
            if column_index+left_pad < (neighborhood_shape[1] - right_pad) and row_index + top_pad < (neighborhood_shape[0] - bottom_pad):
                result[row_index+top_pad, column_index+left_pad] = frame[row_index, column_index]

    return result

if __name__ == "__main__":
    args = sys.argv

    if(len(args) != 2):
        print("Command Line Arguments should follow the format:")
        print("python main.py [relative_image_path]")
    else:
        image_path = args[1]

        image = FileManager.read_grayscale_image(image_path)

        print("Displaying image...")
        display_image(image)

        equalized_image = cv2.equalizeHist(image)

        ahe_image = adaptive_histogram_equalization(image)

        print("Displaying ahe_image...")
        display_image(ahe_image)

        ase_image = adaptive_statistical_enhancement(image)

        print("Displaying ase_image...")
        display_image(ase_image)

        # stack images side by side
        res = np.hstack((image, equalized_image, ahe_image, ase_image))

        display_image(res)
