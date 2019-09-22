import cv2
import sys
import numpy as np
import matplotlib.pyplot as plt
from FileManager import FileManager

def display_image(image):
    # Display image:
    plt.imshow(image, cmap='gray')
    plt.show()

class ImageAnalysis():
    @staticmethod
    def calculate_bit_planes(image, gray_scale=True, bits_per_pixel=8):
        bit_planes = None

        if gray_scale:
            rows, columns = image.shape
            bit_planes = np.ones((rows, columns, bits_per_pixel))

        for row_index, row in enumerate(image):
            for column_index, pixel in enumerate(row):
                for bit_plane_index in range(bits_per_pixel):
                    bit_planes[row_index, column_index, bit_plane_index] = (pixel & 2**bit_plane_index) >> bit_plane_index

        return bit_planes * 256

def display_bit_planes(bit_planes):
    number_of_rows, number_of_columns, number_of_bit_planes = bit_planes.shape

    for bit_plane_index in range(number_of_bit_planes):
        print("bit plane {}".format(bit_plane_index))
        display_image(bit_planes[:, :, bit_plane_index])


if __name__ == "__main__":
    args = sys.argv

    if(len(args) != 2):
        print("Command Line Arguments should follow the format:")
        print("python ImageAnalysis.py [relative_image_path]")
    else:
        image_path = args[1]

        image = FileManager.read_grayscale_image(image_path)

        print("Displaying image...")
        display_image(image)

        bit_planes = ImageAnalysis.calculate_bit_planes(image)
        display_bit_planes(bit_planes)
