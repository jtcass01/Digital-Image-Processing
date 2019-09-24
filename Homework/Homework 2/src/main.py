"""
3.5
Do the following:
(a) Purpose a method for extracting the bit planes of an image based on
converting the value of its pixels to binary.
(b) Find all the bit planes o the following 4-bit image:
        0  1  8  6
        2  2  1  1
        1  15 14 12
        3  6  9  10

3.7
Obtain the unnormalized and the normalized histograms of the following 8-bit,
MxN image.  Give your histogram either in a table or a graph, labeling clearly
the value and location of each histogram component in terms of M and N.
Double-check your answer by making sure that the histogram components add to the
correct value.

3.14
An image with intensities in the range [0, 1] has the pdf, p(r), shown in the
following figure.  It is desired to transform the intensity levels of this image
so that they will have the specified p(z) shown in the figure.  Assume continuous
quantities, and find the transform that will accomplish this.

3.19
The image in Fig 3.30(c) is of size 1000 x 683 pixels.  Its histogram, labeled
"b" in Fig. 3.30(b), was intended to be uniform, but the result is not quite
uniform (observe the shape change at the low end of the intensity scale).
How do you explain this?
"""

import numpy as np

from ImageAnalysis import ImageAnalysis, display_bit_planes
from ImageDisplay import ImageDisplay

def three_five():
    """
    3.5
    Do the following:
    (a) Purpose a method for extracting the bit planes of an image based on
    converting the value of its pixels to binary.
    (b) Find all the bit planes o the following 4-bit image:
            0  1  8  6
            2  2  1  1
            1  15 14 12
            3  6  9  10
    """
    four_bit_image = np.array([[0,1,8,6], [2,2,1,1], [1, 15, 14, 12], [3, 6, 9, 10]])

    ImageDisplay.display_image(four_bit_image)

    bit_planes = ImageAnalysis.calculate_bit_planes(four_bit_image, bits_per_pixel=4)

    display_bit_planes(bit_planes * 256)


def three_seven():
    """
    3.7
    Obtain the unnormalized and the normalized histograms of the following 8-bit,
    MxN image.  Give your histogram either in a table or a graph, labeling clearly
    the value and location of each histogram component in terms of M and N.
    Double-check your answer by making sure that the histogram components add to the
    correct value.
    """
    figure_image = np.array([
    [240, 240, 240,  16,  16,  16,  32,  32,  32,  32,  32,  32,  32],
    [240, 240, 240,  16,  16,  16, 228,  32,  32,  32,  32,  32, 255],
    [240, 240, 240,  16,  16,  16, 228, 228,  32,  32,  32, 255, 255],
    [240, 240, 240,  16,  16,  16, 228, 228, 228,  32, 255, 255, 255],
    [240, 240, 240,  16,  16,  16, 228, 228, 228,   0, 255, 255, 255],
    [240, 240, 240,  16,  16,  16, 228, 228,   0,   0,   0, 255, 255],
    [240, 240, 240,  16,  16,  16, 228,   0,   0,   0,   0,   0, 255],
    [240, 240, 240,  16,  16,  16,   0,   0,   0,   0,   0,   0,   0],
    [127, 127, 127, 191, 191, 191,   0,   0,   0,   0,   0,   0,   0],
    [127, 127, 127, 191, 191, 191,   0,   0,   0,   0,   0,   0,   0],
    [127, 127, 127, 191, 191, 191,   0,   0,   0,   0,   0,   0,   0],
    ])

    normalized_image = ImageStatistics.normalize_image(figure_image, 8)

    histogram = ImageStatistics.calculate_histogram(figure_image)
    normalized_histogram = ImageStatistics.calculate_histogram(normalized_image)

    plt.plot(histogram, label="unnormalized histogram")
    plt.legend()
    plt.show()

    plt.plot(normalized_histogram, label="normalized histogram")
    plt.legend()
    plt.show()


def three_fourteen():
    """
    3.14
    An image with intensities in the range [0, 1] has the pdf, p(r), shown in the
    following figure.  It is desired to transform the intensity levels of this image
    so that they will have the specified p(z) shown in the figure.  Assume continuous
    quantities, and find the transform that will accomplish this.
    """
    print("Transform function in the form of z = L - 1 - r where L is the number of intensity levels in the image.")


def three_nineteen():
    """
    3.19
    The image in Fig 3.30(c) is of size 1000 x 683 pixels.  Its histogram, labeled
    "b" in Fig. 3.30(b), was intended to be uniform, but the result is not quite
    uniform (observe the shape change at the low end of the intensity scale).
    How do you explain this?
    """
    # This is because of the large number of pixels within the low end of the intensity scale.
    # Histogram Equalization utilizes the cumulative density function of the entire image
    # which is dependent on pixel densities.
    pass


def menu():
    print("===== Homework 2 Menu =====")
    print("1 ) 3.5")
    print("2 ) 3.7")
    print("3 ) 3.14")
    print("4 ) 3.19")
    print("0 ) quit")

    return input("Input Problem: ")

if __name__ == "__main__":
    response = ""

    while response != "quit" and response != "q" and response != "0":
        response = menu()

        if response == "1":
            three_five()
        elif response == "2":
            three_seven()
        elif response == "3":
            three_fourteen()
        elif response == "4":
            three_nineteen()
