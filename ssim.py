import cv2 as cv
from skimage import measure


# Calculate SSIM
first = cv.imread("/Users/adarsh/Desktop/res/4a1/input.jpg")

#second = cv.imread("captured.png")
second = cv.imread("/Users/adarsh/Desktop/res/4a1/gen.png")

first = cv.resize(first, (2576,1125))
second = cv.resize(second, (2576,1125))
first = cv.cvtColor(first, cv.COLOR_BGR2GRAY)
second = cv.cvtColor(second, cv.COLOR_BGR2GRAY)
s = measure.compare_ssim(first, second)

print(s)