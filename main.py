# code taken from https://www.pyimagesearch.com/2014/09/15/python-compare-two-images/

# import the necessary packages
from skimage.metrics import structural_similarity as ssim
import cv2

def compare_images(img1, img2):
    if check_size_equal(img1, img2):
        print ("Image sizes are equal")
        return ssim(img1, img2, multichannel=True)
    else:
        print ("Image sizes are not equal")
    if has_scale_factor(img1, img2):
        if img1.shape[0] > img2.shape[0]:
            resized = cv2.resize(img2, (img1.shape[1], img1.shape[0]), interpolation = cv2.INTER_AREA)
            size_check = check_size_equal(img1, resized)
            print ("Resized image dimensions are now equal to larger image: ", size_check)
            return ssim(img1, resized, multichannel=True)
        else:
            resized = cv2.resize(img1, (img2.shape[1], img2.shape[0]), interpolation = cv2.INTER_AREA)
            size_check = check_size_equal(img2, resized)
            print ("Resized image dimensions are now equal to larger image: ", size_check)
            return ssim(img2, resized, multichannel=True)
    else:
        return ("Images have no scale factor")


def check_size_equal(img1, img2):
    height_check = img1.shape[0] == img2.shape[0]
    width_check = img1.shape[1] == img2.shape[1]
    return height_check and width_check

def has_scale_factor(img1, img2):
    height_ratio = float(img1.shape[0])/img2.shape[0]
    width_ratio = float(img1.shape[1])/img2.shape[1]
    return height_ratio/width_ratio == 1.0

# deprecated
def find_scale_factor(img1, img2):
    return float(img1.shape[0])/img2.shape[0]


# load the images -- the original, the original + contrast,
# and the original + photoshop
prinz11 = cv2.imread("images/prinz eugen (azur lane) drawn by moyoron - bfb1f44395b74e7a1c8ffb31fa9b03d2.jpg")
prinz12 = cv2.imread("images/prinz eugen (azur lane) drawn by moyoron - 9facf3f48edbea83feb51d350d304f54.jpg")
prinz13 = cv2.imread("images/prinz eugen (azur lane) drawn by moyoron - 7a93c1324142c0edb61ceb1496646627.jpg")
lusty1 = cv2.imread("images/illustrious (azur lane) drawn by zynxy - 163198c4d8d26a59422161123d58d246.jpg")
prinz21 = cv2.imread("images/prinz eugen (azur lane) drawn by moyoron - 9b068e4a9e446878d93bf65b7f32a6cf.jpg")
prinz22 = cv2.imread("images/prinz eugen (azur lane) drawn by moyoron - 37a4db7a336da75fcb4884615e6bfdbc.jpg")
brem1 = cv2.imread("images/bremerton (azur lane) drawn by takurowo - 470122fdbd3dcc08f654f82b825d155b.png")
brem2 = cv2.imread("images/bremerton (azur lane) drawn by takurowo - 4e03899957524f85ad3f287ca9913eb2.png")
formi1 = cv2.imread("images/formidable (azur lane) drawn by oyabuli - 5575304c2e69eeaf5ace441cc9e50038.jpg")
formi2 = cv2.imread("images/formidable (azur lane) drawn by oyabuli - 236d7512f2c63cba690ce7b2e8bca664.jpg")

# equal size checking test
print ("equal size checking test")
print (check_size_equal(prinz11, prinz12))
print (check_size_equal(prinz11, lusty1))
print (check_size_equal(brem1, brem2))
print (check_size_equal(formi1, formi2))

# check if has a scale factor
print ("scale factor test")
print (has_scale_factor(prinz11, prinz12))
print (has_scale_factor(prinz11, lusty1))
print (has_scale_factor(brem1, brem2))
print (has_scale_factor(formi1, formi2))

# check if has a scale factor
print ("Finding the (height) scale factor")
print (find_scale_factor(prinz11, prinz12))
print (find_scale_factor(prinz11, lusty1))
print (find_scale_factor(brem1, brem2))
print (find_scale_factor(formi1, formi2))

# convert the images to grayscale
# original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
# contrast = cv2.cvtColor(contrast, cv2.COLOR_BGR2GRAY)
# shopped = cv2.cvtColor(shopped, cv2.COLOR_BGR2GRAY)
# other = cv2.cvtColor(other, cv2.COLOR_BGR2GRAY)

# compare the images
print ("Comparing Prinz Set 1")
print ("Comparing Prinz 1 with Prinz 1", compare_images(prinz11, prinz11))
print ("Comparing Prinz 1 with Prinz 2", compare_images(prinz11, prinz12))
print ("Comparing Prinz 1 with Prinz 3", compare_images(prinz12, prinz13))

print ("Comparing Prinz Set 2")
print ("Comparing Prinz 1 with Prinz 1", compare_images(prinz21, prinz21))
print ("Comparing Prinz 1 with Prinz 2", compare_images(prinz21, prinz22))

#NOTE: multichannel mkaes it take three times as long as grayscale

# # throws error since dimensions don't match
print ("Comparing Prinz Set1, Pic 1 with Lusty 1", compare_images(prinz11, lusty1))

print("Comparing Brem Set: ", compare_images(brem1, brem2))
print ("Checking Inversibility of resize function")
print("Comparing Brem Set Reversed: ", compare_images(brem1, brem2))

print("Comparing Formi Set: ", compare_images(formi1, formi2))
