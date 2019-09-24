import numpy as np
import matplotlib.pyplot as plt
import imageio
import os
import sys
import cv2

class ImageStatistics(object):
    def __init__(self, image, bits_per_pixel):
        self.image = image
        self.resolution = ImageStatistics.calculate_resolution(image, bits_per_pixel)
        self.gray_levels = 2**bits_per_pixel
        self.histogram = ImageStatistics.calculate_histogram(image, bits_per_pixel)
        self.probability_density_function = ImageStatistics.calculate_pdf(image, bits_per_pixel)

    def __str__(self):
        stringRepresentation = "Resolution: " + str(self.resolution) + "\n"
        stringRepresentation += "Number Gray Levels (L): " + str(self.gray_levels) + "\n"
        stringRepresentation += "Histogram Representation H(k): " + str(self.histogram) + "\n"
        stringRepresentation += "Probability Density Function P(k): " + str(self.probability_density_function) + "\n"
        return stringRepresentation

    def show_histogram(self):
        plt.plot(self.histogram, label="histogram")
        plt.legend()
        plt.show()

    def show_pdf(self):
        plt.plot(self.probability_density_function, label="probability_density_function")
        plt.legend()
        plt.show()

    @staticmethod
    def calculate_resolution(image, bits_per_pixel):
        row_count, column_count = image.shape
        return row_count * column_count * bits_per_pixel

    @staticmethod
    def calculate_histogram(image, bits_per_pixel):
        columns = 2**bits_per_pixel
        return cv2.calcHist([image], [0], None, [columns], [0, columns])

    @staticmethod
    def calculate_pdf(image, bits_per_pixel):
        row_count, column_count = image.shape
        N = row_count*column_count
        hist = ImageStatistics.calculate_histogram(image, bits_per_pixel)
        return hist / N

    @staticmethod
    def normalize_image(image, bits_per_pixel=8):
        return image / (2**bits_per_pixel)


if __name__ == "__main__":
    args = sys.argv

    if(len(args) != 2):
        print("Command Line Arguments should follow the format:")
        print("python ImageStatistics.py [relative_image_path]")
    else:
        image_path = sys.argv[1]

        # Read image:
        image = cv2.imread(image_path, 0)

        print("Initial image: ")
        print(image, image.shape)

        image_stats = ImageStatistics(image, 8)
        print(image_stats)
        image_stats.show_histogram()
        image_stats.show_pdf()

        # Display image:
        plt.imshow(image, cmap='gray')
        plt.show()
