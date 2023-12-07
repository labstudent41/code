import cv2
import matplotlib.pyplot as plt

# scalar multiplication
img = cv2.imread('house.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
fimg = cv2.multiply(img, True)
cv2.imwrite('house-scaled.jpg', fimg)
plt.imshow(fimg)
plt.show()

img = cv2.imread('house-scaled.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# print(img)
plt.imshow(img)
plt.show()

house = plt.imread('house-scaled.jpg')
# print(house)
plt.imshow(house)
plt.show()

