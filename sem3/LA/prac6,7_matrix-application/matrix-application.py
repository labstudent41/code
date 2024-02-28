import numpy as np
import cv2
import matplotlib.pyplot as plt

### Part 1 --------------------------------------------------------------

# Read the input image
img = cv2.imread("house.png")

# Convert BGR to RGB & plot
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Disable X and Y axis
plt.axis("OFF")

# show the image
plt.imshow(img)
plt.show()

# Get image shape and dimension
rows, cols, dim = img.shape

# Transformation matrix for translation
m = np.float32([[1, 0, 50],
                [0, 1, 50],
                [0, 0, 1]])

# apply a perspective transformation to image
translated_img = cv2.warpPerspective(img, m, (cols, rows))

# disable X and Y axis
plt.axis('OFF')

# show the resulting image
plt.imshow(translated_img)
plt.show()

plt.imsave("house_translated.png", translated_img)

### Part 2 --------------------------------------------------------------

second = cv2.imread("rectangle.png")
first = cv2.imread("circle.png")
# print(first, second)

second = cv2.cvtColor(second, cv2.COLOR_BGR2RGB)
first = cv2.cvtColor(first, cv2.COLOR_BGR2RGB)

# simple matrix operation
manual_subs = second - first
# cv2.imshow("Manual output", manual_subs)

plt.imshow(manual_subs)
plt.show()

# OpenCV algorithms
subtracted = cv2.subtract(first, second)
# cv2.imshow("Output", subtracted)

plt.imshow(subtracted)
plt.show()

# simple matrix operation
manual_add = second + first

# OpenCV algorithms
added = cv2.add(first, second)

plt.imshow(manual_add)
plt.show()

plt.imshow(added)
plt.show()
