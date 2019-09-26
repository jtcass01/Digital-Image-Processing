import cv2
import sys
import numpy as np
import matplotlib.pyplot as plt
from FileManager import FileManager

class ImageAnalysis():
    @staticmethod
    def calculate_bit_planes(image, gray_scale=True, bits_per_pixel=8):
        bit_planes = None

        # If the image is grayscale...
        if gray_scale:
            # Retrieve the image shape
            rows, columns = image.shape
            # Create bit planes of all zeros
            bit_planes = np.zeros((rows, columns, bits_per_pixel))

            # Update bit plane values by iterating over pixels
            for row_index, row in enumerate(image):
                for column_index, pixel in enumerate(row):
                    for bit_plane_index, bit_plane in enumerate(bit_planes):
                        bit_plane[row_index, column_index] = (pixel & 2**bit_plane_index) >> bit_plane_index

        # Retrun produce bit planes
        return bit_planes

def display_bit_planes(bit_planes):
    number_of_rows, number_of_columns, number_of_bit_planes = bit_planes.shape

    for bit_plane_index in range(number_of_bit_planes):
        print("bit plane {}".format(bit_plane_index), bit_planes[bit_plane_index])
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
