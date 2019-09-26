import matplotlib.pyplot as plt

class ImageDisplay():
    @staticmethod
    def display_image(image, gray_scale=True):
        if gray_scale:
            # Display image:
            plt.imshow(image, cmap='gray')
            plt.show()
        else:
            # Display image:
            plt.imshow(image)
            plt.show()

    def display_bit_planes(bit_planes, gray_scale=True):
        if gray_scale:
            for bit_plane in bit_planes:
                ImageDisplay.display_image(bit_plane, gray_scale)
