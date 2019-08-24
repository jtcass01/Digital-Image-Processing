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

from scipy import misc
import os

class Quantizer(object):
    def __init__(self):
        pass

    def quantize_image(self):
        pass

if __name__ == "__main__":
    test_quantizer = Quantizer()

    # Read image:
    image = misc.imread(os.getcwd() + os.path.sep + ".." + os.path.sep + "lenna.jpg")


#    self.quantize_image
