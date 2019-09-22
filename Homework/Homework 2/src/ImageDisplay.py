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
