import cv2

class FileManager():
    @staticmethod
    def read_grayscale_image(image_path):
        return cv2.imread(image_path, 0)
