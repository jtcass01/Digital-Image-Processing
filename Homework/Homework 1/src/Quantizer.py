#-	(Build a quantizer) Reduce the representation of the image lenna.jpg from 8 bits per pixel to 4 bits
# per pixel using the following substitution table:
#F	G
#0-15	7
#16-31	23
#32-47	39
#... ...
#240...255	247
#-	Apply imshow to display image g
#-	Compute the average error between f and g.
#o	MSE = sigma[(f-g)^2]/size

import numpy as np
import matplotlib.pyplot as plt
import imageio
import os
import sys

def mse(array1, array2, axis=None):
    return ((array1 - array2)**2).mean(axis=axis)

class Quantizer():
    @staticmethod
    def quantize_image(image_array):
        quantized_image = np.copy(image_array)

        for row_index, row in enumerate(image_array):
            for column_index, pixel in enumerate(row):
                if pixel >= 0 and pixel < 16:
                    quantized_image[row_index, column_index] = 7
                elif pixel >= 16 and pixel < 32:
                    quantized_image[row_index, column_index] = 23
                elif pixel >= 32 and pixel < 48:
                    quantized_image[row_index, column_index] = 39
                elif pixel >= 48 and pixel < 64:
                    quantized_image[row_index, column_index] = 55
                elif pixel >= 64 and pixel < 80:
                    quantized_image[row_index, column_index] = 71
                elif pixel >= 80 and pixel < 96:
                    quantized_image[row_index, column_index] = 87
                elif pixel >= 96 and pixel < 112:
                    quantized_image[row_index, column_index] = 103
                elif pixel >= 112 and pixel < 128:
                    quantized_image[row_index, column_index] = 119
                elif pixel >= 128 and pixel < 144:
                    quantized_image[row_index, column_index] = 135
                elif pixel >= 144 and pixel < 160:
                    quantized_image[row_index, column_index] = 151
                elif pixel >= 160 and pixel < 176:
                    quantized_image[row_index, column_index] = 167
                elif pixel >= 176 and pixel < 192:
                    quantized_image[row_index, column_index] = 183
                elif pixel >= 192 and pixel < 208:
                    quantized_image[row_index, column_index] = 199
                elif pixel >= 208 and pixel < 224:
                    quantized_image[row_index, column_index] = 215
                elif pixel >= 224 and pixel < 240:
                    quantized_image[row_index, column_index] = 231
                elif pixel >= 240 and pixel < 256:
                    quantized_image[row_index, column_index] = 247

        return quantized_image

if __name__ == "__main__":
    args = sys.argv

    if(len(args) != 2):
        print("Command Line Arguments should follow the format:")
        print("python Quantizer.py [relative_image_path]")
    else:
        image_path = sys.argv[1]

        # Read image:
        image = imageio.imread(image_path)
        print("Initial image: ")
        print(image, image.shape)
        # Display image:
        plt.imshow(image, cmap='gray')
        plt.show()

        # Quantize image:
        quantized_image = Quantizer.quantize_image(image)
        print("Quantized image: ")
        print(quantized_image, quantized_image.shape)
        # Display quantized image:
        plt.imshow(image, cmap='gray')
        plt.show()

        # Calculate Mean Squared Error
        print("Mean Squared Error between intital image and quantized image = {}".format(mse(image, quantized_image)))
