# code taken from https://www.pyimagesearch.com/2014/09/15/python-compare-two-images/

# import the necessary packages
from skimage.metrics import structural_similarity as ssim
import numpy as np
import cv2

def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err

def compare_images(imageA, imageB):
    # compute the mean squared error and structural similarity
    # index for the images
    # m = mse(imageA, imageB)
    # return m
    s = ssim(imageA, imageB)
    return s
    # return (f"{m},{s}")

# load the images -- the original, the original + contrast,
# and the original + photoshop
original = cv2.imread("images/prinz eugen (azur lane) drawn by moyoron - 7a93c1324142c0edb61ceb1496646627.jpg")
contrast = cv2.imread("images/prinz eugen (azur lane) drawn by moyoron - 9facf3f48edbea83feb51d350d304f54.jpg")
shopped = cv2.imread("images/prinz eugen (azur lane) drawn by moyoron - bfb1f44395b74e7a1c8ffb31fa9b03d2.jpg")
other = cv2.imread("images/illustrious (azur lane) drawn by zynxy - 163198c4d8d26a59422161123d58d246.jpg")

# convert the images to grayscale
original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
contrast = cv2.cvtColor(contrast, cv2.COLOR_BGR2GRAY)
shopped = cv2.cvtColor(shopped, cv2.COLOR_BGR2GRAY)
other = cv2.cvtColor(other, cv2.COLOR_BGR2GRAY)

# compare the images
print ("Comparing original with itself", compare_images(original, original))
print ("Comparing original with contrast", compare_images(original, contrast))
print ("Comparing original with the shopped", compare_images(original, shopped))
# throws error since dimensions don't match
# print ("Comparing original with completely different image", compare_images(original, other))
