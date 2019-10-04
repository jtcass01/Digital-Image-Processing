import numpy as np
import matplotlib.pyplot as plt
import imageio
import os
import sys
import cv2
from scipy.stats import entropy

class ImageStatistics(object):
    def __init__(self, image, bits_per_pixel=8):
        self.image = image
        self.resolution = ImageStatistics.calculate_resolution(image, bits_per_pixel)
        self.gray_levels = 2**bits_per_pixel
        self.histogram = ImageStatistics.calculate_histogram(image, bits_per_pixel)
        self.probability_density_function = ImageStatistics.calculate_pdf(image, bits_per_pixel)
        self.mean = ImageStatistics.calculate_mean(image)
        self.variance = ImageStatistics.calculate_variance(image)
        self.std_dev = ImageStatistics.calculate_std_dev(image)
        self.entropy = ImageStatistics.calculate_entropy(image)

    def __str__(self):
        stringRepresentation = "Resolution: " + str(self.resolution) + "\n"
        stringRepresentation += "Number Gray Levels (L): " + str(self.gray_levels) + "\n"
        stringRepresentation += "Histogram Representation H(k): " + str(self.histogram) + "\n"
        stringRepresentation += "Probability Density Function P(k): " + str(self.probability_density_function) + "\n"
        stringRepresentation += "Mean: " + str(self.mean) + "\n"
        stringRepresentation += "Variance: " + str(self.variance) + "\n"
        stringRepresentation += "Standard Deviance: " + str(self.std_dev) + "\n"
        stringRepresentation += "Entropy: " + str(self.entropy) + "\n"
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
    def calculate_resolution(image, bits_per_pixel=8):
        row_count, column_count = image.shape
        return row_count * column_count * bits_per_pixel

    @staticmethod
    def calculate_histogram(image, bits_per_pixel=8):
        histogram = np.zeros((2**bits_per_pixel, 1))

        for row in image:
            for pixel in row:
                histogram[int(pixel), 0] += 1

        return histogram

    @staticmethod
    def calculate_pdf(image, bits_per_pixel=8):
        row_count, column_count = image.shape
        N = row_count*column_count
        hist = ImageStatistics.calculate_histogram(image, bits_per_pixel)
        return hist / N

    @staticmethod
    def normalize_image(image, bits_per_pixel=8):
        return image / (2**bits_per_pixel)

    @staticmethod
    def calculate_mean(image, bits_per_pixel=8):
        return np.mean(image)

    @staticmethod
    def calculate_variance(image, bits_per_pixel=8):
        return np.var(image)

    @staticmethod
    def calculate_std_dev(image, bits_per_pixel=8):
        return np.std(image)

    @staticmethod
    def calculate_entropy(image, base=2):
        _, counts = np.unique(image, return_counts=True)
        return entropy(counts, base=base)


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
